from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrimaryId")


@_attrs_define
class PrimaryId:
    """A primary external ID

    Attributes:
        type_discriminator (str):
        id_source (str): Name of the external source
        value (str): Primary external ID
        pure_id (int | Unset): Pure database ID of the object
    """

    type_discriminator: str
    id_source: str
    value: str
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_discriminator = self.type_discriminator

        id_source = self.id_source

        value = self.value

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "idSource": id_source,
                "value": value,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        id_source = d.pop("idSource")

        value = d.pop("value")

        pure_id = d.pop("pureId", UNSET)

        primary_id = cls(
            type_discriminator=type_discriminator,
            id_source=id_source,
            value=value,
            pure_id=pure_id,
        )

        primary_id.additional_properties = d
        return primary_id

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
