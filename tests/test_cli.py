import json
import httpx
import pytest
from typer.testing import CliRunner
from pure_client import PureClient
from pure_client.cli import app

runner = CliRunner()
UUID = '11111111-1111-4111-8111-111111111111'

@pytest.fixture
def configured(monkeypatch):
    monkeypatch.setenv('PURE_API_BASE_URL','https://env.example/ws/api')
    monkeypatch.setenv('PURE_API_KEY','private-test-key')
    calls = []
    def install(handler):
        def construct(settings):
            def tracked(request):
                calls.append(request)
                return handler(request)
            return PureClient(settings, transport=httpx.MockTransport(tracked))
        monkeypatch.setattr('pure_client.cli.PureClient',construct)
        return calls
    return install

@pytest.mark.parametrize('resource', ['persons','organizations','research-outputs'])
@pytest.mark.parametrize('action', ['list','get','search'])
def test_cli_workflows(configured, record, tmp_path, resource, action):
    row = record(resource)
    calls = configured(lambda r: httpx.Response(200,json=row if action == 'get' else {'items':[row],'count':1}))
    args = ['--base-url','https://option.example/ws/api',resource, action]
    if action == 'get':
        args.append(UUID)
    if action == 'search':
        path = tmp_path/'query.json'
        path.write_text('{"searchString":"Ada"}')
        args.append(str(path))
    result = runner.invoke(app,args)
    assert result.exit_code == 0, result.output
    assert json.loads(result.stdout) == (row if action == 'get' else {'items':[row],'count':1})
    assert result.stderr == ''
    assert calls[0].url.host == 'option.example'
    assert calls[0].headers['api-key'] == 'private-test-key'

@pytest.mark.parametrize('status', [401,404,500])
def test_cli_http_errors(configured,status):
    configured(lambda r: httpx.Response(status,json={'title':'Action failed', 'detail':'private-test-key'}))
    result = runner.invoke(app,['persons','list'])
    assert result.exit_code == 5
    assert result.stdout == ''
    assert f'HTTP {status}' in result.stderr
    assert 'Action failed' in result.stderr
    assert 'private-test-key' not in result.output
    assert 'Traceback' not in result.output

@pytest.mark.parametrize('kind', ['timeout','network','malformed'])
def test_cli_failure_codes(configured,kind):
    def handle(request):
        if kind == 'timeout':
            raise httpx.ReadTimeout('private-test-key',request=request)
        if kind == 'network':
            raise httpx.ConnectError('private-test-key',request=request)
        return httpx.Response(200,content=b'no JSON')
    configured(handle)
    result = runner.invoke(app,['persons','list'])
    assert result.exit_code == (6 if kind == 'malformed' else 4)
    assert result.stdout == ''
    assert result.stderr
    assert 'Traceback' not in result.output and 'private-test-key' not in result.output

@pytest.mark.parametrize('args', [['persons','get','123'],['persons','list','--size','1001'],['persons','list','--offset','-1'],['persons','list','--size','bad']])
def test_cli_invalid_input(configured,args):
    configured(lambda r: pytest.fail('Must not make request'))
    result = runner.invoke(app,args)
    assert result.exit_code in (2,3)
    assert result.stdout == '' and result.stderr

@pytest.mark.parametrize('text', ['bad json','[]','{"searchString":3}'])
def test_cli_bad_query(configured,tmp_path,text):
    configured(lambda r: pytest.fail('Must not make request'))
    path = tmp_path/'query.json'
    path.write_text(text)
    result = runner.invoke(app,['persons','search',str(path)])
    assert result.exit_code == 3
    assert result.stdout == '' and result.stderr

def test_cli_configuration_and_help(monkeypatch):
    monkeypatch.delenv('PURE_API_BASE_URL',raising=False)
    monkeypatch.delenv('PURE_API_KEY',raising=False)
    monkeypatch.setattr('pure_client.cli.PureClient',lambda s: pytest.fail('No HTTP expected'))
    result = runner.invoke(app,['persons','list'])
    assert result.exit_code == 2 and result.stdout == ''
    assert 'PURE_API_BASE_URL' in result.stderr
    for args in [['--help'],['persons','--help'],['research-outputs','search','--help'],['organizations','get','--help']]:
        result = runner.invoke(app,args)
        assert result.exit_code == 0
        assert 'Usage' in result.stdout

def test_cli_all_pages(configured,record):
    calls = []
    def handle(request):
        calls.append(request)
        return httpx.Response(200,json={'items':[record('persons')]} if len(calls)==1 else {'items':[]})
    configured(handle)
    result = runner.invoke(app,['persons','list','--all'])
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {'items':[record('persons')]}
    assert [r.url.params['offset'] for r in calls] == ['0','1']
