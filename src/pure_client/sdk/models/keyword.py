from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Keyword")


@_attrs_define
class Keyword:
    """List of free keywords

    Attributes:
        locale (str): Locale that user defined keywords are in
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        free_keywords (list[str] | Unset): User defined keywords in a specific locale
    """

    locale: str
    pure_id: int | Unset = UNSET
    free_keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        pure_id = self.pure_id

        free_keywords: list[str] | Unset = UNSET
        if not isinstance(self.free_keywords, Unset):
            free_keywords = self.free_keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if free_keywords is not UNSET:
            field_dict["freeKeywords"] = free_keywords

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        locale = d.pop("locale")

        pure_id = d.pop("pureId", UNSET)

        free_keywords = cast(list[str], d.pop("freeKeywords", UNSET))

        keyword = cls(
            locale=locale,
            pure_id=pure_id,
            free_keywords=free_keywords,
        )

        keyword.additional_properties = d
        return keyword

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
