from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.compound_date_range import CompoundDateRange
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="ExternalAppointment")


@_attrs_define
class ExternalAppointment:
    """An appointment held in an external organizational unit

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        appointment (ClassificationRefType0 | None | Unset): A reference to a classification value
        appointment_string (LocalizedStringType0 | None | Unset): A set of string values, one for each submission
            locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        period (CompoundDateRange | Unset): A date range of that can be defined by only year, year and month or a full
            date
        external_organization (ExternalOrganizationRefType0 | None | Unset): A reference to an organization external to
            the institution
    """

    pure_id: int | Unset = UNSET
    appointment: ClassificationRefType0 | None | Unset = UNSET
    appointment_string: LocalizedStringType0 | None | Unset = UNSET
    period: CompoundDateRange | Unset = UNSET
    external_organization: ExternalOrganizationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        pure_id = self.pure_id

        appointment: dict[str, Any] | None | Unset
        if isinstance(self.appointment, Unset):
            appointment = UNSET
        elif isinstance(self.appointment, ClassificationRefType0):
            appointment = self.appointment.to_dict()
        else:
            appointment = self.appointment

        appointment_string: dict[str, Any] | None | Unset
        if isinstance(self.appointment_string, Unset):
            appointment_string = UNSET
        elif isinstance(self.appointment_string, LocalizedStringType0):
            appointment_string = self.appointment_string.to_dict()
        else:
            appointment_string = self.appointment_string

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        external_organization: dict[str, Any] | None | Unset
        if isinstance(self.external_organization, Unset):
            external_organization = UNSET
        elif isinstance(self.external_organization, ExternalOrganizationRefType0):
            external_organization = self.external_organization.to_dict()
        else:
            external_organization = self.external_organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if appointment is not UNSET:
            field_dict["appointment"] = appointment
        if appointment_string is not UNSET:
            field_dict["appointmentString"] = appointment_string
        if period is not UNSET:
            field_dict["period"] = period
        if external_organization is not UNSET:
            field_dict["externalOrganization"] = external_organization

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_range import CompoundDateRange
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_appointment(data: object) -> ClassificationRefType0 | None | Unset:
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

        appointment = _parse_appointment(d.pop("appointment", UNSET))

        def _parse_appointment_string(
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

        appointment_string = _parse_appointment_string(
            d.pop("appointmentString", UNSET)
        )

        _period = d.pop("period", UNSET)
        period: CompoundDateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = CompoundDateRange.from_dict(_period)

        def _parse_external_organization(
            data: object,
        ) -> ExternalOrganizationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_external_organization_ref_type_0 = (
                    ExternalOrganizationRefType0.from_dict(data)
                )

                return componentsschemas_external_organization_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalOrganizationRefType0 | None | Unset, data)

        external_organization = _parse_external_organization(
            d.pop("externalOrganization", UNSET)
        )

        external_appointment = cls(
            pure_id=pure_id,
            appointment=appointment,
            appointment_string=appointment_string,
            period=period,
            external_organization=external_organization,
        )

        external_appointment.additional_properties = d
        return external_appointment

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
