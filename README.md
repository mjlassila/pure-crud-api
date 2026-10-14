# Pure client

An installable Python client and read-only Typer CLI for the attached Elsevier Pure API **5.36.3** contract. The original specification defines the server path `/ws/api` and the `api-key` authentication header. Supply the full API URL; the client does not add a version segment.

Python 3.12 or newer is required. Generated interfaces are isolated in `src/pure_client/sdk`; shared configuration, error handling, and workflows are handwritten in `src/pure_client`. This implementation uses `openapi-python-client`, not `UMNLibraries/pureapi`.

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

The initial CLI exposes exactly three workflows for each resource:

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
pure --base-url https://pure.example.edu/ws/api --timeout 60 persons list
```

The identifier is a **UUID**, not a database ID. The API documents HTTP 301 when a record's UUID changes; this is reported as an HTTP failure rather than silently following the redirect.

An example `query.json` using fields present in all three query schemas:

```json
{"searchString":"Ada","size":100,"offset":0}
```

Search uses the corresponding POST `/persons/search`, `/research-outputs/search`, or `/organizations/search` operation and a generated `PersonsQuery`, `ResearchOutputsQuery`, or `OrganizationsQuery` model. Query fields are `size`, `offset`, `orderings`, `uuids`, `searchString`, and the write-only `orderBy`. UUID formats and JSON types are validated locally. Query files must contain a JSON object; malformed JSON, non-finite numeric constants, and duplicate keys are rejected.

List sends only the documented `size`, `offset`, and optional `order` query parameters. The list schema limits `size` to 1000; the search schemas do not specify that maximum. The client additionally requires positive sizes and nonnegative offsets to make pagination useful. `--size` and `--offset` on search override values in the JSON body. `order` and `orderBy` examples are illustrative: obtain instance-specific valid values from the resource's generated orderings operation.

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

`sync`, `sync_detailed`, `asyncio`, and `asyncio_detailed` are generated operation interfaces. Use the shared wrapper for sync operations. For async usage, use `async with PureClient.from_env() as pure:` and call a generated `asyncio_detailed(client=pure.sdk, ...)` operation. Sync and async SDK clients receive appropriate response hooks, authentication, timeouts, and TLS settings. Direct async callers are responsible for network/model exception handling; the handwritten workflows and `call` are synchronous. Generated classes do not enforce every schema constraint. The handwritten list/get/search workflows validate input and response JSON against packaged local schemas, then preserve the API response JSON. Generic `call` applies HTTP and processing error handling but does not add schema validation to every generated operation. Do not log raw SDK clients, request headers, HTTPX debug traces, or payloads; generated client representations are outside the wrapper's redaction guarantees.

## Generation checkpoint and coverage

Generation is pinned to **openapi-python-client 0.27.1**. The original `spec/pure-api-openapi.yaml` is byte-for-byte unchanged. Initial unmodified generation produced inheritance/model warnings plus unsupported wildcard binary request/response warnings; its captured output is in `docs/generation-original.log`.

The reproducible preprocessing step in `scripts/preprocess.py` flattens object `allOf` inheritance. It resolves inherited properties, unions required fields, and intersects duplicate property constraints (including nullable arrays). Discriminator mappings remain on their declaring parent and are not inherited by concrete subclasses; inherited discriminator fields remain present. This avoids generator failures when combining a nullable/polymorphic parent with a concrete object and when merging arrays with differing nullability. Unknown conflicting constraints fail rather than being silently overwritten. Paths, methods, parameters, bodies, authentication, and response references are unchanged. Runtime JSON Schema conversion expresses OpenAPI `nullable` as a union with null. Focused tests verify inherited constraints, nullability, and unchanged operation definitions. The temporary compatible YAML is an intermediate file and does not replace the original.

Exact regeneration commands from the repository root:

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.lock
python -m scripts.generate
```

`python -m scripts.generate` runs preprocessing followed by:

```sh
python -m openapi_python_client generate \
  --path <temporary-compatible.yaml> --config generator.yaml \
  --meta none --output-path <temporary-sdk>
```

To inspect preprocessing independently:

```sh
mkdir -p work
python scripts/preprocess.py spec/pure-api-openapi.yaml work/compatible.yaml
```

Generation only replaces `src/pure_client/sdk`, refreshes the runtime `schemas.json`, and writes generation and coverage reports. It preserves all handwritten modules, tests, and configuration. Never hand-edit generated SDK files. The lock records the generator, formatter, build tools, test tools, and transitive versions used here.

**970 operations are accounted for: 928 generated without operation warnings, 21 partially supported binary downloads, and 21 unsupported wildcard uploads.** See [the coverage report](docs/coverage.md) for every limitation and [the machine-readable inventory](docs/coverage.json) for every operation and module. Binary downloads expose raw bytes via `sync_detailed().content`, but have no generated 200 response parser. The generator rejects wildcard `*/*` upload bodies entirely. Substituting a concrete MIME type would narrow the API contract, so this implementation does not make that change. The smallest future alternative is a generator template supporting wildcard binary request bodies; no generator switch or handwritten endpoint replacement is included. The SDK must therefore **not** be described as complete endpoint support.

## Tests and builds

```sh
pip install -r requirements-dev.lock
pytest -q
python -m build --no-isolation
python -m venv work/smoke-venv
work/smoke-venv/bin/pip install dist/pure_client-0.1.0-py3-none-any.whl
work/smoke-venv/bin/python -c 'from pure_client import PureClient, Settings; from pure_client.sdk.models.persons_query import PersonsQuery; print(PersonsQuery(search_string="Ada").to_dict())'
work/smoke-venv/bin/pure --help
```

Automated tests use HTTPX MockTransport; they need no credentials and do not call a live Pure instance. They cover request contract matching for all three resources, configuration precedence, authentication, pagination, stdout/stderr and exit codes, invalid input, HTTP failures, timeouts, malformed responses, model imports, coverage accounting, and preprocessing. See [verification results](docs/verification.md) for commands actually run, regeneration preservation checks, and the isolated installation smoke test. No live API validation has been performed. Generated operations beyond the representative workflows are import-checked and inventoried, not individually behavior-tested.
