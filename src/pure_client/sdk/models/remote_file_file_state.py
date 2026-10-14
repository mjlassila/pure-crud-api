from enum import Enum


class RemoteFileFileState(str, Enum):
    AWAITING_CREATION = "AWAITING_CREATION"
    AWAITING_DELETE = "AWAITING_DELETE"
    CREATION_FAILED = "CREATION_FAILED"
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    DELETED = "DELETED"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    STORED = "STORED"

    def __str__(self) -> str:
        return str(self.value)
