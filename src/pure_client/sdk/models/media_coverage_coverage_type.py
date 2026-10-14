from enum import Enum


class MediaCoverageCoverageType(str, Enum):
    CONTRIBUTION = "CONTRIBUTION"
    COVERAGE = "COVERAGE"

    def __str__(self) -> str:
        return str(self.value)
