"""Validate JSON against local contract schemas; generated models do not validate types."""
from functools import lru_cache
from importlib.resources import files
import json
from jsonschema import Draft202012Validator, FormatChecker
from .errors import PureError

@lru_cache
def validator(name: str):
    root = json.loads(files('pure_client').joinpath('schemas.json').read_text())
    root['$ref'] = f'#/components/schemas/{name}'
    return Draft202012Validator(root, format_checker=FormatChecker())

def validate(data, name: str, *, response: bool = False):
    error = next(validator(name).iter_errors(data), None)
    if error is not None:
        # Do not include invalid values: the API may echo credentials in them.
        location = '.'.join(str(p) for p in error.absolute_path) or '<root>'
        raise PureError(f"{'Response' if response else 'Input'} does not match {name} at {location} ({error.validator}).", 6 if response else 3)
