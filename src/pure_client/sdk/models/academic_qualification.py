from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.compound_date_range import CompoundDateRange
    from ..models.internal_or_external_supervisor import InternalOrExternalSupervisor
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )


T = TypeVar("T", bound="AcademicQualification")


@_attrs_define
class AcademicQualification:
    """An object mapping the data of an education received by a person

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        award_date (datetime.date | None | Unset): Date that the education was awarded at.
        period (CompoundDateRange | Unset): A date range of that can be defined by only year, year and month or a full
            date
        field_of_study (ClassificationRefType0 | None | Unset): A reference to a classification value
        field_of_study_unstructured (LocalizedStringType0 | None | Unset): A set of string values, one for each
            submission locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        organization (None | OrganizationOrExternalOrganizationRefType0 | Unset): A reference to an organization in the
            institution or an external organization
        project_title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        qualification (ClassificationRefType0 | None | Unset): A reference to a classification value
        qualification_unstructured (LocalizedStringType0 | None | Unset): A set of string values, one for each
            submission locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        distinction (ClassificationRefType0 | None | Unset): A reference to a classification value
        supervisor (InternalOrExternalSupervisor | Unset): A supervisor, either internal or external, use as mutually
            exclusive
    """

    pure_id: int | Unset = UNSET
    award_date: datetime.date | None | Unset = UNSET
    period: CompoundDateRange | Unset = UNSET
    field_of_study: ClassificationRefType0 | None | Unset = UNSET
    field_of_study_unstructured: LocalizedStringType0 | None | Unset = UNSET
    organization: None | OrganizationOrExternalOrganizationRefType0 | Unset = UNSET
    project_title: LocalizedStringType0 | None | Unset = UNSET
    qualification: ClassificationRefType0 | None | Unset = UNSET
    qualification_unstructured: LocalizedStringType0 | None | Unset = UNSET
    distinction: ClassificationRefType0 | None | Unset = UNSET
    supervisor: InternalOrExternalSupervisor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

        pure_id = self.pure_id

        award_date: None | str | Unset
        if isinstance(self.award_date, Unset):
            award_date = UNSET
        elif isinstance(self.award_date, datetime.date):
            award_date = self.award_date.isoformat()
        else:
            award_date = self.award_date

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        field_of_study: dict[str, Any] | None | Unset
        if isinstance(self.field_of_study, Unset):
            field_of_study = UNSET
        elif isinstance(self.field_of_study, ClassificationRefType0):
            field_of_study = self.field_of_study.to_dict()
        else:
            field_of_study = self.field_of_study

        field_of_study_unstructured: dict[str, Any] | None | Unset
        if isinstance(self.field_of_study_unstructured, Unset):
            field_of_study_unstructured = UNSET
        elif isinstance(self.field_of_study_unstructured, LocalizedStringType0):
            field_of_study_unstructured = self.field_of_study_unstructured.to_dict()
        else:
            field_of_study_unstructured = self.field_of_study_unstructured

        organization: dict[str, Any] | None | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, OrganizationOrExternalOrganizationRefType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        project_title: dict[str, Any] | None | Unset
        if isinstance(self.project_title, Unset):
            project_title = UNSET
        elif isinstance(self.project_title, LocalizedStringType0):
            project_title = self.project_title.to_dict()
        else:
            project_title = self.project_title

        qualification: dict[str, Any] | None | Unset
        if isinstance(self.qualification, Unset):
            qualification = UNSET
        elif isinstance(self.qualification, ClassificationRefType0):
            qualification = self.qualification.to_dict()
        else:
            qualification = self.qualification

        qualification_unstructured: dict[str, Any] | None | Unset
        if isinstance(self.qualification_unstructured, Unset):
            qualification_unstructured = UNSET
        elif isinstance(self.qualification_unstructured, LocalizedStringType0):
            qualification_unstructured = self.qualification_unstructured.to_dict()
        else:
            qualification_unstructured = self.qualification_unstructured

        distinction: dict[str, Any] | None | Unset
        if isinstance(self.distinction, Unset):
            distinction = UNSET
        elif isinstance(self.distinction, ClassificationRefType0):
            distinction = self.distinction.to_dict()
        else:
            distinction = self.distinction

        supervisor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supervisor, Unset):
            supervisor = self.supervisor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if award_date is not UNSET:
            field_dict["awardDate"] = award_date
        if period is not UNSET:
            field_dict["period"] = period
        if field_of_study is not UNSET:
            field_dict["fieldOfStudy"] = field_of_study
        if field_of_study_unstructured is not UNSET:
            field_dict["fieldOfStudyUnstructured"] = field_of_study_unstructured
        if organization is not UNSET:
            field_dict["organization"] = organization
        if project_title is not UNSET:
            field_dict["projectTitle"] = project_title
        if qualification is not UNSET:
            field_dict["qualification"] = qualification
        if qualification_unstructured is not UNSET:
            field_dict["qualificationUnstructured"] = qualification_unstructured
        if distinction is not UNSET:
            field_dict["distinction"] = distinction
        if supervisor is not UNSET:
            field_dict["supervisor"] = supervisor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_range import CompoundDateRange
        from ..models.internal_or_external_supervisor import (
            InternalOrExternalSupervisor,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_award_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                award_date_type_0 = isoparse(data).date()

                return award_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        award_date = _parse_award_date(d.pop("awardDate", UNSET))

        _period = d.pop("period", UNSET)
        period: CompoundDateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = CompoundDateRange.from_dict(_period)

        def _parse_field_of_study(
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

        field_of_study = _parse_field_of_study(d.pop("fieldOfStudy", UNSET))

        def _parse_field_of_study_unstructured(
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

        field_of_study_unstructured = _parse_field_of_study_unstructured(
            d.pop("fieldOfStudyUnstructured", UNSET)
        )

        def _parse_organization(
            data: object,
        ) -> None | OrganizationOrExternalOrganizationRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_or_external_organization_ref_type_0 = (
                    OrganizationOrExternalOrganizationRefType0.from_dict(data)
                )

                return (
                    componentsschemas_organization_or_external_organization_ref_type_0
                )
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationOrExternalOrganizationRefType0 | Unset, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_project_title(data: object) -> LocalizedStringType0 | None | Unset:
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

        project_title = _parse_project_title(d.pop("projectTitle", UNSET))

        def _parse_qualification(data: object) -> ClassificationRefType0 | None | Unset:
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

        qualification = _parse_qualification(d.pop("qualification", UNSET))

        def _parse_qualification_unstructured(
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

        qualification_unstructured = _parse_qualification_unstructured(
            d.pop("qualificationUnstructured", UNSET)
        )

        def _parse_distinction(data: object) -> ClassificationRefType0 | None | Unset:
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

        distinction = _parse_distinction(d.pop("distinction", UNSET))

        _supervisor = d.pop("supervisor", UNSET)
        supervisor: InternalOrExternalSupervisor | Unset
        if isinstance(_supervisor, Unset):
            supervisor = UNSET
        else:
            supervisor = InternalOrExternalSupervisor.from_dict(_supervisor)

        academic_qualification = cls(
            pure_id=pure_id,
            award_date=award_date,
            period=period,
            field_of_study=field_of_study,
            field_of_study_unstructured=field_of_study_unstructured,
            organization=organization,
            project_title=project_title,
            qualification=qualification,
            qualification_unstructured=qualification_unstructured,
            distinction=distinction,
            supervisor=supervisor,
        )

        academic_qualification.additional_properties = d
        return academic_qualification

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
