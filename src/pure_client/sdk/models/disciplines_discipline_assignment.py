from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DisciplinesDisciplineAssignment")


@_attrs_define
class DisciplinesDisciplineAssignment:
    """The assigned discipline and its split percentage

    Attributes:
        discipline_id (str): The assigned discipline
        split_percentage (float): The split percentages within an assigned discipline scheme must sum up to 100%
    """

    discipline_id: str
    split_percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discipline_id = self.discipline_id

        split_percentage = self.split_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disciplineId": discipline_id,
                "splitPercentage": split_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        discipline_id = d.pop("disciplineId")

        split_percentage = d.pop("splitPercentage")

        disciplines_discipline_assignment = cls(
            discipline_id=discipline_id,
            split_percentage=split_percentage,
        )

        disciplines_discipline_assignment.additional_properties = d
        return disciplines_discipline_assignment

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
