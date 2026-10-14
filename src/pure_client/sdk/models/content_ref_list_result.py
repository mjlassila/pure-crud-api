from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_ref_type_0 import ContentRefType0


T = TypeVar("T", bound="ContentRefListResult")


@_attrs_define
class ContentRefListResult:
    """List of Content Refs

    Attributes:
        items (list[ContentRefType0 | None] | Unset):
    """

    items: list[ContentRefType0 | None] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_ref_type_0 import ContentRefType0

        items: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item: dict[str, Any] | None
                if isinstance(items_item_data, ContentRefType0):
                    items_item = items_item_data.to_dict()
                else:
                    items_item = items_item_data
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.content_ref_type_0 import ContentRefType0

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[ContentRefType0 | None] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:

                def _parse_items_item(data: object) -> ContentRefType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_content_ref_type_0 = (
                            ContentRefType0.from_dict(data)
                        )

                        return componentsschemas_content_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(ContentRefType0 | None, data)

                items_item = _parse_items_item(items_item_data)

                items.append(items_item)

        content_ref_list_result = cls(
            items=items,
        )

        content_ref_list_result.additional_properties = d
        return content_ref_list_result

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
