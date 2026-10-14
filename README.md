# Pure API CRUD client

An installable Python client and read-only Typer CLI for Elsevier Pure API. The original specification defines the server path `/ws/api` and the `api-key` authentication header. Supply the full API URL; the client does not add a version segment.

Python 3.12 or newer is required.

## Install and configure

```sh
python -m venv .venv
. .venv/bin/activate
pip install .
# Or install the built wheel:
# pip install dist/pure_client-0.1.0-py3-none-any.whl
export PURE_API_BASE_URL=https://pure.example.edu/ws/api
# Set PURE_API_KEY securely in your environment or secret manager.
pure --help
```

`PURE_API_KEY` is required and sent only in the `api-key` header. There is no CLI credential option. Examples contain no credential values. `--base-url` overrides `PURE_API_BASE_URL`, even when supplied as an empty string (which fails validation). Global options go **before** the command group. The timeout defaults to 30 seconds; `--timeout` sets a finite positive duration in seconds for HTTPX connect/read/write/pool timeouts. This is a per-phase timeout, not an overall pagination deadline. TLS verification is enabled. Redirects and retries are disabled, avoiding unexpected credential forwarding or request replay. HTTP(S) base URLs are supported; use HTTPS for deployment.

## CLI

The CLI exposes list, UUID fetch, and JSON-body search for persons, research outputs, organizations, fingerprints, and concepts. It also reads fingerprints for a person:

```sh
pure persons list --size 100 --offset 0
pure persons get 11111111-1111-4111-8111-111111111111
pure persons search query.json --all
pure research-outputs list --all
pure research-outputs get 11111111-1111-4111-8111-111111111111
pure research-outputs search query.json --size 100 --offset 0
pure organizations list --order name
pure organizations get 11111111-1111-4111-8111-111111111111
pure organizations search query.json
pure fingerprints list --all
pure fingerprints get 11111111-1111-4111-8111-111111111111
pure fingerprints search fingerprint-query.json --all
pure concepts list --size 100
pure concepts get 11111111-1111-4111-8111-111111111111
pure concepts search query.json --all
pure persons fingerprints 11111111-1111-4111-8111-111111111111
pure --base-url https://pure.example.edu/ws/api --timeout 60 persons list
```

The identifier is a **UUID**, not a database ID. The API documents HTTP 301 when a record's UUID changes; this is reported as an HTTP failure rather than silently following the redirect.

An example `query.json` using fields present in all five query schemas:

```json
{"searchString":"Ada","size":100,"offset":0}
```

Search uses the corresponding POST `/persons/search`, `/research-outputs/search`, `/organizations/search`, `/fingerprints/search`, or `/concepts/search` operation and its generated query model (`PersonsQuery`, `ResearchOutputsQuery`, `OrganizationsQuery`, `FingerprintQuery`, or `ConceptQuery`). All five queries support `size`, `offset`, `uuids`, and `searchString`. Persons, research outputs, organizations, and concepts also support `orderings` and the write-only `orderBy`. Fingerprint queries instead support `relatedContentUuid` and `relatedContentSystemName`. UUID formats and JSON types are validated locally. Query files must contain a JSON object; malformed JSON, non-finite numeric constants, and duplicate keys are rejected.

List sends only the documented `size` and `offset` query parameters, plus optional `order` for persons, research outputs, organizations, and concepts. Fingerprint list commands do not expose or send `order`. The list schema limits `size` to 1000; the search schemas do not specify that maximum. The client additionally requires positive sizes and nonnegative offsets to make pagination useful. `--size` and `--offset` on search override values in the JSON body. `order` and `orderBy` examples are illustrative: use instance-supported ordering values. The YAML does not define a concepts ordering-discovery endpoint.

`pure persons fingerprints PERSON_UUID` calls the exact GET `/persons/{uuid}/fingerprints` endpoint and returns its `FingerprintListResult` JSON unchanged, including ranked concepts. This operation has no pagination parameters in the YAML, so the command offers neither `--size`, `--offset`, nor `--all`. A person UUID is required; API 403 and 404 responses produce HTTP diagnostics and exit code 5.

For a paginated fingerprint search filtered by related person content, `fingerprint-query.json` can contain the documented query fields:

```json
{"relatedContentUuid":"11111111-1111-4111-8111-111111111111","relatedContentSystemName":"Person","size":100,"offset":0}
```

`--all` is a **client-side option**, never an API parameter. It aggregates records from the selected offset and emits `{"items":[...]}`. Ordinary commands emit the original JSON response, preserving field names and extra fields. Pagination advances by the number of records returned (including server-capped pages), stops at the reported count or an empty page, and deduplicates by UUID, falling back to canonical JSON for records without UUIDs. A page containing no new records fails with a diagnostic rather than looping forever. A client-side limit of 10,000 pages also fails explicitly. Aggregation collects data in memory and returns no partial stdout on failure. Changing data on the server can affect offset pagination; use an appropriate stable ordering for large exports. There is no snapshot guarantee in this contract.

Successful data commands print a single JSON value to stdout. Diagnostics go to stderr, with no tracebacks by default. HTTP failures include status, actionable advice, and available `title`, `detail`, or `message` fields; credential values are redacted from these diagnostics. Network and model-processing exceptions are summarized without exposing raw exception messages or payloads.

| Exit code | Meaning |
| --- | --- |
| 0 | Success |
| 2 | Missing/invalid configuration or Typer command syntax/argument conversion error |
| 3 | Invalid workflow input or unreadable/invalid query file |
| 4 | Network failure or timeout |
| 5 | HTTP failure, including redirects |
| 6 | Invalid response, processing/JSON encoding failure, or pagination failure |

## Python

```python
from pure_client import PureClient, PureError

with PureClient.from_env(timeout=30) as pure:
    first_page = pure.list("persons", size=20)
    person = pure.get("persons", "11111111-1111-4111-8111-111111111111")
    matches = pure.search("persons", {"searchString": "Ada"}, all_pages=True)
    fingerprints = pure.person_fingerprints("11111111-1111-4111-8111-111111111111")
    concepts = pure.list("concepts", size=20)
```

Alternatively, use `PureClient(Settings(base_url=..., api_key=..., timeout=...))` when credentials come from a secret provider. `Settings.from_env` and `PureClient.from_env` accept an optional `base_url` override and an `environ` mapping. Keys are hidden in the public client and settings representations.

Other generated operations remain accessible through Python, including operations beyond the initial CLI scope:

```python
from pure_client import PureClient
from pure_client.sdk.api.person import person_list, person_query
from pure_client.sdk.models.persons_query import PersonsQuery

with PureClient.from_env() as pure:
    # Shared HTTP/network/processing error handling; returns a generated Response.
    response = pure.call(person_list, size=10, offset=0)
    page_model = response.parsed
    if page_model is not None:
        api_fields = page_model.to_dict()
    query_model = PersonsQuery(search_string="Ada", size=20)
    response = pure.call(person_query, body=query_model)

    # Direct SDK interface, for callers handling SDK exceptions themselves:
    response = person_list.sync_detailed(client=pure.sdk, size=10, offset=0)
```


