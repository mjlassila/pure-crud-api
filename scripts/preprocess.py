"""Flatten object inheritance for openapi-python-client without changing wire fields."""
from copy import deepcopy
from pathlib import Path
import yaml

ANNOTATIONS = {'description', 'title', 'example', 'deprecated', 'readOnly', 'writeOnly'}

def intersect(a, b):
    result = deepcopy(a)
    for key, value in b.items():
        if key not in result or key in ANNOTATIONS:
            result[key] = deepcopy(value)
        elif key == 'properties':
            for name, prop in value.items():
                result[key][name] = intersect(result[key][name], prop) if name in result[key] else deepcopy(prop)
        elif key == 'required':
            result[key] = sorted(set(result[key]) | set(value))
        elif key == 'items':
            result[key] = intersect(result[key], value)
        elif key == 'nullable':
            result[key] = result[key] and value
        elif key in {'minimum', 'minLength', 'minItems', 'minProperties'}:
            result[key] = max(result[key], value)
        elif key in {'maximum', 'maxLength', 'maxItems', 'maxProperties'}:
            result[key] = min(result[key], value)
        elif key == 'enum':
            result[key] = [v for v in result[key] if v in value]
        elif result[key] != value:
            raise ValueError(f'Cannot safely intersect {key}: {result[key]!r}, {value!r}')
    # Null must be admitted by both constraints, including an absent nullable flag.
    if a.get('nullable') or b.get('nullable'):
        result['nullable'] = bool(a.get('nullable') and b.get('nullable'))
    return result

def preprocess(spec):
    result = deepcopy(spec)
    schemas = spec['components']['schemas']
    cache = {}
    def flatten(node, trail=()):
        node = deepcopy(node)
        if 'allOf' not in node:
            return node
        parts = node.pop('allOf')
        merged = {'type': 'object'}
        for part in parts:
            if '$ref' in part:
                name = part['$ref'].removeprefix('#/components/schemas/')
                if name in trail:
                    raise ValueError('Cyclic inheritance')
                if name not in cache:
                    cache[name] = flatten(schemas[name], trail + (name,))
                part = deepcopy(cache[name])
            else:
                part = flatten(part, trail)
            if part.get('type') != 'object':
                raise ValueError('Only object inheritance can be flattened')
            # A parent's dispatch mapping applies when referenced as the parent,
            # not when constructing a specific subclass. Keep subclass mappings.
            part.pop('discriminator', None)
            merged = intersect(merged, part)
        nullable = node.pop('nullable', None)
        merged = intersect(merged, node)
        if nullable is not None:
            merged['nullable'] = nullable
        return merged
    for name, node in schemas.items():
        result['components']['schemas'][name] = flatten(node, (name,))
    return result

if __name__ == '__main__':
    import sys
    spec = yaml.safe_load(Path(sys.argv[1]).read_text())
    Path(sys.argv[2]).write_text(yaml.safe_dump(preprocess(spec), sort_keys=False))
