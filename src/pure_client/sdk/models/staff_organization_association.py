from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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


T = TypeVar("T", bound="StaffOrganizationAssociation")


@_attrs_define
class StaffOrganizationAssociation:
    """A relation describing the association between Staff and organization

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
        contract_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        fte (float | None | Unset): The FTE (Full-Time Equivalent). A decimal number ranging between 0 (0% equivalent of
            full time) and 1 (100% equivalent of full time).
        job_description (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        job_title (ClassificationRefType0 | None | Unset): A reference to a classification value
        staff_type (ClassificationRefType0 | None | Unset): A reference to a classification value
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
    contract_type: ClassificationRefType0 | None | Unset = UNSET
    fte: float | None | Unset = UNSET
    job_description: LocalizedStringType0 | None | Unset = UNSET
    job_title: ClassificationRefType0 | None | Unset = UNSET
    staff_type: ClassificationRefType0 | None | Unset = UNSET
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

        contract_type: dict[str, Any] | None | Unset
        if isinstance(self.contract_type, Unset):
            contract_type = UNSET
        elif isinstance(self.contract_type, ClassificationRefType0):
            contract_type = self.contract_type.to_dict()
        else:
            contract_type = self.contract_type

        fte: float | None | Unset
        if isinstance(self.fte, Unset):
            fte = UNSET
        else:
            fte = self.fte

        job_description: dict[str, Any] | None | Unset
        if isinstance(self.job_description, Unset):
            job_description = UNSET
        elif isinstance(self.job_description, LocalizedStringType0):
            job_description = self.job_description.to_dict()
        else:
            job_description = self.job_description

        job_title: dict[str, Any] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, ClassificationRefType0):
            job_title = self.job_title.to_dict()
        else:
            job_title = self.job_title

        staff_type: dict[str, Any] | None | Unset
        if isinstance(self.staff_type, Unset):
            staff_type = UNSET
        elif isinstance(self.staff_type, ClassificationRefType0):
            staff_type = self.staff_type.to_dict()
        else:
            staff_type = self.staff_type

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
        if contract_type is not UNSET:
            field_dict["contractType"] = contract_type
        if fte is not UNSET:
            field_dict["fte"] = fte
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if staff_type is not UNSET:
            field_dict["staffType"] = staff_type

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

        def _parse_contract_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        contract_type = _parse_contract_type(d.pop("contractType", UNSET))

        def _parse_fte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fte = _parse_fte(d.pop("fte", UNSET))

        def _parse_job_description(data: object) -> LocalizedStringType0 | None | Unset:
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

        job_description = _parse_job_description(d.pop("jobDescription", UNSET))

        def _parse_job_title(data: object) -> ClassificationRefType0 | None | Unset:
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

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_staff_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        staff_type = _parse_staff_type(d.pop("staffType", UNSET))

        staff_organization_association = cls(
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
            contract_type=contract_type,
            fte=fte,
            job_description=job_description,
            job_title=job_title,
            staff_type=staff_type,
        )

        staff_organization_association.additional_properties = d
        return staff_organization_association

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
