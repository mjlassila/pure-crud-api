from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disciplines_discipline_scheme import DisciplinesDisciplineScheme


T = TypeVar("T", bound="DisciplinesDisciplineSchemeListResult")


@_attrs_define
class DisciplinesDisciplineSchemeListResult:
    """List of discipline schemes

    Attributes:
        count (int | Unset): The amount of discipline schemes
        items (list[DisciplinesDisciplineScheme] | Unset): Discipline schemes
    """

    count: int | Unset = UNSET
    items: list[DisciplinesDisciplineScheme] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.disciplines_discipline_scheme import DisciplinesDisciplineScheme

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _items = d.pop("items", UNSET)
        items: list[DisciplinesDisciplineScheme] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = DisciplinesDisciplineScheme.from_dict(items_item_data)

                items.append(items_item)

        disciplines_discipline_scheme_list_result = cls(
            count=count,
            items=items,
        )

        disciplines_discipline_scheme_list_result.additional_properties = d
        return disciplines_discipline_scheme_list_result

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
