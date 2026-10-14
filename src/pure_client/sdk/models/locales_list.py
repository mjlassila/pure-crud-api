from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalesList")


@_attrs_define
class LocalesList:
    """List of available locales

    Attributes:
        locales (list[str] | Unset): Allowed locale values for use in localized string entities. The locale format
            consists of lower-case ISO 639 alpha-2 language code and upper-cased ISO 3166 alpha-2 country code.
    """

    locales: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locales: list[str] | Unset = UNSET
        if not isinstance(self.locales, Unset):
            locales = self.locales

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locales is not UNSET:
            field_dict["locales"] = locales

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        locales = cast(list[str], d.pop("locales", UNSET))

        locales_list = cls(
            locales=locales,
        )

        locales_list.additional_properties = d
        return locales_list

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
