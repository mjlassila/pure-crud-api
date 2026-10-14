from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_ref_type_0 import ContentRefType0
    from ..models.metric_collection_item import MetricCollectionItem


T = TypeVar("T", bound="MetricCollection")


@_attrs_define
class MetricCollection:
    """List of metrics

    Attributes:
        collection_id (str): Collection ID is the unique id of the provider for the metrics. A collection of metrics is
            a list of metrics that have a shared data structure and provider.
        owner (ContentRefType0 | None | Unset):
        items (list[MetricCollectionItem] | Unset): Metric collection items
    """

    collection_id: str
    owner: ContentRefType0 | None | Unset = UNSET
    items: list[MetricCollectionItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_ref_type_0 import ContentRefType0

        collection_id = self.collection_id

        owner: dict[str, Any] | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        elif isinstance(self.owner, ContentRefType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionId": collection_id,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.content_ref_type_0 import ContentRefType0
        from ..models.metric_collection_item import MetricCollectionItem

        d = dict(src_dict)
        collection_id = d.pop("collectionId")

        def _parse_owner(data: object) -> ContentRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_ref_type_0 = ContentRefType0.from_dict(data)

                return componentsschemas_content_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContentRefType0 | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        _items = d.pop("items", UNSET)
        items: list[MetricCollectionItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = MetricCollectionItem.from_dict(items_item_data)

                items.append(items_item)

        metric_collection = cls(
            collection_id=collection_id,
            owner=owner,
            items=items,
        )

        metric_collection.additional_properties = d
        return metric_collection

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
