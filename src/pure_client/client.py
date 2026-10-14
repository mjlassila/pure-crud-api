"""Public configured SDK and shared read workflows, with no handwritten HTTP requests."""
from dataclasses import dataclass, field
from importlib import import_module
import json
from pathlib import Path
from urllib.parse import quote
from uuid import UUID
import httpx
from .config import Settings
from .errors import PureError
from .sdk.client import Client
from .sdk.types import UNSET
from .validation import validate

RESOURCES = {
    'persons': ('person', 'PersonsQuery', 'Person'),
    'organizations': ('organization', 'OrganizationsQuery', 'Organization'),
    'research-outputs': ('research_output', 'ResearchOutputsQuery', 'ResearchOutput'),
}
QUERY_MODULES = {'PersonsQuery': 'persons_query', 'OrganizationsQuery': 'organizations_query', 'ResearchOutputsQuery': 'research_outputs_query'}

class _ConfiguredSDK(Client):
    """Keep sync and async response hooks compatible without editing generated code."""
    async def _check_async_http(self, response):
        await response.aread()
        for hook in self._httpx_args['event_hooks']['response']:
            hook(response)

    def get_async_httpx_client(self):
        client = super().get_async_httpx_client()
        client.event_hooks['response'] = [self._check_async_http]
        return client


