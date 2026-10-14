from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.currency_amount import CurrencyAmount
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.formatted_string import FormattedString
    from ..models.funding_opportunity_academic_degree_eligibility import (
        FundingOpportunityAcademicDegreeEligibility,
    )
    from ..models.funding_opportunity_document import FundingOpportunityDocument
    from ..models.funding_opportunity_eligibility import FundingOpportunityEligibility
    from ..models.identifier import Identifier
    from ..models.keyword_group import KeywordGroup
    from ..models.label import Label
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.user_ref_type_0 import UserRefType0
    from ..models.visibility import Visibility


T = TypeVar("T", bound="ExternalFundingOpportunity")


@_attrs_define
class ExternalFundingOpportunity:
    """One of the Funding Opportunity types

    Attributes:
        type_ (ClassificationRefType0 | None): A reference to a classification value
        title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        type_discriminator (str):
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        uuid (UUID | Unset): UUID, this is the primary identity of the entity
        created_by (str | Unset): Username of creator
        created_date (datetime.datetime | Unset): Date and time of creation
        modified_by (str | Unset): Username of the user that performed a modification
        modified_date (datetime.datetime | Unset): Date and time of last modification
        portal_url (str | Unset): URL of the content on the Pure Portal
        pretty_url_identifiers (list[str] | Unset): All pretty URLs
        previous_uuids (list[str] | Unset): UUIDs of other content items which have been merged into this content item
            (or similar)
        version (None | str | Unset): Used to guard against conflicting updates. For new content this is null, and for
            existing content the current value. The property should never be modified by a client, except in the rare case
            where the client wants to perform an update irrespective of if other clients have made updates in the meantime,
            also known as a "dirty write". A dirty write is performed by not including the property value or setting the
            property to null
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        visibility (Visibility | Unset): Visibility of an object
        identifiers (list[Identifier] | None | Unset): Identifiers related to the funding opportunity.
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the funding opportunity.
        description (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        description_of_application_process (FormattedString | Unset): A string containing HTML formatted text
        url (None | str | Unset): The url to full announcement to the funding opportunity
        url_to_application_site (None | str | Unset): The url to the application site of the funding opportunity
        email_address_for_application (None | str | Unset): The email address to send the application to for the funding
            opportunity
        funding_organizations (list[ExternalOrganizationRefType0 | None] | Unset): A collection of funding organization
            for the funding opportunity.
        opening_date (datetime.date | None | Unset): The opening date of the funding opportunity.
        deadline (datetime.date | None | Unset): The deadline of the funding opportunity.
        letter_of_intent_date (datetime.date | None | Unset): The letter of intent date of the funding opportunity.
        active (bool | Unset):
        recurring (bool | Unset):
        award_ceiling (CurrencyAmount | Unset): A monetary value in the specified currency as defined by the W3C's
            Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        estimated_funding (CurrencyAmount | Unset): A monetary value in the specified currency as defined by the W3C's
            Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        eligibilities (list[FundingOpportunityEligibility] | Unset): The eligibilities of the funding opportunity
        academic_degree_eligibilities (list[FundingOpportunityAcademicDegreeEligibility] | Unset): The academic degree
            eligibilities of the funding opportunity
        limited_submission (bool | Unset):
        number_of_annual_applications_per_hei (int | Unset):
        number_of_awards (int | Unset):
        open_access_requirements (bool | Unset):
        associated_application_count (int | Unset):
        created_by_users (list[None | UserRefType0] | Unset):
        shared_with_users (list[None | UserRefType0] | Unset):
        rejected_by_users (list[None | UserRefType0] | Unset):
        shared_with_organizations (list[None | OrganizationRefType0] | Unset):
        nature_types (list[ClassificationRefType0 | None] | Unset): The nature types of the funding opportunity
        administrative_labels (list[Label] | Unset): Administrative labels of the funding opportunity.
        labels (list[Label] | Unset): Labels of the funding opportunity.
        academic_labels (list[Label] | Unset): Academic labels of the funding opportunity.
        documents (list[FundingOpportunityDocument] | None | Unset): Associated documents for the funding opportunity.
        system_name (str | Unset): The content system name
    """

    type_: ClassificationRefType0 | None
    title: LocalizedStringType0 | None
    type_discriminator: str
    pure_id: int | Unset = UNSET
    uuid: UUID | Unset = UNSET
    created_by: str | Unset = UNSET
    created_date: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    portal_url: str | Unset = UNSET
    pretty_url_identifiers: list[str] | Unset = UNSET
    previous_uuids: list[str] | Unset = UNSET
    version: None | str | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    description: FormattedLocalizedStringType0 | None | Unset = UNSET
    description_of_application_process: FormattedString | Unset = UNSET
    url: None | str | Unset = UNSET
    url_to_application_site: None | str | Unset = UNSET
    email_address_for_application: None | str | Unset = UNSET
    funding_organizations: list[ExternalOrganizationRefType0 | None] | Unset = UNSET
    opening_date: datetime.date | None | Unset = UNSET
    deadline: datetime.date | None | Unset = UNSET
    letter_of_intent_date: datetime.date | None | Unset = UNSET
    active: bool | Unset = UNSET
    recurring: bool | Unset = UNSET
    award_ceiling: CurrencyAmount | Unset = UNSET
    estimated_funding: CurrencyAmount | Unset = UNSET
    eligibilities: list[FundingOpportunityEligibility] | Unset = UNSET
    academic_degree_eligibilities: (
        list[FundingOpportunityAcademicDegreeEligibility] | Unset
    ) = UNSET
    limited_submission: bool | Unset = UNSET
    number_of_annual_applications_per_hei: int | Unset = UNSET
    number_of_awards: int | Unset = UNSET
    open_access_requirements: bool | Unset = UNSET
    associated_application_count: int | Unset = UNSET
    created_by_users: list[None | UserRefType0] | Unset = UNSET
    shared_with_users: list[None | UserRefType0] | Unset = UNSET
    rejected_by_users: list[None | UserRefType0] | Unset = UNSET
    shared_with_organizations: list[None | OrganizationRefType0] | Unset = UNSET
    nature_types: list[ClassificationRefType0 | None] | Unset = UNSET
    administrative_labels: list[Label] | Unset = UNSET
    labels: list[Label] | Unset = UNSET
    academic_labels: list[Label] | Unset = UNSET
    documents: list[FundingOpportunityDocument] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.user_ref_type_0 import UserRefType0

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        title: dict[str, Any] | None
        if isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        type_discriminator = self.type_discriminator

        pure_id = self.pure_id

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        created_by = self.created_by

        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        modified_by = self.modified_by

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        portal_url = self.portal_url

        pretty_url_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pretty_url_identifiers, Unset):
            pretty_url_identifiers = self.pretty_url_identifiers

        previous_uuids: list[str] | Unset = UNSET
        if not isinstance(self.previous_uuids, Unset):
            previous_uuids = self.previous_uuids

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        identifiers: list[dict[str, Any]] | None | Unset
        if isinstance(self.identifiers, Unset):
            identifiers = UNSET
        elif isinstance(self.identifiers, list):
            identifiers = []
            for identifiers_type_0_item_data in self.identifiers:
                identifiers_type_0_item = identifiers_type_0_item_data.to_dict()
                identifiers.append(identifiers_type_0_item)

        else:
            identifiers = self.identifiers

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

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, FormattedLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        description_of_application_process: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description_of_application_process, Unset):
            description_of_application_process = (
                self.description_of_application_process.to_dict()
            )

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        url_to_application_site: None | str | Unset
        if isinstance(self.url_to_application_site, Unset):
            url_to_application_site = UNSET
        else:
            url_to_application_site = self.url_to_application_site

        email_address_for_application: None | str | Unset
        if isinstance(self.email_address_for_application, Unset):
            email_address_for_application = UNSET
        else:
            email_address_for_application = self.email_address_for_application

        funding_organizations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.funding_organizations, Unset):
            funding_organizations = []
            for funding_organizations_item_data in self.funding_organizations:
                funding_organizations_item: dict[str, Any] | None
                if isinstance(
                    funding_organizations_item_data, ExternalOrganizationRefType0
                ):
                    funding_organizations_item = (
                        funding_organizations_item_data.to_dict()
                    )
                else:
                    funding_organizations_item = funding_organizations_item_data
                funding_organizations.append(funding_organizations_item)

        opening_date: None | str | Unset
        if isinstance(self.opening_date, Unset):
            opening_date = UNSET
        elif isinstance(self.opening_date, datetime.date):
            opening_date = self.opening_date.isoformat()
        else:
            opening_date = self.opening_date

        deadline: None | str | Unset
        if isinstance(self.deadline, Unset):
            deadline = UNSET
        elif isinstance(self.deadline, datetime.date):
            deadline = self.deadline.isoformat()
        else:
            deadline = self.deadline

        letter_of_intent_date: None | str | Unset
        if isinstance(self.letter_of_intent_date, Unset):
            letter_of_intent_date = UNSET
        elif isinstance(self.letter_of_intent_date, datetime.date):
            letter_of_intent_date = self.letter_of_intent_date.isoformat()
        else:
            letter_of_intent_date = self.letter_of_intent_date

        active = self.active

        recurring = self.recurring

        award_ceiling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.award_ceiling, Unset):
            award_ceiling = self.award_ceiling.to_dict()

        estimated_funding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_funding, Unset):
            estimated_funding = self.estimated_funding.to_dict()

        eligibilities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eligibilities, Unset):
            eligibilities = []
            for eligibilities_item_data in self.eligibilities:
                eligibilities_item = eligibilities_item_data.to_dict()
                eligibilities.append(eligibilities_item)

        academic_degree_eligibilities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.academic_degree_eligibilities, Unset):
            academic_degree_eligibilities = []
            for (
                academic_degree_eligibilities_item_data
            ) in self.academic_degree_eligibilities:
                academic_degree_eligibilities_item = (
                    academic_degree_eligibilities_item_data.to_dict()
                )
                academic_degree_eligibilities.append(academic_degree_eligibilities_item)

        limited_submission = self.limited_submission

        number_of_annual_applications_per_hei = (
            self.number_of_annual_applications_per_hei
        )

        number_of_awards = self.number_of_awards

        open_access_requirements = self.open_access_requirements

        associated_application_count = self.associated_application_count

        created_by_users: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.created_by_users, Unset):
            created_by_users = []
            for created_by_users_item_data in self.created_by_users:
                created_by_users_item: dict[str, Any] | None
                if isinstance(created_by_users_item_data, UserRefType0):
                    created_by_users_item = created_by_users_item_data.to_dict()
                else:
                    created_by_users_item = created_by_users_item_data
                created_by_users.append(created_by_users_item)

        shared_with_users: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.shared_with_users, Unset):
            shared_with_users = []
            for shared_with_users_item_data in self.shared_with_users:
                shared_with_users_item: dict[str, Any] | None
                if isinstance(shared_with_users_item_data, UserRefType0):
                    shared_with_users_item = shared_with_users_item_data.to_dict()
                else:
                    shared_with_users_item = shared_with_users_item_data
                shared_with_users.append(shared_with_users_item)

        rejected_by_users: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.rejected_by_users, Unset):
            rejected_by_users = []
            for rejected_by_users_item_data in self.rejected_by_users:
                rejected_by_users_item: dict[str, Any] | None
                if isinstance(rejected_by_users_item_data, UserRefType0):
                    rejected_by_users_item = rejected_by_users_item_data.to_dict()
                else:
                    rejected_by_users_item = rejected_by_users_item_data
                rejected_by_users.append(rejected_by_users_item)

        shared_with_organizations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.shared_with_organizations, Unset):
            shared_with_organizations = []
            for shared_with_organizations_item_data in self.shared_with_organizations:
                shared_with_organizations_item: dict[str, Any] | None
                if isinstance(
                    shared_with_organizations_item_data, OrganizationRefType0
                ):
                    shared_with_organizations_item = (
                        shared_with_organizations_item_data.to_dict()
                    )
                else:
                    shared_with_organizations_item = shared_with_organizations_item_data
                shared_with_organizations.append(shared_with_organizations_item)

        nature_types: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.nature_types, Unset):
            nature_types = []
            for nature_types_item_data in self.nature_types:
                nature_types_item: dict[str, Any] | None
                if isinstance(nature_types_item_data, ClassificationRefType0):
                    nature_types_item = nature_types_item_data.to_dict()
                else:
                    nature_types_item = nature_types_item_data
                nature_types.append(nature_types_item)

        administrative_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.administrative_labels, Unset):
            administrative_labels = []
            for administrative_labels_item_data in self.administrative_labels:
                administrative_labels_item = administrative_labels_item_data.to_dict()
                administrative_labels.append(administrative_labels_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        academic_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.academic_labels, Unset):
            academic_labels = []
            for academic_labels_item_data in self.academic_labels:
                academic_labels_item = academic_labels_item_data.to_dict()
                academic_labels.append(academic_labels_item)

        documents: list[dict[str, Any]] | None | Unset
        if isinstance(self.documents, Unset):
            documents = UNSET
        elif isinstance(self.documents, list):
            documents = []
            for documents_type_0_item_data in self.documents:
                documents_type_0_item = documents_type_0_item_data.to_dict()
                documents.append(documents_type_0_item)

        else:
            documents = self.documents

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "typeDiscriminator": type_discriminator,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if portal_url is not UNSET:
            field_dict["portalUrl"] = portal_url
        if pretty_url_identifiers is not UNSET:
            field_dict["prettyUrlIdentifiers"] = pretty_url_identifiers
        if previous_uuids is not UNSET:
            field_dict["previousUuids"] = previous_uuids
        if version is not UNSET:
            field_dict["version"] = version
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if description is not UNSET:
            field_dict["description"] = description
        if description_of_application_process is not UNSET:
            field_dict["descriptionOfApplicationProcess"] = (
                description_of_application_process
            )
        if url is not UNSET:
            field_dict["url"] = url
        if url_to_application_site is not UNSET:
            field_dict["urlToApplicationSite"] = url_to_application_site
        if email_address_for_application is not UNSET:
            field_dict["emailAddressForApplication"] = email_address_for_application
        if funding_organizations is not UNSET:
            field_dict["fundingOrganizations"] = funding_organizations
        if opening_date is not UNSET:
            field_dict["openingDate"] = opening_date
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if letter_of_intent_date is not UNSET:
            field_dict["letterOfIntentDate"] = letter_of_intent_date
        if active is not UNSET:
            field_dict["active"] = active
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if award_ceiling is not UNSET:
            field_dict["awardCeiling"] = award_ceiling
        if estimated_funding is not UNSET:
            field_dict["estimatedFunding"] = estimated_funding
        if eligibilities is not UNSET:
            field_dict["eligibilities"] = eligibilities
        if academic_degree_eligibilities is not UNSET:
            field_dict["academicDegreeEligibilities"] = academic_degree_eligibilities
        if limited_submission is not UNSET:
            field_dict["limitedSubmission"] = limited_submission
        if number_of_annual_applications_per_hei is not UNSET:
            field_dict["numberOfAnnualApplicationsPerHEI"] = (
                number_of_annual_applications_per_hei
            )
        if number_of_awards is not UNSET:
            field_dict["numberOfAwards"] = number_of_awards
        if open_access_requirements is not UNSET:
            field_dict["openAccessRequirements"] = open_access_requirements
        if associated_application_count is not UNSET:
            field_dict["associatedApplicationCount"] = associated_application_count
        if created_by_users is not UNSET:
            field_dict["createdByUsers"] = created_by_users
        if shared_with_users is not UNSET:
            field_dict["sharedWithUsers"] = shared_with_users
        if rejected_by_users is not UNSET:
            field_dict["rejectedByUsers"] = rejected_by_users
        if shared_with_organizations is not UNSET:
            field_dict["sharedWithOrganizations"] = shared_with_organizations
        if nature_types is not UNSET:
            field_dict["natureTypes"] = nature_types
        if administrative_labels is not UNSET:
            field_dict["administrativeLabels"] = administrative_labels
        if labels is not UNSET:
            field_dict["labels"] = labels
        if academic_labels is not UNSET:
            field_dict["academicLabels"] = academic_labels
        if documents is not UNSET:
            field_dict["documents"] = documents
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.currency_amount import CurrencyAmount
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.formatted_string import FormattedString
        from ..models.funding_opportunity_academic_degree_eligibility import (
            FundingOpportunityAcademicDegreeEligibility,
        )
        from ..models.funding_opportunity_document import FundingOpportunityDocument
        from ..models.funding_opportunity_eligibility import (
            FundingOpportunityEligibility,
        )
        from ..models.identifier import Identifier
        from ..models.keyword_group import KeywordGroup
        from ..models.label import Label
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.user_ref_type_0 import UserRefType0
        from ..models.visibility import Visibility

        d = dict(src_dict)

        def _parse_type_(data: object) -> ClassificationRefType0 | None:
            if data is None:
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
            return cast(ClassificationRefType0 | None, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_title(data: object) -> LocalizedStringType0 | None:
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

        title = _parse_title(d.pop("title"))

        type_discriminator = d.pop("typeDiscriminator")

        pure_id = d.pop("pureId", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        created_by = d.pop("createdBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        modified_by = d.pop("modifiedBy", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        portal_url = d.pop("portalUrl", UNSET)

        pretty_url_identifiers = cast(list[str], d.pop("prettyUrlIdentifiers", UNSET))

        previous_uuids = cast(list[str], d.pop("previousUuids", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_custom_defined_fields(
            data: object,
        ) -> CustomDefinedFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_custom_defined_fields_type_0 = (
                    CustomDefinedFieldsType0.from_dict(data)
                )

                return componentsschemas_custom_defined_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDefinedFieldsType0 | None | Unset, data)

        custom_defined_fields = _parse_custom_defined_fields(
            d.pop("customDefinedFields", UNSET)
        )

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        def _parse_identifiers(data: object) -> list[Identifier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                identifiers_type_0 = []
                _identifiers_type_0 = data
                for identifiers_type_0_item_data in _identifiers_type_0:
                    identifiers_type_0_item = Identifier.from_dict(
                        identifiers_type_0_item_data
                    )

                    identifiers_type_0.append(identifiers_type_0_item)

                return identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Identifier] | None | Unset, data)

        identifiers = _parse_identifiers(d.pop("identifiers", UNSET))

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

        def _parse_description(
            data: object,
        ) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _description_of_application_process = d.pop(
            "descriptionOfApplicationProcess", UNSET
        )
        description_of_application_process: FormattedString | Unset
        if isinstance(_description_of_application_process, Unset):
            description_of_application_process = UNSET
        else:
            description_of_application_process = FormattedString.from_dict(
                _description_of_application_process
            )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_url_to_application_site(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_to_application_site = _parse_url_to_application_site(
            d.pop("urlToApplicationSite", UNSET)
        )

        def _parse_email_address_for_application(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_for_application = _parse_email_address_for_application(
            d.pop("emailAddressForApplication", UNSET)
        )

        _funding_organizations = d.pop("fundingOrganizations", UNSET)
        funding_organizations: list[ExternalOrganizationRefType0 | None] | Unset = UNSET
        if _funding_organizations is not UNSET:
            funding_organizations = []
            for funding_organizations_item_data in _funding_organizations:

                def _parse_funding_organizations_item(
                    data: object,
                ) -> ExternalOrganizationRefType0 | None:
                    if data is None:
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
                    return cast(ExternalOrganizationRefType0 | None, data)

                funding_organizations_item = _parse_funding_organizations_item(
                    funding_organizations_item_data
                )

                funding_organizations.append(funding_organizations_item)

        def _parse_opening_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opening_date_type_0 = isoparse(data).date()

                return opening_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        opening_date = _parse_opening_date(d.pop("openingDate", UNSET))

        def _parse_deadline(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_type_0 = isoparse(data).date()

                return deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        deadline = _parse_deadline(d.pop("deadline", UNSET))

        def _parse_letter_of_intent_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                letter_of_intent_date_type_0 = isoparse(data).date()

                return letter_of_intent_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        letter_of_intent_date = _parse_letter_of_intent_date(
            d.pop("letterOfIntentDate", UNSET)
        )

        active = d.pop("active", UNSET)

        recurring = d.pop("recurring", UNSET)

        _award_ceiling = d.pop("awardCeiling", UNSET)
        award_ceiling: CurrencyAmount | Unset
        if isinstance(_award_ceiling, Unset):
            award_ceiling = UNSET
        else:
            award_ceiling = CurrencyAmount.from_dict(_award_ceiling)

        _estimated_funding = d.pop("estimatedFunding", UNSET)
        estimated_funding: CurrencyAmount | Unset
        if isinstance(_estimated_funding, Unset):
            estimated_funding = UNSET
        else:
            estimated_funding = CurrencyAmount.from_dict(_estimated_funding)

        _eligibilities = d.pop("eligibilities", UNSET)
        eligibilities: list[FundingOpportunityEligibility] | Unset = UNSET
        if _eligibilities is not UNSET:
            eligibilities = []
            for eligibilities_item_data in _eligibilities:
                eligibilities_item = FundingOpportunityEligibility.from_dict(
                    eligibilities_item_data
                )

                eligibilities.append(eligibilities_item)

        _academic_degree_eligibilities = d.pop("academicDegreeEligibilities", UNSET)
        academic_degree_eligibilities: (
            list[FundingOpportunityAcademicDegreeEligibility] | Unset
        ) = UNSET
        if _academic_degree_eligibilities is not UNSET:
            academic_degree_eligibilities = []
            for (
                academic_degree_eligibilities_item_data
            ) in _academic_degree_eligibilities:
                academic_degree_eligibilities_item = (
                    FundingOpportunityAcademicDegreeEligibility.from_dict(
                        academic_degree_eligibilities_item_data
                    )
                )

                academic_degree_eligibilities.append(academic_degree_eligibilities_item)

        limited_submission = d.pop("limitedSubmission", UNSET)

        number_of_annual_applications_per_hei = d.pop(
            "numberOfAnnualApplicationsPerHEI", UNSET
        )

        number_of_awards = d.pop("numberOfAwards", UNSET)

        open_access_requirements = d.pop("openAccessRequirements", UNSET)

        associated_application_count = d.pop("associatedApplicationCount", UNSET)

        _created_by_users = d.pop("createdByUsers", UNSET)
        created_by_users: list[None | UserRefType0] | Unset = UNSET
        if _created_by_users is not UNSET:
            created_by_users = []
            for created_by_users_item_data in _created_by_users:

                def _parse_created_by_users_item(data: object) -> None | UserRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                        return componentsschemas_user_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UserRefType0, data)

                created_by_users_item = _parse_created_by_users_item(
                    created_by_users_item_data
                )

                created_by_users.append(created_by_users_item)

        _shared_with_users = d.pop("sharedWithUsers", UNSET)
        shared_with_users: list[None | UserRefType0] | Unset = UNSET
        if _shared_with_users is not UNSET:
            shared_with_users = []
            for shared_with_users_item_data in _shared_with_users:

                def _parse_shared_with_users_item(data: object) -> None | UserRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                        return componentsschemas_user_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UserRefType0, data)

                shared_with_users_item = _parse_shared_with_users_item(
                    shared_with_users_item_data
                )

                shared_with_users.append(shared_with_users_item)

        _rejected_by_users = d.pop("rejectedByUsers", UNSET)
        rejected_by_users: list[None | UserRefType0] | Unset = UNSET
        if _rejected_by_users is not UNSET:
            rejected_by_users = []
            for rejected_by_users_item_data in _rejected_by_users:

                def _parse_rejected_by_users_item(data: object) -> None | UserRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                        return componentsschemas_user_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UserRefType0, data)

                rejected_by_users_item = _parse_rejected_by_users_item(
                    rejected_by_users_item_data
                )

                rejected_by_users.append(rejected_by_users_item)

        _shared_with_organizations = d.pop("sharedWithOrganizations", UNSET)
        shared_with_organizations: list[None | OrganizationRefType0] | Unset = UNSET
        if _shared_with_organizations is not UNSET:
            shared_with_organizations = []
            for shared_with_organizations_item_data in _shared_with_organizations:

                def _parse_shared_with_organizations_item(
                    data: object,
                ) -> None | OrganizationRefType0:
                    if data is None:
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
                    return cast(None | OrganizationRefType0, data)

                shared_with_organizations_item = _parse_shared_with_organizations_item(
                    shared_with_organizations_item_data
                )

                shared_with_organizations.append(shared_with_organizations_item)

        _nature_types = d.pop("natureTypes", UNSET)
        nature_types: list[ClassificationRefType0 | None] | Unset = UNSET
        if _nature_types is not UNSET:
            nature_types = []
            for nature_types_item_data in _nature_types:

                def _parse_nature_types_item(
                    data: object,
                ) -> ClassificationRefType0 | None:
                    if data is None:
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
                    return cast(ClassificationRefType0 | None, data)

                nature_types_item = _parse_nature_types_item(nature_types_item_data)

                nature_types.append(nature_types_item)

        _administrative_labels = d.pop("administrativeLabels", UNSET)
        administrative_labels: list[Label] | Unset = UNSET
        if _administrative_labels is not UNSET:
            administrative_labels = []
            for administrative_labels_item_data in _administrative_labels:
                administrative_labels_item = Label.from_dict(
                    administrative_labels_item_data
                )

                administrative_labels.append(administrative_labels_item)

        _labels = d.pop("labels", UNSET)
        labels: list[Label] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = Label.from_dict(labels_item_data)

                labels.append(labels_item)

        _academic_labels = d.pop("academicLabels", UNSET)
        academic_labels: list[Label] | Unset = UNSET
        if _academic_labels is not UNSET:
            academic_labels = []
            for academic_labels_item_data in _academic_labels:
                academic_labels_item = Label.from_dict(academic_labels_item_data)

                academic_labels.append(academic_labels_item)

        def _parse_documents(
            data: object,
        ) -> list[FundingOpportunityDocument] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                documents_type_0 = []
                _documents_type_0 = data
                for documents_type_0_item_data in _documents_type_0:
                    documents_type_0_item = FundingOpportunityDocument.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FundingOpportunityDocument] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

        system_name = d.pop("systemName", UNSET)

        external_funding_opportunity = cls(
            type_=type_,
            title=title,
            type_discriminator=type_discriminator,
            pure_id=pure_id,
            uuid=uuid,
            created_by=created_by,
            created_date=created_date,
            modified_by=modified_by,
            modified_date=modified_date,
            portal_url=portal_url,
            pretty_url_identifiers=pretty_url_identifiers,
            previous_uuids=previous_uuids,
            version=version,
            custom_defined_fields=custom_defined_fields,
            visibility=visibility,
            identifiers=identifiers,
            keyword_groups=keyword_groups,
            description=description,
            description_of_application_process=description_of_application_process,
            url=url,
            url_to_application_site=url_to_application_site,
            email_address_for_application=email_address_for_application,
            funding_organizations=funding_organizations,
            opening_date=opening_date,
            deadline=deadline,
            letter_of_intent_date=letter_of_intent_date,
            active=active,
            recurring=recurring,
            award_ceiling=award_ceiling,
            estimated_funding=estimated_funding,
            eligibilities=eligibilities,
            academic_degree_eligibilities=academic_degree_eligibilities,
            limited_submission=limited_submission,
            number_of_annual_applications_per_hei=number_of_annual_applications_per_hei,
            number_of_awards=number_of_awards,
            open_access_requirements=open_access_requirements,
            associated_application_count=associated_application_count,
            created_by_users=created_by_users,
            shared_with_users=shared_with_users,
            rejected_by_users=rejected_by_users,
            shared_with_organizations=shared_with_organizations,
            nature_types=nature_types,
            administrative_labels=administrative_labels,
            labels=labels,
            academic_labels=academic_labels,
            documents=documents,
            system_name=system_name,
        )

        external_funding_opportunity.additional_properties = d
        return external_funding_opportunity

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
