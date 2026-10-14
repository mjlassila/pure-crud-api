"""Configuration shared by Python and CLI callers."""
from dataclasses import dataclass, field
import math
import os
from collections.abc import Mapping
from urllib.parse import urlsplit
from .errors import PureError

@dataclass(frozen=True)
class Settings:
    base_url: str
    api_key: str = field(repr=False)
    timeout: float = 30.0

    def __post_init__(self):
        try:
            url = urlsplit(self.base_url)
            valid = url.scheme in {'http', 'https'} and url.hostname and url.port != 0 and not any(ord(c) <= 32 for c in self.base_url)
        except (ValueError, TypeError):
            valid = False
            url = None
        if not valid or url.username or url.password or url.query or url.fragment:
            raise PureError('Set a full HTTP(S) PURE_API_BASE_URL without credentials, query, or fragment (for example https://pure.example.edu/ws/api).', 2)
        if not isinstance(self.api_key, str) or not self.api_key.strip() or any(ord(c) < 32 or ord(c) > 126 for c in self.api_key):
            raise PureError('Set a nonempty, valid PURE_API_KEY.', 2)
        if isinstance(self.timeout, bool) or not isinstance(self.timeout, (int, float)) or not math.isfinite(self.timeout) or self.timeout <= 0:
            raise PureError('Timeout must be a finite number greater than zero.', 2)
        object.__setattr__(self, 'base_url', self.base_url.rstrip('/'))

    @classmethod
    def from_env(cls, *, base_url: str | None = None, timeout: float = 30.0, environ: Mapping[str, str] | None = None):
        env = os.environ if environ is None else environ
        return cls(base_url=base_url if base_url is not None else env.get('PURE_API_BASE_URL', ''), api_key=env.get('PURE_API_KEY', ''), timeout=timeout)
