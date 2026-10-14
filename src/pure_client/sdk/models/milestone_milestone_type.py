from enum import Enum


class MilestoneMilestoneType(str, Enum):
    ACADEMIC = "ACADEMIC"
    ADMINISTRATIVE = "ADMINISTRATIVE"

    def __str__(self) -> str:
        return str(self.value)
