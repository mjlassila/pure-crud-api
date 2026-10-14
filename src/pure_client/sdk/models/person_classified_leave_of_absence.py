from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.date_range import DateRange


T = TypeVar("T", bound="PersonClassifiedLeaveOfAbsence")


@_attrs_define
class PersonClassifiedLeaveOfAbsence:
    """Leave of absence held by a person

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        classification (ClassificationRefType0 | None | Unset): A reference to a classification value
        period (DateRange | Unset): A date range
    """

    pure_id: int | Unset = UNSET
    classification: ClassificationRefType0 | None | Unset = UNSET
    period: DateRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        pure_id = self.pure_id

        classification: dict[str, Any] | None | Unset
        if isinstance(self.classification, Unset):
            classification = UNSET
        elif isinstance(self.classification, ClassificationRefType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if classification is not UNSET:
            field_dict["classification"] = classification
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_classification(
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

        classification = _parse_classification(d.pop("classification", UNSET))

        _period = d.pop("period", UNSET)
        period: DateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = DateRange.from_dict(_period)

        person_classified_leave_of_absence = cls(
            pure_id=pure_id,
            classification=classification,
            period=period,
        )

        person_classified_leave_of_absence.additional_properties = d
        return person_classified_leave_of_absence

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
