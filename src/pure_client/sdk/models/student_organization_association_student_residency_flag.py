from enum import Enum


class StudentOrganizationAssociationStudentResidencyFlag(str, Enum):
    HOME = "HOME"
    OVERSEAS = "OVERSEAS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
