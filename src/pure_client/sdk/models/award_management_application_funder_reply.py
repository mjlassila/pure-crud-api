from enum import Enum


class AwardManagementApplicationFunderReply(str, Enum):
    AWARDED = "AWARDED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