@dataclass(repr=False)
class PureClient:
    settings: Settings
    transport: httpx.BaseTransport | None = field(default=None, repr=False)
    sdk: Client = field(init=False, repr=False)

    def __post_init__(self):
        args = {'event_hooks': {'response': [self._check_http]}}
        if self.transport is not None:
            args['transport'] = self.transport
        self.sdk = _ConfiguredSDK(base_url=self.settings.base_url, headers={'api-key': self.settings.api_key}, timeout=httpx.Timeout(self.settings.timeout), verify_ssl=True, follow_redirects=False, raise_on_unexpected_status=False, httpx_args=args)

    def __repr__(self):
        return f'PureClient(base_url={self.settings.base_url!r}, timeout={self.settings.timeout!r})'

    @classmethod
    def from_env(cls, *, base_url=None, timeout=30.0, environ=None, transport=None):
        return cls(Settings.from_env(base_url=base_url, timeout=timeout, environ=environ), transport=transport)

    def __enter__(self):
        self.sdk.__enter__()
        return self

    def __exit__(self, *args):
        return self.sdk.__exit__(*args)

    async def __aenter__(self):
        await self.sdk.__aenter__()
        return self

    async def __aexit__(self, *args):
        return await self.sdk.__aexit__(*args)

    def _redact(self, text):
        for secret in (self.settings.api_key, quote(self.settings.api_key, safe=''), json.dumps(self.settings.api_key)[1:-1]):
            text = text.replace(secret, '[redacted]')
        return text

    def _check_http(self, response):
        if 200 <= response.status_code < 300:
            return
        response.read()
        advice = {401: 'Check PURE_API_KEY.', 403: 'Check API key permissions.', 404: 'Check the UUID and base URL.', 301: 'The record UUID changed; consult the Location header.', 429: 'Retry later; the API rate limit was reached.'}.get(response.status_code, 'Check the API response and server availability.')
        details = []
        try:
            body = response.json()
            if isinstance(body, dict):
                for name in ('title', 'detail', 'message'):
                    if isinstance(body.get(name), str):
                        details.append(body[name])
        except (ValueError, UnicodeError):
            pass
        # Escape control characters to keep diagnostics on a single line.
        detail = ' '.join(' '.join(v.split()) for v in details)
        message = self._redact(f'HTTP {response.status_code}: {advice}' + (f' {detail}' if detail else ''))[:2000]
        raise PureError(message, 5)

    def call(self, operation, **kwargs):
        """Call a generated operation's sync_detailed with shared error handling."""
        try:
            return operation.sync_detailed(client=self.sdk, **kwargs)
        except PureError:
            raise
        except httpx.TimeoutException:
            raise PureError('Request timed out. Adjust --timeout or check server availability.', 4) from None
        except httpx.RequestError:
            raise PureError('Network request failed. Check the base URL, connectivity, and TLS certificates.', 4) from None
        except Exception:
            # Generated model exceptions can contain payloads; do not expose them.
            raise PureError('Could not process the API response. Check that the server uses the supplied Pure 5.36.3 contract.', 6) from None

    def _operation(self, resource, action):
        if resource not in RESOURCES:
            raise PureError('Unknown resource; choose persons, organizations, or research-outputs.', 3)
        tag, _, _ = RESOURCES[resource]
        return import_module(f'.sdk.api.{tag}.{tag}_{action}', package='pure_client')

    def _data(self, operation, schema, **kwargs):
        result = self.call(operation, **kwargs)
        if result.status_code != 200:
            raise PureError('API returned an undocumented success status for this workflow.', 6)
        try:
            data = json.loads(result.content, parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
            validate(data, schema, response=True)
            return data
        except PureError:
            raise
        except Exception:
            raise PureError('API returned malformed JSON or an invalid response.', 6) from None

    def get(self, resource: str, uuid: str | UUID):
        operation = self._operation(resource, 'get')
        try:
            identifier = UUID(str(uuid))
        except (ValueError, TypeError, AttributeError):
            raise PureError('Identifier must be a valid UUID.', 3) from None
        return self._data(operation, RESOURCES[resource][2], uuid=identifier)

    def list(self, resource: str, *, size=10, offset=0, order=None, all_pages=False):
        operation = self._operation(resource, 'list')
        self._paging(size, offset, list_request=True)
        if order is not None and not isinstance(order, str):
            raise PureError('Order must be a string from the resource orderings operation.', 3)
        def page(current):
            return self._data(operation, RESOURCES[resource][2] + 'ListResult', size=size, offset=current, order=order if order is not None else UNSET)
        return self._pages(page, offset) if all_pages else page(offset)

    def search(self, resource: str, body: dict, *, size=None, offset=None, all_pages=False):
        operation = self._operation(resource, 'query')
        if not isinstance(body, dict):
            raise PureError('Search input must be a JSON object.', 3)
        query = dict(body)
        if size is not None:
            query['size'] = size
        if offset is not None:
            query['offset'] = offset
        self._paging(query.get('size', 10), query.get('offset', 0))
        name = RESOURCES[resource][1]
        validate(query, name)
        model = getattr(import_module(f'.sdk.models.{QUERY_MODULES[name]}', package='pure_client'), name)
        def page(current):
            payload = dict(query)
            if all_pages:
                payload['offset'] = current
                payload.setdefault('size', 10)
            try:
                parsed = model.from_dict(payload)
            except Exception:
                raise PureError('Could not construct the generated search model.', 3) from None
            return self._data(operation, RESOURCES[resource][2] + 'ListResult', body=parsed)
        return self._pages(page, query.get('offset', 0)) if all_pages else page(query.get('offset', 0))

    @staticmethod
    def _paging(size, offset, list_request=False):
        if isinstance(size, bool) or not isinstance(size, int) or size <= 0 or (list_request and size > 1000):
            raise PureError('Size must be a positive integer' + (' at most 1000 for list requests.' if list_request else '.'), 3)
        if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
            raise PureError('Offset must be a nonnegative integer.', 3)

    def _pages(self, page, offset):
        items = []
        seen = set()
        for _ in range(10000):
            data = page(offset)
            rows = data.get('items')
            if not isinstance(rows, list):
                raise PureError('Paginated response must contain an items array.', 6)
            if not rows:
                return {'items': items}
            fresh = 0
            for row in rows:
                identity = ('uuid', str(row['uuid']).lower()) if row.get('uuid') else ('value', json.dumps(row, sort_keys=True, separators=(',', ':')))
                if identity not in seen:
                    items.append(row)
                    seen.add(identity)
                    fresh += 1
            if not fresh:
                raise PureError('Pagination stopped making progress; the server may be ignoring offset.', 6)
            # Advance by records actually returned, so server-capped pages do not skip records.
            offset += len(rows)
            count = data.get('count')
            if isinstance(count, int) and offset >= count:
                return {'items': items}
        raise PureError('Pagination exceeded the client-side limit of 10000 pages; narrow the search.', 6)


def load_query(path: Path | str):
    try:
        text = Path(path).read_text(encoding='utf-8')
        def pairs(values):
            result = {}
            for key, value in values:
                if key in result:
                    raise ValueError('duplicate key')
                result[key] = value
            return result
        data = json.loads(text, object_pairs_hook=pairs, parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
    except (OSError, ValueError, UnicodeError):
        raise PureError('Cannot read query file as valid UTF-8 JSON; check the file and JSON syntax (including duplicate keys).', 3) from None
    if not isinstance(data, dict):
        raise PureError('Query file must contain a JSON object.', 3)
    return data
