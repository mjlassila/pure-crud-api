from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisciplinesDiscipline")


@_attrs_define
class DisciplinesDiscipline:
    """A discipline within a specific discipline scheme

    Attributes:
        discipline_id (str | Unset): The discipline identifier
        title (str | Unset): The discipline title
        description (str | Unset): The discipline description
    """

    discipline_id: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discipline_id = self.discipline_id

        title = self.title

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discipline_id is not UNSET:
            field_dict["disciplineId"] = discipline_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        discipline_id = d.pop("disciplineId", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        disciplines_discipline = cls(
            discipline_id=discipline_id,
            title=title,
            description=description,
        )

        disciplines_discipline.additional_properties = d
        return disciplines_discipline

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
