from enum import Enum


class FundingOpportunityEligibilityEligibilityFulfilmentType(str, Enum):
    RECOMMENDATION = "RECOMMENDATION"
    REQUIREMENT = "REQUIREMENT"

    def __str__(self) -> str:
        return str(self.value)
