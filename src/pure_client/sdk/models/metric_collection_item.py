from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.metric_value import MetricValue


T = TypeVar("T", bound="MetricCollectionItem")


@_attrs_define
class MetricCollectionItem:
    """A metric collection. Contents a list of metric values.

    Attributes:
        metric_values (list[MetricValue]): List of metric values.
        source (ClassificationRefType0 | None | Unset): A reference to a classification value
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        year (int | None | Unset): The year of the metric, if applicable.
    """

    metric_values: list[MetricValue]
    source: ClassificationRefType0 | None | Unset = UNSET
    category: ClassificationRefType0 | None | Unset = UNSET
    year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        metric_values = []
        for metric_values_item_data in self.metric_values:
            metric_values_item = metric_values_item_data.to_dict()
            metric_values.append(metric_values_item)

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, ClassificationRefType0):
            source = self.source.to_dict()
        else:
            source = self.source

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricValues": metric_values,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if category is not UNSET:
            field_dict["category"] = category
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.metric_value import MetricValue

        d = dict(src_dict)
        metric_values = []
        _metric_values = d.pop("metricValues")
        for metric_values_item_data in _metric_values:
            metric_values_item = MetricValue.from_dict(metric_values_item_data)

            metric_values.append(metric_values_item)

        def _parse_source(data: object) -> ClassificationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_classification_ref_type_0 = (
                    ClassificationRefType0.from_dict(data)
                )

                return componentsschemas_classification_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClassificationRefType0 | None | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_category(data: object) -> ClassificationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_classification_ref_type_0 = (
                    ClassificationRefType0.from_dict(data)
                )

                return componentsschemas_classification_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClassificationRefType0 | None | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        metric_collection_item = cls(
            metric_values=metric_values,
            source=source,
            category=category,
            year=year,
        )

        metric_collection_item.additional_properties = d
        return metric_collection_item

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
