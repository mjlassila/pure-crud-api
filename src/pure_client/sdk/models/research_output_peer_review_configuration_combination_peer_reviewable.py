from enum import Enum


class ResearchOutputPeerReviewConfigurationCombinationPeerReviewable(str, Enum):
    INTERNATIONAL_PEER_REVIEWABLE = "INTERNATIONAL_PEER_REVIEWABLE"
    NOT_PEER_REVIEWABLE = "NOT_PEER_REVIEWABLE"
    PEER_REVIEWABLE = "PEER_REVIEWABLE"

    def __str__(self) -> str:
        return str(self.value)
