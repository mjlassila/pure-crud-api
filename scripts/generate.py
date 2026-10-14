"""Pinned generation, warning accounting, and runtime schema export."""
from collections import Counter
from pathlib import Path
import importlib.metadata
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import yaml
from openapi_python_client.utils import snake_case
from scripts.preprocess import preprocess

ROOT = Path(__file__).resolve().parents[1]

def runtime_schema(node):
    if isinstance(node, list):
        return [runtime_schema(v) for v in node]
    if not isinstance(node, dict):
        return node
    result = {k: runtime_schema(v) for k, v in node.items() if k != 'nullable'}
    if node.get('nullable'):
        return {'anyOf': [result, {'type': 'null'}]}
    return result

def main():
    if importlib.metadata.version('openapi-python-client') != '0.27.1':
        raise SystemExit('Use openapi-python-client==0.27.1')
    original = yaml.safe_load((ROOT / 'spec/pure-api-openapi.yaml').read_text())
    spec = preprocess(original)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        source = tmp / 'compatible.yaml'
        source.write_text(yaml.safe_dump(spec, sort_keys=False))
        destination = tmp / 'sdk'
        env = dict(os.environ)
        env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + env['PATH']
        command = [sys.executable, '-m', 'openapi_python_client', 'generate', '--path', str(source), '--config', str(ROOT / 'generator.yaml'), '--meta', 'none', '--output-path', str(destination)]
        result = subprocess.run(command, capture_output=True, text=True, env=env)
        log = result.stdout + result.stderr
        # Generator output contains a random staging path; normalize for reproducibility.
        log = log.replace(str(destination), '<generated-sdk>')
        (ROOT / 'docs/generation.log').write_text(log)
        if result.returncode:
            raise SystemExit(log)
        warning_blocks = re.split(r'(?=WARNING parsing )', log)
        warnings = {}
        for block in warning_blocks:
            match = re.match(r'WARNING parsing (\w+) (\S+) within', block)
            if match:
                warnings[(match[1].lower(), match[2])] = block.split('\n\n')[1].strip()
        if 'Unable to' in log or 'Skipping Integration' in log:
            raise SystemExit('Unexpected model or integration warning; review docs/generation.log')
        coverage = []
        for path, item in original['paths'].items():
            for method, operation in item.items():
                if method not in {'get','put','post','delete','patch','head','options','trace'}:
                    continue
                module = snake_case(operation['operationId'])
                tag = snake_case(operation['tags'][0])
                exists = (destination / 'api' / tag / (module + '.py')).is_file()
                warning = warnings.get((method, path))
                status = 'generated' if exists else 'unsupported'
                if exists and warning:
                    status = 'partial'
                if warning and '*/*' not in warning:
                    raise SystemExit(f'Unexpected warning for {method} {path}: {warning}')
                if not exists and not warning:
                    raise SystemExit(f'Unaccounted missing operation: {method} {path}')
                coverage.append({'operationId': operation['operationId'], 'method': method.upper(), 'path': path, 'status': status, 'module': f'pure_client.sdk.api.{tag}.{module}' if exists else None, 'reason': ('Wildcard binary request body is unsupported by generator' if not exists else 'Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes') if warning else None})
        target = ROOT / 'src/pure_client/sdk'
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(destination, target, ignore=shutil.ignore_patterns('__pycache__', '.ruff_cache'))
    (ROOT / 'docs/coverage.json').write_text(json.dumps(coverage, indent=2) + '\n')
    counts = Counter(row['status'] for row in coverage)
    lines = ['# SDK coverage', '', f"{len(coverage)} operations: " + ', '.join(f'{v} {k}' for k,v in sorted(counts.items())) + '.', '', 'Every operation is recorded in `coverage.json`. Generated means a module exists without a generation warning; it does not imply live verification. Partial binary downloads expose raw bytes through `sync_detailed().content` but lack a 200 parser. Unsupported wildcard uploads have no module. Changing `*/*` to a concrete MIME type would narrow the contract, so preprocessing does not do that. The smallest future extension is a generator template supporting arbitrary binary request media types.', '', '| Operation | Status | Cause |', '| --- | --- | --- |']
    lines += [f"| `{r['operationId']}` ({r['method']} `{r['path']}`) | {r['status']} | {r['reason']} |" for r in coverage if r['status'] != 'generated']
    (ROOT / 'docs/coverage.md').write_text('\n'.join(lines) + '\n')
    (ROOT / 'src/pure_client/schemas.json').write_text(json.dumps(runtime_schema({'components': {'schemas': spec['components']['schemas']}}), separators=(',',':')) + '\n')
    print(dict(counts))

if __name__ == '__main__':
    main()
