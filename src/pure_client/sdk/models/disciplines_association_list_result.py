from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disciplines_association import DisciplinesAssociation
    from ..models.page_information import PageInformation


T = TypeVar("T", bound="DisciplinesAssociationListResult")


@_attrs_define
class DisciplinesAssociationListResult:
    """List of discipline associations. Can contain a subset of all items along with the full count

    Attributes:
        count (int | Unset): The full count, ignoring paging
        page_information (PageInformation | Unset): Information about pages
        items (list[DisciplinesAssociation] | Unset): Discipline associations
    """

    count: int | Unset = UNSET
    page_information: PageInformation | Unset = UNSET
    items: list[DisciplinesAssociation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        page_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_information, Unset):
            page_information = self.page_information.to_dict()

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
        if page_information is not UNSET:
            field_dict["pageInformation"] = page_information
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.disciplines_association import DisciplinesAssociation
        from ..models.page_information import PageInformation

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _page_information = d.pop("pageInformation", UNSET)
        page_information: PageInformation | Unset
        if isinstance(_page_information, Unset):
            page_information = UNSET
        else:
            page_information = PageInformation.from_dict(_page_information)

        _items = d.pop("items", UNSET)
        items: list[DisciplinesAssociation] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = DisciplinesAssociation.from_dict(items_item_data)

                items.append(items_item)

        disciplines_association_list_result = cls(
            count=count,
            page_information=page_information,
            items=items,
        )

        disciplines_association_list_result.additional_properties = d
        return disciplines_association_list_result

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
