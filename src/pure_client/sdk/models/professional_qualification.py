from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compound_date_range import CompoundDateRange
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="ProfessionalQualification")


@_attrs_define
class ProfessionalQualification:
    """The professional qualifications held by a person

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        abbreviated_qualification (LocalizedStringType0 | None | Unset): A set of string values, one for each submission
            locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        period (CompoundDateRange | Unset): A date range of that can be defined by only year, year and month or a full
            date
        qualification (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
    """

    pure_id: int | Unset = UNSET
    abbreviated_qualification: LocalizedStringType0 | None | Unset = UNSET
    period: CompoundDateRange | Unset = UNSET
    qualification: LocalizedStringType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_string_type_0 import LocalizedStringType0

        pure_id = self.pure_id

        abbreviated_qualification: dict[str, Any] | None | Unset
        if isinstance(self.abbreviated_qualification, Unset):
            abbreviated_qualification = UNSET
        elif isinstance(self.abbreviated_qualification, LocalizedStringType0):
            abbreviated_qualification = self.abbreviated_qualification.to_dict()
        else:
            abbreviated_qualification = self.abbreviated_qualification

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        qualification: dict[str, Any] | None | Unset
        if isinstance(self.qualification, Unset):
            qualification = UNSET
        elif isinstance(self.qualification, LocalizedStringType0):
            qualification = self.qualification.to_dict()
        else:
            qualification = self.qualification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if abbreviated_qualification is not UNSET:
            field_dict["abbreviatedQualification"] = abbreviated_qualification
        if period is not UNSET:
            field_dict["period"] = period
        if qualification is not UNSET:
            field_dict["qualification"] = qualification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compound_date_range import CompoundDateRange
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_abbreviated_qualification(
            data: object,
        ) -> LocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(LocalizedStringType0 | None | Unset, data)

        abbreviated_qualification = _parse_abbreviated_qualification(
            d.pop("abbreviatedQualification", UNSET)
        )

        _period = d.pop("period", UNSET)
        period: CompoundDateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = CompoundDateRange.from_dict(_period)

        def _parse_qualification(data: object) -> LocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(LocalizedStringType0 | None | Unset, data)

        qualification = _parse_qualification(d.pop("qualification", UNSET))

        professional_qualification = cls(
            pure_id=pure_id,
            abbreviated_qualification=abbreviated_qualification,
            period=period,
            qualification=qualification,
        )

        professional_qualification.additional_properties = d
        return professional_qualification

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
