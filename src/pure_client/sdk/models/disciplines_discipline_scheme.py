from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DisciplinesDisciplineScheme")


@_attrs_define
class DisciplinesDisciplineScheme:
    """A discipline scheme

    Attributes:
        discipline_scheme (str): The discipline scheme identifier
        title (str): The discipline title
    """

    discipline_scheme: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discipline_scheme = self.discipline_scheme

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disciplineScheme": discipline_scheme,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        discipline_scheme = d.pop("disciplineScheme")

        title = d.pop("title")

        disciplines_discipline_scheme = cls(
            discipline_scheme=discipline_scheme,
            title=title,
        )

        disciplines_discipline_scheme.additional_properties = d
        return disciplines_discipline_scheme

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
