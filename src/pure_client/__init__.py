"""Elsevier Pure client; full generated interfaces live under pure_client.sdk."""
from .client import PureClient, load_query, load_person_uuids
from .config import Settings
from .errors import PureError

__all__ = ['PureClient', 'Settings', 'PureError', 'load_query', 'load_person_uuids']
