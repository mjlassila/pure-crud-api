from enum import Enum


class KeywordGroupConfigurationUserdefinedKeywordEditMode(str, Enum):
    ALL_SUPPORTED_LOCALES = "ALL_SUPPORTED_LOCALES"
    ALL_SUPPORTED_SUBMISSION_LOCALES = "ALL_SUPPORTED_SUBMISSION_LOCALES"
    SUBMISSION_LOCALE = "SUBMISSION_LOCALE"

    def __str__(self) -> str:
        return str(self.value)
