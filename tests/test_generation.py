import importlib
import json
from pathlib import Path
import pkgutil
import yaml
from jsonschema import Draft202012Validator
from scripts.preprocess import preprocess, intersect
from scripts.generate import runtime_schema

ROOT = Path(__file__).resolve().parents[1]

def test_all_generated_modules_import_and_coverage_accounts_for_every_operation():
    import pure_client.sdk as sdk
    for module in pkgutil.walk_packages(sdk.__path__,sdk.__name__+'.'):
        importlib.import_module(module.name)
    spec = yaml.safe_load((ROOT/'spec/pure-api-openapi.yaml').read_text())
    expected = {v['operationId'] for p in spec['paths'].values() for m,v in p.items() if m in {'get','post','put','patch','delete','head','options','trace'}}
    coverage = json.loads((ROOT/'docs/coverage.json').read_text())
    assert len(coverage) == len(expected) == 970
    assert {r['operationId'] for r in coverage} == expected
    for row in coverage:
        if row['status'] == 'unsupported':
            operation = spec['paths'][row['path']][row['method'].lower()]
            assert '*/*' in operation['requestBody']['content']
        else:
            module = importlib.import_module(row['module'])
            assert callable(module.sync_detailed) and callable(module.asyncio_detailed)
    assert sum(r['status']=='generated' for r in coverage) == 928
    assert sum(r['status']=='partial' for r in coverage) == 21
    assert sum(r['status']=='unsupported' for r in coverage) == 21

def test_flatten_real_inheritance_preserves_fields_and_required_union():
    spec = yaml.safe_load((ROOT/'spec/pure-api-openapi.yaml').read_text())
    transformed = preprocess(spec)
    assert spec['info'] == transformed['info']
    assert spec['servers'] == transformed['servers']
    assert spec['paths'] == transformed['paths']
    assert spec['components']['securitySchemes'] == transformed['components']['securitySchemes']
    assert 'allOf' in spec['components']['schemas']['StaffOrganizationAssociation']
    result = transformed['components']['schemas']['StaffOrganizationAssociation']
    assert 'allOf' not in result
    assert 'organization' in result['properties'] and 'fte' in result['properties']
    assert 'typeDiscriminator' in result['required']
    # Dispatch remains on the parent, not on the concrete subclass.
    assert 'discriminator' in transformed['components']['schemas']['PersonOrganizationAssociation']
    assert 'discriminator' not in result
    visit = transformed['components']['schemas']['VisitOther']
    assert visit['properties']['persons']['nullable'] is False
    assert {'externalOrganizationRef','managingOrganization','period','type','visibility'} <= set(visit['required'])

def test_flatten_semantics_for_duplicate_nullable_array_and_required_fields():
    spec = {'components': {'schemas': {
        'Base': {'type':'object','required':['a'], 'properties': {'a': {'type':'string'}, 'items':{'type':'array','items':{'type':'string'}}}},
        'Sub': {'type':'object','required':['b'],'allOf':[{'$ref':'#/components/schemas/Base'}, {'type':'object','properties':{'b':{'type':'integer'},'items':{'type':'array','items':{'type':'string'},'nullable':True}}}]},
    }}}
    flat = preprocess(spec)
    for value in [{'a':'x','b':1,'items':[]}, {'a':'x','b':1,'items':None}, {'a':'x'}, {'b':1}, {'a':'x','b':'bad'}, {'a':'x','b':1,'items':['ok']}]:
        before = runtime_schema(spec)
        before['$ref'] = '#/components/schemas/Sub'
        after = runtime_schema(flat)
        after['$ref'] = '#/components/schemas/Sub'
        assert Draft202012Validator(before).is_valid(value) == Draft202012Validator(after).is_valid(value)

def test_unsupported_intersection_fails_explicitly():
    import pytest
    with pytest.raises(ValueError, match='safely intersect'):
        intersect({'type':'string'},{'type':'number'})

def test_polymorphic_and_nullable_representative_models():
    from pure_client.sdk.models.staff_organization_association import StaffOrganizationAssociation
    from pure_client.sdk.models.custom_defined_field_boolean_type_0 import CustomDefinedFieldBooleanType0
    payload = {'typeDiscriminator':'StaffOrganizationAssociation','fte':0.5,'organization':None}
    assert StaffOrganizationAssociation.from_dict(payload).to_dict() == payload
    data = {'typeDiscriminator':'Boolean','value':True}
    assert CustomDefinedFieldBooleanType0.from_dict(data).to_dict() == data
