import json
from pathlib import Path
import httpx
import pytest
from pure_client import PureClient, Settings, PureError, load_query

UUID = '11111111-1111-4111-8111-111111111111'
RESOURCES = ['persons', 'organizations', 'research-outputs']

@pytest.mark.parametrize('resource', RESOURCES)
def test_list_fetch_search_contract(client_factory, record, resource):
    calls = []
    row = record(resource)
    def handle(request):
        calls.append(request)
        assert request.headers['api-key'] == 'private-test-key'
        assert 'Authorization' not in request.headers
        assert 'private-test-key' not in str(request.url)
        if request.url.path.endswith(UUID):
            return httpx.Response(200, json=row)
        return httpx.Response(200, json={'items': [row], 'count': 1, 'pageInformation': {'offset': 0, 'size': 2}})
    client = client_factory(handle)
    assert client.list(resource, size=2, order='name')['items'] == [row]
    assert client.get(resource, UUID) == row
    body = {'searchString': 'Ada', 'orderBy': 'name', 'uuids': [UUID], 'size': 2, 'offset': 0}
    assert client.search(resource, body)['items'] == [row]
    assert (calls[0].method, calls[0].url.path) == ('GET', '/ws/api/' + resource)
    assert dict(calls[0].url.params) == {'size': '2', 'offset': '0', 'order': 'name'}
    assert (calls[1].method, calls[1].url.path) == ('GET', '/ws/api/' + resource + '/' + UUID)
    assert (calls[2].method, calls[2].url.path) == ('POST', '/ws/api/' + resource + '/search')
    assert not calls[2].url.query
    assert json.loads(calls[2].content) == body
    assert calls[2].headers['content-type'] == 'application/json'
    assert 'private-test-key' not in repr(client)
    assert 'private-test-key' not in repr(client.settings)
    assert client.sdk._verify_ssl is True
    assert client.sdk._timeout.read == 30.0

@pytest.mark.parametrize('resource', RESOURCES)
@pytest.mark.parametrize('action', ['list', 'search'])
def test_paginate_capped_pages_and_empty_termination(client_factory, record, resource, action):
    offsets = []
    identifiers = ['11111111-1111-4111-8111-111111111111', '22222222-2222-4222-8222-222222222222']
    def handle(request):
        offset = int(request.url.params['offset']) if action == 'list' else json.loads(request.content)['offset']
        offsets.append(offset)
        if action == 'search':
            assert json.loads(request.content)['searchString'] == 'Ada'
        rows = [record(resource, identifiers[offset])] if offset < 2 else []
        return httpx.Response(200, json={'items': rows})
    client = client_factory(handle)
    if action == 'list':
        result = client.list(resource, size=100, all_pages=True)
    else:
        result = client.search(resource, {'searchString': 'Ada', 'size': 100}, all_pages=True)
    assert [r['uuid'] for r in result['items']] == identifiers
    assert offsets == [0, 1, 2]

@pytest.mark.parametrize('action', ['list','search'])
def test_pagination_deduplicates_and_count_terminates(client_factory, record, action):
    a = record('persons')
    b = record('persons','22222222-2222-4222-8222-222222222222')
    calls = []
    def handle(request):
        calls.append(request)
        return httpx.Response(200, json={'items': [a] if len(calls) == 1 else [a,b], 'count': 3})
    client = client_factory(handle)
    result = client.list('persons', all_pages=True) if action == 'list' else client.search('persons', {}, all_pages=True)
    assert result['items'] == [a,b]
    assert len(calls) == 2

def test_pagination_repeated_page_fails(client_factory, record):
    client = client_factory(lambda r: httpx.Response(200,json={'items': [record('persons')]}))
    with pytest.raises(PureError, match='progress') as error:
        client.list('persons', all_pages=True)
    assert error.value.code == 6

@pytest.mark.parametrize('status', [301,401,403,404,429,500,503])
def test_http_errors_actionable_and_redacted(client_factory, status):
    client = client_factory(lambda r: httpx.Response(status,json={'title': 'Problem', 'detail': 'private-test-key echoed\ninvalid'}))
    with pytest.raises(PureError) as error:
        client.get('persons', UUID)
    assert error.value.code == 5
    assert f'HTTP {status}' in str(error.value)
    assert 'Problem' in str(error.value)
    assert 'private-test-key' not in str(error.value)
    assert '\n' not in str(error.value)

@pytest.mark.parametrize('exc', [httpx.ReadTimeout, httpx.ConnectError])
def test_network_failures_do_not_leak(client_factory, exc):
    def handle(request):
        raise exc('private-test-key', request=request)
    with pytest.raises(PureError) as error:
        client_factory(handle).list('persons')
    assert error.value.code == 4
    assert 'private-test-key' not in str(error.value)

