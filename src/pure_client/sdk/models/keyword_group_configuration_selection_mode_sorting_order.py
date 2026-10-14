from enum import Enum


class KeywordGroupConfigurationSelectionModeSortingOrder(str, Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"
    SCHEMA_INDEX = "SCHEMA_INDEX"

    def __str__(self) -> str:
        return str(self.value)
