from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.student_organization_association_student_residency_flag import (
    StudentOrganizationAssociationStudentResidencyFlag,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_address import ClassifiedAddress
    from ..models.classified_localized_value import ClassifiedLocalizedValue
    from ..models.classified_value import ClassifiedValue
    from ..models.date_range import DateRange
    from ..models.keyword_group import KeywordGroup
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.person_supervisor_association import PersonSupervisorAssociation


T = TypeVar("T", bound="StudentOrganizationAssociation")


@_attrs_define
class StudentOrganizationAssociation:
    """A relation describing the association between student and organization

    Attributes:
        type_discriminator (str):
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        addresses (list[ClassifiedAddress] | None | Unset): List of physical addresses.
        affiliation_id (None | str | Unset): Affiliation identification. This could be a student ID or a staff ID.
        employment_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        organization (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
        emails (list[ClassifiedValue] | None | Unset): List of emails.
        web_addresses (list[ClassifiedLocalizedValue] | None | Unset): List of web addresses.
        phone_numbers (list[ClassifiedValue] | None | Unset): Phone numbers associated with the organization
            association.
        period (DateRange | Unset): A date range
        supervisor_associations (list[PersonSupervisorAssociation] | None | Unset): List of associations to persons who
            supervise this person.
        keyword_groups (list[KeywordGroup] | None | Unset): List of keyword groups.
        primary_association (bool | Unset): A boolean value indicating whether this is the primary association or not.
            Only one of the associations from a person to an organization will be primary.
        award_date (datetime.date | None | Unset): The date when the student received an award.
        award_gained (None | str | Unset): Description of what award the student gained.
        fte (float | None | Unset): The FTE (Full-Time Equivalent). A decimal number ranging between 0 (0% equivalent of
            full time) and 1 (100% equivalent of full time).
        programme (None | str | Unset): The name or title of a program often consists of the degree (e.g., BS) and the
            discipline or field of study (e.g., Business Administration).
        project_title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        expected_study_duration (int | None | Unset): The expected study duration.
        minimum_study_duration (int | None | Unset): The minimum study duration.
        maximum_study_duration (int | None | Unset): The maximum study duration.
        program_year (None | str | Unset): The program year
        initial_submission_date (datetime.date | None | Unset): The program year
        get_expected_end_date (datetime.date | None | Unset): Expected end date
        start_year (None | str | Unset): Start year
        attendance_status (ClassificationRefType0 | None | Unset): A reference to a classification value
        get_student_nationality (ClassificationRefType0 | None | Unset): A reference to a classification value
        student_residency_flag (StudentOrganizationAssociationStudentResidencyFlag | Unset): Residency flag of the
            student, indicating whether the student is a home student or an overseas student.
        get_student_country_of_domicile (ClassificationRefType0 | None | Unset): A reference to a classification value
        student_type_description (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    type_discriminator: str
    pure_id: int | Unset = UNSET
    addresses: list[ClassifiedAddress] | None | Unset = UNSET
    affiliation_id: None | str | Unset = UNSET
    employment_type: ClassificationRefType0 | None | Unset = UNSET
    organization: None | OrganizationRefType0 | Unset = UNSET
    emails: list[ClassifiedValue] | None | Unset = UNSET
    web_addresses: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    phone_numbers: list[ClassifiedValue] | None | Unset = UNSET
    period: DateRange | Unset = UNSET
    supervisor_associations: list[PersonSupervisorAssociation] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    primary_association: bool | Unset = UNSET
    award_date: datetime.date | None | Unset = UNSET
    award_gained: None | str | Unset = UNSET
    fte: float | None | Unset = UNSET
    programme: None | str | Unset = UNSET
    project_title: LocalizedStringType0 | None | Unset = UNSET
    expected_study_duration: int | None | Unset = UNSET
    minimum_study_duration: int | None | Unset = UNSET
    maximum_study_duration: int | None | Unset = UNSET
    program_year: None | str | Unset = UNSET
    initial_submission_date: datetime.date | None | Unset = UNSET
    get_expected_end_date: datetime.date | None | Unset = UNSET
    start_year: None | str | Unset = UNSET
    attendance_status: ClassificationRefType0 | None | Unset = UNSET
    get_student_nationality: ClassificationRefType0 | None | Unset = UNSET
    student_residency_flag: (
        StudentOrganizationAssociationStudentResidencyFlag | Unset
    ) = UNSET
    get_student_country_of_domicile: ClassificationRefType0 | None | Unset = UNSET
    student_type_description: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0

        type_discriminator = self.type_discriminator

        pure_id = self.pure_id

        addresses: list[dict[str, Any]] | None | Unset
        if isinstance(self.addresses, Unset):
            addresses = UNSET
        elif isinstance(self.addresses, list):
            addresses = []
            for addresses_type_0_item_data in self.addresses:
                addresses_type_0_item = addresses_type_0_item_data.to_dict()
                addresses.append(addresses_type_0_item)

        else:
            addresses = self.addresses

        affiliation_id: None | str | Unset
        if isinstance(self.affiliation_id, Unset):
            affiliation_id = UNSET
        else:
            affiliation_id = self.affiliation_id

        employment_type: dict[str, Any] | None | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        elif isinstance(self.employment_type, ClassificationRefType0):
            employment_type = self.employment_type.to_dict()
        else:
            employment_type = self.employment_type

        organization: dict[str, Any] | None | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, OrganizationRefType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        emails: list[dict[str, Any]] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = []
            for emails_type_0_item_data in self.emails:
                emails_type_0_item = emails_type_0_item_data.to_dict()
                emails.append(emails_type_0_item)

        else:
            emails = self.emails

        web_addresses: list[dict[str, Any]] | None | Unset
        if isinstance(self.web_addresses, Unset):
            web_addresses = UNSET
        elif isinstance(self.web_addresses, list):
            web_addresses = []
            for web_addresses_type_0_item_data in self.web_addresses:
                web_addresses_type_0_item = web_addresses_type_0_item_data.to_dict()
                web_addresses.append(web_addresses_type_0_item)

        else:
            web_addresses = self.web_addresses

        phone_numbers: list[dict[str, Any]] | None | Unset
        if isinstance(self.phone_numbers, Unset):
            phone_numbers = UNSET
        elif isinstance(self.phone_numbers, list):
            phone_numbers = []
            for phone_numbers_type_0_item_data in self.phone_numbers:
                phone_numbers_type_0_item = phone_numbers_type_0_item_data.to_dict()
                phone_numbers.append(phone_numbers_type_0_item)

        else:
            phone_numbers = self.phone_numbers

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        supervisor_associations: list[dict[str, Any]] | None | Unset
        if isinstance(self.supervisor_associations, Unset):
            supervisor_associations = UNSET
        elif isinstance(self.supervisor_associations, list):
            supervisor_associations = []
            for (
                supervisor_associations_type_0_item_data
            ) in self.supervisor_associations:
                supervisor_associations_type_0_item = (
                    supervisor_associations_type_0_item_data.to_dict()
                )
                supervisor_associations.append(supervisor_associations_type_0_item)

        else:
            supervisor_associations = self.supervisor_associations

        keyword_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyword_groups, Unset):
            keyword_groups = UNSET
        elif isinstance(self.keyword_groups, list):
            keyword_groups = []
            for keyword_groups_type_0_item_data in self.keyword_groups:
                keyword_groups_type_0_item = keyword_groups_type_0_item_data.to_dict()
                keyword_groups.append(keyword_groups_type_0_item)

        else:
            keyword_groups = self.keyword_groups

        primary_association = self.primary_association

        award_date: None | str | Unset
        if isinstance(self.award_date, Unset):
            award_date = UNSET
        elif isinstance(self.award_date, datetime.date):
            award_date = self.award_date.isoformat()
        else:
            award_date = self.award_date

        award_gained: None | str | Unset
        if isinstance(self.award_gained, Unset):
            award_gained = UNSET
        else:
            award_gained = self.award_gained

        fte: float | None | Unset
        if isinstance(self.fte, Unset):
            fte = UNSET
        else:
            fte = self.fte

        programme: None | str | Unset
        if isinstance(self.programme, Unset):
            programme = UNSET
        else:
            programme = self.programme

        project_title: dict[str, Any] | None | Unset
        if isinstance(self.project_title, Unset):
            project_title = UNSET
        elif isinstance(self.project_title, LocalizedStringType0):
            project_title = self.project_title.to_dict()
        else:
            project_title = self.project_title

        expected_study_duration: int | None | Unset
        if isinstance(self.expected_study_duration, Unset):
            expected_study_duration = UNSET
        else:
            expected_study_duration = self.expected_study_duration

        minimum_study_duration: int | None | Unset
        if isinstance(self.minimum_study_duration, Unset):
            minimum_study_duration = UNSET
        else:
            minimum_study_duration = self.minimum_study_duration

        maximum_study_duration: int | None | Unset
        if isinstance(self.maximum_study_duration, Unset):
            maximum_study_duration = UNSET
        else:
            maximum_study_duration = self.maximum_study_duration

        program_year: None | str | Unset
        if isinstance(self.program_year, Unset):
            program_year = UNSET
        else:
            program_year = self.program_year

        initial_submission_date: None | str | Unset
        if isinstance(self.initial_submission_date, Unset):
            initial_submission_date = UNSET
        elif isinstance(self.initial_submission_date, datetime.date):
            initial_submission_date = self.initial_submission_date.isoformat()
        else:
            initial_submission_date = self.initial_submission_date

        get_expected_end_date: None | str | Unset
        if isinstance(self.get_expected_end_date, Unset):
            get_expected_end_date = UNSET
        elif isinstance(self.get_expected_end_date, datetime.date):
            get_expected_end_date = self.get_expected_end_date.isoformat()
        else:
            get_expected_end_date = self.get_expected_end_date

        start_year: None | str | Unset
        if isinstance(self.start_year, Unset):
            start_year = UNSET
        else:
            start_year = self.start_year

        attendance_status: dict[str, Any] | None | Unset
        if isinstance(self.attendance_status, Unset):
            attendance_status = UNSET
        elif isinstance(self.attendance_status, ClassificationRefType0):
            attendance_status = self.attendance_status.to_dict()
        else:
            attendance_status = self.attendance_status

        get_student_nationality: dict[str, Any] | None | Unset
        if isinstance(self.get_student_nationality, Unset):
            get_student_nationality = UNSET
        elif isinstance(self.get_student_nationality, ClassificationRefType0):
            get_student_nationality = self.get_student_nationality.to_dict()
        else:
            get_student_nationality = self.get_student_nationality

        student_residency_flag: str | Unset = UNSET
        if not isinstance(self.student_residency_flag, Unset):
            student_residency_flag = self.student_residency_flag.value

        get_student_country_of_domicile: dict[str, Any] | None | Unset
        if isinstance(self.get_student_country_of_domicile, Unset):
            get_student_country_of_domicile = UNSET
        elif isinstance(self.get_student_country_of_domicile, ClassificationRefType0):
            get_student_country_of_domicile = (
                self.get_student_country_of_domicile.to_dict()
            )
        else:
            get_student_country_of_domicile = self.get_student_country_of_domicile

        student_type_description: dict[str, Any] | None | Unset
        if isinstance(self.student_type_description, Unset):
            student_type_description = UNSET
        elif isinstance(self.student_type_description, ClassificationRefType0):
            student_type_description = self.student_type_description.to_dict()
        else:
            student_type_description = self.student_type_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if affiliation_id is not UNSET:
            field_dict["affiliationId"] = affiliation_id
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if organization is not UNSET:
            field_dict["organization"] = organization
        if emails is not UNSET:
            field_dict["emails"] = emails
        if web_addresses is not UNSET:
            field_dict["webAddresses"] = web_addresses
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if period is not UNSET:
            field_dict["period"] = period
        if supervisor_associations is not UNSET:
            field_dict["supervisorAssociations"] = supervisor_associations
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if primary_association is not UNSET:
            field_dict["primaryAssociation"] = primary_association
        if award_date is not UNSET:
            field_dict["awardDate"] = award_date
        if award_gained is not UNSET:
            field_dict["awardGained"] = award_gained
        if fte is not UNSET:
            field_dict["fte"] = fte
        if programme is not UNSET:
            field_dict["programme"] = programme
        if project_title is not UNSET:
            field_dict["projectTitle"] = project_title
        if expected_study_duration is not UNSET:
            field_dict["expectedStudyDuration"] = expected_study_duration
        if minimum_study_duration is not UNSET:
            field_dict["minimumStudyDuration"] = minimum_study_duration
        if maximum_study_duration is not UNSET:
            field_dict["maximumStudyDuration"] = maximum_study_duration
        if program_year is not UNSET:
            field_dict["programYear"] = program_year
        if initial_submission_date is not UNSET:
            field_dict["initialSubmissionDate"] = initial_submission_date
        if get_expected_end_date is not UNSET:
            field_dict["getExpectedEndDate"] = get_expected_end_date
        if start_year is not UNSET:
            field_dict["startYear"] = start_year
        if attendance_status is not UNSET:
            field_dict["attendanceStatus"] = attendance_status
        if get_student_nationality is not UNSET:
            field_dict["getStudentNationality"] = get_student_nationality
        if student_residency_flag is not UNSET:
            field_dict["studentResidencyFlag"] = student_residency_flag
        if get_student_country_of_domicile is not UNSET:
            field_dict["getStudentCountryOfDomicile"] = get_student_country_of_domicile
        if student_type_description is not UNSET:
            field_dict["studentTypeDescription"] = student_type_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_address import ClassifiedAddress
        from ..models.classified_localized_value import ClassifiedLocalizedValue
        from ..models.classified_value import ClassifiedValue
        from ..models.date_range import DateRange
        from ..models.keyword_group import KeywordGroup
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_supervisor_association import PersonSupervisorAssociation

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        pure_id = d.pop("pureId", UNSET)

        def _parse_addresses(data: object) -> list[ClassifiedAddress] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                addresses_type_0 = []
                _addresses_type_0 = data
                for addresses_type_0_item_data in _addresses_type_0:
                    addresses_type_0_item = ClassifiedAddress.from_dict(
                        addresses_type_0_item_data
                    )

                    addresses_type_0.append(addresses_type_0_item)

                return addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedAddress] | None | Unset, data)

        addresses = _parse_addresses(d.pop("addresses", UNSET))

        def _parse_affiliation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        affiliation_id = _parse_affiliation_id(d.pop("affiliationId", UNSET))

        def _parse_employment_type(
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

        employment_type = _parse_employment_type(d.pop("employmentType", UNSET))

        def _parse_organization(data: object) -> None | OrganizationRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_ref_type_0 = (
                    OrganizationRefType0.from_dict(data)
                )

                return componentsschemas_organization_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationRefType0 | Unset, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_emails(data: object) -> list[ClassifiedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = []
                _emails_type_0 = data
                for emails_type_0_item_data in _emails_type_0:
                    emails_type_0_item = ClassifiedValue.from_dict(
                        emails_type_0_item_data
                    )

                    emails_type_0.append(emails_type_0_item)

                return emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedValue] | None | Unset, data)

        emails = _parse_emails(d.pop("emails", UNSET))

        def _parse_web_addresses(
            data: object,
        ) -> list[ClassifiedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                web_addresses_type_0 = []
                _web_addresses_type_0 = data
                for web_addresses_type_0_item_data in _web_addresses_type_0:
                    web_addresses_type_0_item = ClassifiedLocalizedValue.from_dict(
                        web_addresses_type_0_item_data
                    )

                    web_addresses_type_0.append(web_addresses_type_0_item)

                return web_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedLocalizedValue] | None | Unset, data)

        web_addresses = _parse_web_addresses(d.pop("webAddresses", UNSET))

        def _parse_phone_numbers(data: object) -> list[ClassifiedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = []
                _phone_numbers_type_0 = data
                for phone_numbers_type_0_item_data in _phone_numbers_type_0:
                    phone_numbers_type_0_item = ClassifiedValue.from_dict(
                        phone_numbers_type_0_item_data
                    )

                    phone_numbers_type_0.append(phone_numbers_type_0_item)

                return phone_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedValue] | None | Unset, data)

        phone_numbers = _parse_phone_numbers(d.pop("phoneNumbers", UNSET))

        _period = d.pop("period", UNSET)
        period: DateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = DateRange.from_dict(_period)

        def _parse_supervisor_associations(
            data: object,
        ) -> list[PersonSupervisorAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supervisor_associations_type_0 = []
                _supervisor_associations_type_0 = data
                for (
                    supervisor_associations_type_0_item_data
                ) in _supervisor_associations_type_0:
                    supervisor_associations_type_0_item = (
                        PersonSupervisorAssociation.from_dict(
                            supervisor_associations_type_0_item_data
                        )
                    )

                    supervisor_associations_type_0.append(
                        supervisor_associations_type_0_item
                    )

                return supervisor_associations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PersonSupervisorAssociation] | None | Unset, data)

        supervisor_associations = _parse_supervisor_associations(
            d.pop("supervisorAssociations", UNSET)
        )

        def _parse_keyword_groups(data: object) -> list[KeywordGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyword_groups_type_0 = []
                _keyword_groups_type_0 = data
                for keyword_groups_type_0_item_data in _keyword_groups_type_0:
                    keyword_groups_type_0_item = KeywordGroup.from_dict(
                        keyword_groups_type_0_item_data
                    )

                    keyword_groups_type_0.append(keyword_groups_type_0_item)

                return keyword_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeywordGroup] | None | Unset, data)

        keyword_groups = _parse_keyword_groups(d.pop("keywordGroups", UNSET))

        primary_association = d.pop("primaryAssociation", UNSET)

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

        def _parse_award_gained(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        award_gained = _parse_award_gained(d.pop("awardGained", UNSET))

        def _parse_fte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fte = _parse_fte(d.pop("fte", UNSET))

        def _parse_programme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme = _parse_programme(d.pop("programme", UNSET))

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

        def _parse_expected_study_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_study_duration = _parse_expected_study_duration(
            d.pop("expectedStudyDuration", UNSET)
        )

        def _parse_minimum_study_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minimum_study_duration = _parse_minimum_study_duration(
            d.pop("minimumStudyDuration", UNSET)
        )

        def _parse_maximum_study_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maximum_study_duration = _parse_maximum_study_duration(
            d.pop("maximumStudyDuration", UNSET)
        )

        def _parse_program_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_year = _parse_program_year(d.pop("programYear", UNSET))

        def _parse_initial_submission_date(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initial_submission_date_type_0 = isoparse(data).date()

                return initial_submission_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        initial_submission_date = _parse_initial_submission_date(
            d.pop("initialSubmissionDate", UNSET)
        )

        def _parse_get_expected_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                get_expected_end_date_type_0 = isoparse(data).date()

                return get_expected_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        get_expected_end_date = _parse_get_expected_end_date(
            d.pop("getExpectedEndDate", UNSET)
        )

        def _parse_start_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_year = _parse_start_year(d.pop("startYear", UNSET))

        def _parse_attendance_status(
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

        attendance_status = _parse_attendance_status(d.pop("attendanceStatus", UNSET))

        def _parse_get_student_nationality(
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

        get_student_nationality = _parse_get_student_nationality(
            d.pop("getStudentNationality", UNSET)
        )

        _student_residency_flag = d.pop("studentResidencyFlag", UNSET)
        student_residency_flag: (
            StudentOrganizationAssociationStudentResidencyFlag | Unset
        )
        if isinstance(_student_residency_flag, Unset):
            student_residency_flag = UNSET
        else:
            student_residency_flag = StudentOrganizationAssociationStudentResidencyFlag(
                _student_residency_flag
            )

        def _parse_get_student_country_of_domicile(
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

        get_student_country_of_domicile = _parse_get_student_country_of_domicile(
            d.pop("getStudentCountryOfDomicile", UNSET)
        )

        def _parse_student_type_description(
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

        student_type_description = _parse_student_type_description(
            d.pop("studentTypeDescription", UNSET)
        )

        student_organization_association = cls(
            type_discriminator=type_discriminator,
            pure_id=pure_id,
            addresses=addresses,
            affiliation_id=affiliation_id,
            employment_type=employment_type,
            organization=organization,
            emails=emails,
            web_addresses=web_addresses,
            phone_numbers=phone_numbers,
            period=period,
            supervisor_associations=supervisor_associations,
            keyword_groups=keyword_groups,
            primary_association=primary_association,
            award_date=award_date,
            award_gained=award_gained,
            fte=fte,
            programme=programme,
            project_title=project_title,
            expected_study_duration=expected_study_duration,
            minimum_study_duration=minimum_study_duration,
            maximum_study_duration=maximum_study_duration,
            program_year=program_year,
            initial_submission_date=initial_submission_date,
            get_expected_end_date=get_expected_end_date,
            start_year=start_year,
            attendance_status=attendance_status,
            get_student_nationality=get_student_nationality,
            student_residency_flag=student_residency_flag,
            get_student_country_of_domicile=get_student_country_of_domicile,
            student_type_description=student_type_description,
        )

        student_organization_association.additional_properties = d
        return student_organization_association

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
