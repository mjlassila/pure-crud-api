from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MilestoneQuery")


@_attrs_define
class MilestoneQuery:
    """Create a query for milestone

    Attributes:
        size (int | Unset):
        offset (int | Unset):
        orderings (list[str] | Unset):
        uuids (list[UUID] | Unset):
        search_string (str | Unset): String used to perform search
        related_content_system_name (str | Unset): The related content system name to perform search
        related_content_uuid (str | Unset): The related content uuid to perform search
        order_by (str | Unset):
    """

    size: int | Unset = UNSET
    offset: int | Unset = UNSET
    orderings: list[str] | Unset = UNSET
    uuids: list[UUID] | Unset = UNSET
    search_string: str | Unset = UNSET
    related_content_system_name: str | Unset = UNSET
    related_content_uuid: str | Unset = UNSET
    order_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        offset = self.offset

        orderings: list[str] | Unset = UNSET
        if not isinstance(self.orderings, Unset):
            orderings = self.orderings

        uuids: list[str] | Unset = UNSET
        if not isinstance(self.uuids, Unset):
            uuids = []
            for uuids_item_data in self.uuids:
                uuids_item = str(uuids_item_data)
                uuids.append(uuids_item)

        search_string = self.search_string

        related_content_system_name = self.related_content_system_name

        related_content_uuid = self.related_content_uuid

        order_by = self.order_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if offset is not UNSET:
            field_dict["offset"] = offset
        if orderings is not UNSET:
            field_dict["orderings"] = orderings
        if uuids is not UNSET:
            field_dict["uuids"] = uuids
        if search_string is not UNSET:
            field_dict["searchString"] = search_string
        if related_content_system_name is not UNSET:
            field_dict["relatedContentSystemName"] = related_content_system_name
        if related_content_uuid is not UNSET:
            field_dict["relatedContentUuid"] = related_content_uuid
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        size = d.pop("size", UNSET)

        offset = d.pop("offset", UNSET)

        orderings = cast(list[str], d.pop("orderings", UNSET))

        _uuids = d.pop("uuids", UNSET)
        uuids: list[UUID] | Unset = UNSET
        if _uuids is not UNSET:
            uuids = []
            for uuids_item_data in _uuids:
                uuids_item = UUID(uuids_item_data)

                uuids.append(uuids_item)

        search_string = d.pop("searchString", UNSET)

        related_content_system_name = d.pop("relatedContentSystemName", UNSET)

        related_content_uuid = d.pop("relatedContentUuid", UNSET)

        order_by = d.pop("orderBy", UNSET)

        milestone_query = cls(
            size=size,
            offset=offset,
            orderings=orderings,
            uuids=uuids,
            search_string=search_string,
            related_content_system_name=related_content_system_name,
            related_content_uuid=related_content_uuid,
            order_by=order_by,
        )

        milestone_query.additional_properties = d
        return milestone_query

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
