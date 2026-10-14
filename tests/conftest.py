from copy import deepcopy
import pytest
import httpx
from pure_client import PureClient, Settings

UUID = '11111111-1111-4111-8111-111111111111'

@pytest.fixture
def record():
    def make(resource, uuid=UUID):
        if resource == 'persons':
            return {'uuid': uuid, 'name': {'firstName': 'Ada', 'lastName': 'Lovelace'}, 'customExtra': {'kept': True}}
        if resource == 'fingerprints':
            return {'uuid': uuid, 'relatedContent': {'uuid': UUID, 'systemName': 'Person'}, 'concepts': [{'concept': {'uuid': UUID, 'systemName': 'Concept'}, 'rank': 0.75, 'weightedRank': 0.6}]}
        if resource == 'concepts':
            return {'uuid': uuid, 'conceptId': 'C001', 'thesaurus': {'uuid': UUID, 'systemName': 'Thesaurus'}, 'name': {'en_GB': 'Artificial intelligence'}}
        if resource == 'organizations':
            return {'uuid': uuid, 'name': {'en_GB': 'Example University'}, 'lifecycle': {}, 'type': {'uri': '/organization/types/university'}}
        return {'uuid': uuid, 'title': {'value': 'Example output'}, 'type': {'uri': '/researchoutput/types/contributiontojournal/article'}, 'category': {'uri': '/researchoutput/categories/research'}, 'language': {'uri': '/languages/en'}, 'managingOrganization': {'systemName': 'Organization', 'uuid': UUID}, 'publicationStatuses': [], 'contributors': [], 'typeDiscriminator': 'ContributionToJournal'}
    return make

@pytest.fixture
def client_factory():
    clients = []
    def make(handler):
        client = PureClient(Settings('https://pure.example.edu/ws/api/', 'private-test-key'), transport=httpx.MockTransport(handler))
        clients.append(client)
        return client
    yield make
    for client in clients:
        client.sdk.get_httpx_client().close()
