from enum import Enum


class ArticleVersionKey(str, Enum):
    ACCEPTED = "ACCEPTED"
    PUBLISHED = "PUBLISHED"
    SUBMITTED = "SUBMITTED"

    def __str__(self) -> str:
        return str(self.value)
