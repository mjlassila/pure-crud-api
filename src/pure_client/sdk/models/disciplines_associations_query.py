from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisciplinesAssociationsQuery")


@_attrs_define
class DisciplinesAssociationsQuery:
    """Create a query for discipline associations

    Attributes:
        uuids (list[UUID] | Unset):
        size (int | Unset):
        offset (int | Unset):
    """

    uuids: list[UUID] | Unset = UNSET
    size: int | Unset = UNSET
    offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuids: list[str] | Unset = UNSET
        if not isinstance(self.uuids, Unset):
            uuids = []
            for uuids_item_data in self.uuids:
                uuids_item = str(uuids_item_data)
                uuids.append(uuids_item)

        size = self.size

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuids is not UNSET:
            field_dict["uuids"] = uuids
        if size is not UNSET:
            field_dict["size"] = size
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _uuids = d.pop("uuids", UNSET)
        uuids: list[UUID] | Unset = UNSET
        if _uuids is not UNSET:
            uuids = []
            for uuids_item_data in _uuids:
                uuids_item = UUID(uuids_item_data)

                uuids.append(uuids_item)

        size = d.pop("size", UNSET)

        offset = d.pop("offset", UNSET)

        disciplines_associations_query = cls(
            uuids=uuids,
            size=size,
            offset=offset,
        )

        disciplines_associations_query.additional_properties = d
        return disciplines_associations_query

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