@pytest.mark.parametrize('payload', [b'bad JSON', b'[]', b'{"items":"wrong"}', b'{"items":[{"uuid":"bad"}]}', b'{"count":"invalid","items":[]}', b'{"items":[],"count":NaN}'])
def test_malformed_responses(client_factory, payload):
    client = client_factory(lambda r: httpx.Response(200,content=payload))
    with pytest.raises(PureError) as error:
        client.list('persons')
    assert error.value.code == 6

@pytest.mark.parametrize('body', [[], {'size': True}, {'size': 0}, {'offset': -1}, {'searchString': 5}, {'uuids': ['invalid']}, {'orderings': 'name'}])
def test_invalid_query_never_sends(client_factory, body):
    def handle(request):
        pytest.fail('Input must fail before HTTP')
    with pytest.raises(PureError) as error:
        client_factory(handle).search('persons', body)
    assert error.value.code == 3

def test_search_override_and_input_immutability(client_factory):
    calls = []
    def handle(request):
        calls.append(json.loads(request.content))
        return httpx.Response(200,json={'items': []})
    body = {'size': 100, 'offset': 5, 'searchString': 'Ada'}
    client_factory(handle).search('persons', body, size=3, offset=7, all_pages=True)
    assert calls == [{'size': 3,'offset':7,'searchString':'Ada'}]
    assert body['size'] == 100 and body['offset'] == 5

@pytest.mark.parametrize('value', ['not-a-uuid','123','../../../path'])
def test_uuid_input(client_factory, value):
    with pytest.raises(PureError) as error:
        client_factory(lambda r: pytest.fail('No request expected')).get('persons', value)
    assert error.value.code == 3

@pytest.mark.parametrize('text', ['[]','null','{bad}', '{"size":NaN}', '{"size":1,"size":2}'])
def test_query_file_invalid(tmp_path, text):
    path = tmp_path / 'query.json'
    path.write_text(text)
    with pytest.raises(PureError) as error:
        load_query(path)
    assert error.value.code == 3

def test_query_file_valid_and_missing(tmp_path):
    path = tmp_path/'query.json'
    path.write_text('{"searchString":"Ada"}')
    assert load_query(path) == {'searchString':'Ada'}
    with pytest.raises(PureError):
        load_query(tmp_path/'missing')

def test_config_precedence_and_url():
    env = {'PURE_API_BASE_URL': 'https://env.example/ws/api/', 'PURE_API_KEY': 'secret'}
    assert Settings.from_env(environ=env).base_url == 'https://env.example/ws/api'
    assert Settings.from_env(base_url='https://option.example/ws/api/',environ=env).base_url == 'https://option.example/ws/api'

@pytest.mark.parametrize('url', ['', '/ws/api','ftp://example/ws/api','https://secret@example/ws/api','https://example/ws/api?api-key=secret','https://example/#x','https://example:invalid/ws/api'])
def test_invalid_base_url(url):
    with pytest.raises(PureError) as error:
        Settings(url,'secret')
    assert error.value.code == 2
    assert 'secret' not in str(error.value)

@pytest.mark.parametrize('timeout', [0,-1,float('inf'),float('nan'),True])
def test_invalid_timeout(timeout):
    with pytest.raises(PureError):
        Settings('https://example/ws/api','secret',timeout)

@pytest.mark.parametrize('env', [{}, {'PURE_API_BASE_URL':'https://example/ws/api'}, {'PURE_API_BASE_URL':'https://example/ws/api','PURE_API_KEY':''}])
def test_missing_configuration(env):
    with pytest.raises(PureError) as error:
        Settings.from_env(environ=env)
    assert error.value.code == 2

@pytest.mark.parametrize('status', [200,401])
def test_generated_async_interface_has_compatible_hooks(status):
    import asyncio
    from pure_client.sdk.api.person import person_list
    async def execute():
        transport = httpx.MockTransport(lambda r: httpx.Response(status,json={'items':[]} if status==200 else {'title':'Denied'}))
        async with PureClient(Settings('https://example/ws/api','private-test-key'), transport=transport) as client:
            if status == 200:
                result = await person_list.asyncio_detailed(client=client.sdk)
                assert result.parsed.to_dict() == {'items':[]}
            else:
                with pytest.raises(PureError,match='HTTP 401'):
                    await person_list.asyncio_detailed(client=client.sdk)
    asyncio.run(execute())

def test_undocumented_success_status_fails(client_factory):
    with pytest.raises(PureError) as error:
        client_factory(lambda r: httpx.Response(201,json={'items':[]})).list('persons')
    assert error.value.code == 6
