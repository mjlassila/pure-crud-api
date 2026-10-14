from enum import Enum


class VisibilityKey(str, Enum):
    BACKEND = "BACKEND"
    CAMPUS = "CAMPUS"
    CONFIDENTIAL = "CONFIDENTIAL"
    FREE = "FREE"

    def __str__(self) -> str:
        return str(self.value)
