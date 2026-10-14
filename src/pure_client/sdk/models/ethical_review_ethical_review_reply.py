from enum import Enum


class EthicalReviewEthicalReviewReply(str, Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"
    EXTENDED = "EXTENDED"
    PENDING = "PENDING"
    WITHDRAWN = "WITHDRAWN"

    def __str__(self) -> str:
        return str(self.value)
