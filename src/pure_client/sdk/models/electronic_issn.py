from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ElectronicISSN")


@_attrs_define
class ElectronicISSN:
    """Additional Electronic ISSN, is searchable but cannot be used when relating the journal to other content

    Attributes:
        issn (str): The actual ISSN value
        type_discriminator (str):
    """

    issn: str
    type_discriminator: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issn = self.issn

        type_discriminator = self.type_discriminator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issn": issn,
                "typeDiscriminator": type_discriminator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        issn = d.pop("issn")

        type_discriminator = d.pop("typeDiscriminator")

        electronic_issn = cls(
            issn=issn,
            type_discriminator=type_discriminator,
        )

        electronic_issn.additional_properties = d
        return electronic_issn

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
