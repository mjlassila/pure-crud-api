from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.metric_definition import MetricDefinition


T = TypeVar("T", bound="MetricCollectionDefinition")


@_attrs_define
class MetricCollectionDefinition:
    """Information about a set of related metrics, usually from a single provider

    Attributes:
        collection_id (str): ID of the metric collection
        name (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        metrics (list[MetricDefinition] | Unset): Information about each metric in the collection
    """

    collection_id: str
    name: LocalizedStringType0 | None
    metrics: list[MetricDefinition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_string_type_0 import LocalizedStringType0

        collection_id = self.collection_id

        name: dict[str, Any] | None
        if isinstance(self.name, LocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionId": collection_id,
                "name": name,
            }
        )
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.metric_definition import MetricDefinition

        d = dict(src_dict)
        collection_id = d.pop("collectionId")

        def _parse_name(data: object) -> LocalizedStringType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_localized_string_type_0 = (
                    LocalizedStringType0.from_dict(data)
                )

                return componentsschemas_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedStringType0 | None, data)

        name = _parse_name(d.pop("name"))

        _metrics = d.pop("metrics", UNSET)
        metrics: list[MetricDefinition] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = MetricDefinition.from_dict(metrics_item_data)

                metrics.append(metrics_item)

        metric_collection_definition = cls(
            collection_id=collection_id,
            name=name,
            metrics=metrics,
        )

        metric_collection_definition.additional_properties = d
        return metric_collection_definition

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
