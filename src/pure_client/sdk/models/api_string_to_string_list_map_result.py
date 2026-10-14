from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_string_to_string_list_map_result_items import (
        APIStringToStringListMapResultItems,
    )


T = TypeVar("T", bound="APIStringToStringListMapResult")


@_attrs_define
class APIStringToStringListMapResult:
    """
    Attributes:
        items (APIStringToStringListMapResultItems | Unset):
        count (int | Unset):
    """

    items: APIStringToStringListMapResultItems | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_string_to_string_list_map_result_items import (
            APIStringToStringListMapResultItems,
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: APIStringToStringListMapResultItems | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = APIStringToStringListMapResultItems.from_dict(_items)

        count = d.pop("count", UNSET)

        api_string_to_string_list_map_result = cls(
            items=items,
            count=count,
        )

        api_string_to_string_list_map_result.additional_properties = d
        return api_string_to_string_list_map_result

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
