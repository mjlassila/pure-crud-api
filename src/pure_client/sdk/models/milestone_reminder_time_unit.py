from enum import Enum


class MilestoneReminderTimeUnit(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"
    WEEK = "WEEK"

    def __str__(self) -> str:
        return str(self.value)
