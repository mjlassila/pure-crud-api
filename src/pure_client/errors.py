"""Stable public errors and CLI exit codes."""
class PureError(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code
