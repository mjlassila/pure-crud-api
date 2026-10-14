from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="MetricValue")


@_attrs_define
class MetricValue:
    """A metric value, that contains one piece of data. Only one type of value can be set at a time, and it must match the
    specification of the metric definition.

        Attributes:
            metric_id (str): ID of the metric that defines this metric value (this controls for example the type returned).
            integer_value (int | None | Unset): The integer value of the metric.
            decimal_value (float | None | Unset): The decimal value of the metric.
            string_value (None | str | Unset): The string value of the metric.
            boolean_value (bool | None | Unset): The boolean value of the metric.
            classification_value (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    metric_id: str
    integer_value: int | None | Unset = UNSET
    decimal_value: float | None | Unset = UNSET
    string_value: None | str | Unset = UNSET
    boolean_value: bool | None | Unset = UNSET
    classification_value: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        metric_id = self.metric_id

        integer_value: int | None | Unset
        if isinstance(self.integer_value, Unset):
            integer_value = UNSET
        else:
            integer_value = self.integer_value

        decimal_value: float | None | Unset
        if isinstance(self.decimal_value, Unset):
            decimal_value = UNSET
        else:
            decimal_value = self.decimal_value

        string_value: None | str | Unset
        if isinstance(self.string_value, Unset):
            string_value = UNSET
        else:
            string_value = self.string_value

        boolean_value: bool | None | Unset
        if isinstance(self.boolean_value, Unset):
            boolean_value = UNSET
        else:
            boolean_value = self.boolean_value

        classification_value: dict[str, Any] | None | Unset
        if isinstance(self.classification_value, Unset):
            classification_value = UNSET
        elif isinstance(self.classification_value, ClassificationRefType0):
            classification_value = self.classification_value.to_dict()
        else:
            classification_value = self.classification_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricId": metric_id,
            }
        )
        if integer_value is not UNSET:
            field_dict["integerValue"] = integer_value
        if decimal_value is not UNSET:
            field_dict["decimalValue"] = decimal_value
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if boolean_value is not UNSET:
            field_dict["booleanValue"] = boolean_value
        if classification_value is not UNSET:
            field_dict["classificationValue"] = classification_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)
        metric_id = d.pop("metricId")

        def _parse_integer_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        integer_value = _parse_integer_value(d.pop("integerValue", UNSET))

        def _parse_decimal_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        decimal_value = _parse_decimal_value(d.pop("decimalValue", UNSET))

        def _parse_string_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        string_value = _parse_string_value(d.pop("stringValue", UNSET))

        def _parse_boolean_value(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        boolean_value = _parse_boolean_value(d.pop("booleanValue", UNSET))

        def _parse_classification_value(
            data: object,
        ) -> ClassificationRefType0 | None | Unset:
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

        classification_value = _parse_classification_value(
            d.pop("classificationValue", UNSET)
        )

        metric_value = cls(
            metric_id=metric_id,
            integer_value=integer_value,
            decimal_value=decimal_value,
            string_value=string_value,
            boolean_value=boolean_value,
            classification_value=classification_value,
        )

        metric_value.additional_properties = d
        return metric_value

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
