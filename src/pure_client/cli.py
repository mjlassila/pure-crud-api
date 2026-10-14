"""Read-only Typer workflows backed by the generated SDK."""
import json
from pathlib import Path
from typing import Annotated
import typer
from .client import PureClient, RESOURCES, ORDERED_RESOURCES, load_query, load_person_uuids
from .config import Settings
from .errors import PureError

app = typer.Typer(help='Elsevier Pure 5.36.3 read-only workflows.', no_args_is_help=True, pretty_exceptions_enable=False)

@app.callback()
def configure(ctx: typer.Context, base_url: Annotated[str | None, typer.Option('--base-url', help='Full API URL; overrides PURE_API_BASE_URL.')] = None, timeout: Annotated[float, typer.Option('--timeout', help='Client-side timeout in seconds (finite and positive).')] = 30.0):
    # Defer validation so help works without configuration.
    ctx.obj = {'base_url': base_url, 'timeout': timeout}


def run(ctx, resource, action, **kwargs):
    try:
        settings = Settings.from_env(**ctx.obj)
        if action == 'person_fingerprints':
            uuid_file = kwargs.pop('uuid_file', None)
            if (kwargs.get('uuid') is None) == (uuid_file is None):
                raise PureError('Provide either a person UUID or --file, but not both.', 3)
            if uuid_file is not None:
                action = 'persons_fingerprints'
                kwargs = {'uuids': load_person_uuids(uuid_file)}
        if action == 'search':
            kwargs['body'] = load_query(kwargs.pop('query_file'))
        with PureClient(settings) as client:
            workflow = getattr(client, action)
            data = workflow(**kwargs) if resource is None else workflow(resource, **kwargs)
        typer.echo(json.dumps(data, ensure_ascii=False, allow_nan=False))
    except PureError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(error.code) from None
    except (TypeError, ValueError, UnicodeError):
        typer.echo('Could not encode the API response as JSON.', err=True)
        raise typer.Exit(6) from None


def commands(resource):
    group = typer.Typer(help=f'Read {resource}.', no_args_is_help=True)

    def list_records(ctx: typer.Context, size: Annotated[int, typer.Option(help='API page size, maximum 1000.')] = 10, offset: Annotated[int, typer.Option(help='API record offset.')] = 0, order: Annotated[str | None, typer.Option(help='API ordering value; use an ordering supported by your Pure instance.')] = None, all_pages: Annotated[bool, typer.Option('--all', help='Client-side aggregation of pages.')] = False):
        run(ctx, resource, 'list', size=size, offset=offset, order=order, all_pages=all_pages)

    if resource in ORDERED_RESOURCES:
        group.command('list')(list_records)
    else:
        @group.command('list')
        def list_unordered(ctx: typer.Context, size: Annotated[int, typer.Option(help='API page size, maximum 1000.')] = 10, offset: Annotated[int, typer.Option(help='API record offset.')] = 0, all_pages: Annotated[bool, typer.Option('--all', help='Client-side aggregation of pages.')] = False):
            run(ctx, resource, 'list', size=size, offset=offset, all_pages=all_pages)

    if resource == 'persons':
        @group.command('fingerprints')
        def person_fingerprints(ctx: typer.Context, uuid: Annotated[str | None, typer.Argument(help='Person UUID; use this or --file.')] = None, uuid_file: Annotated[Path | None, typer.Option('--file', help='UTF-8 file with one person UUID per line or a JSON array of UUID strings.')] = None):
            run(ctx, None, 'person_fingerprints', uuid=uuid, uuid_file=uuid_file)

    @group.command('get')
    def get_record(ctx: typer.Context, uuid: Annotated[str, typer.Argument(help='Record UUID as defined by the API.')]):
        run(ctx, resource, 'get', uuid=uuid)

    @group.command('search')
    def search_records(ctx: typer.Context, query_file: Annotated[Path, typer.Argument(help='UTF-8 JSON query body file.')], size: Annotated[int | None, typer.Option(help='Override size in the API query body.')] = None, offset: Annotated[int | None, typer.Option(help='Override offset in the API query body.')] = None, all_pages: Annotated[bool, typer.Option('--all', help='Client-side aggregation of pages.')] = False):
        run(ctx, resource, 'search', query_file=query_file, size=size, offset=offset, all_pages=all_pages)

    return group

for resource in RESOURCES:
    app.add_typer(commands(resource), name=resource)

if __name__ == '__main__':
    app()
