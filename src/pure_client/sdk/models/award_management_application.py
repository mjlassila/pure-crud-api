from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.award_management_application_funder_reply import (
    AwardManagementApplicationFunderReply,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_applicant_association import AbstractApplicantAssociation
    from ..models.application_cluster_ref_type_0 import ApplicationClusterRefType0
    from ..models.application_document import ApplicationDocument
    from ..models.application_funding_association import ApplicationFundingAssociation
    from ..models.application_ref_type_0 import ApplicationRefType0
    from ..models.award_ref_type_0 import AwardRefType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_localized_value import ClassifiedLocalizedValue
    from ..models.collaborator_association import CollaboratorAssociation
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.date_range import DateRange
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.funding_opportunity_ref_type_0 import FundingOpportunityRefType0
    from ..models.identifier import Identifier
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.system_currency_amount import SystemCurrencyAmount
    from ..models.user_ref_type_0 import UserRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="AwardManagementApplication")


@_attrs_define
class AwardManagementApplication:
    """The Award Management application template is used when the Award Management module is enabled for the Pure
    installation.

        Attributes:
            fundings (list[ApplicationFundingAssociation]): A collection of funding information for the application.
            organizations (list[None | OrganizationRefType0]): A collection of organizational unit affiliations.
            managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
            title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
                locale values will be ignored. Example: {'en_GB': 'Some text'}.
            type_ (ClassificationRefType0 | None): A reference to a classification value
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
            acronym (None | str | Unset): The acronym of the application
            applicants (list[AbstractApplicantAssociation] | Unset): Related applicants and their affiliations.
            external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
                organization affiliations.
            application_date (datetime.date | Unset): The date of application, ie. the date it was submitted to the funder.
            awards (list[AwardRefType0 | None] | None | Unset): A collection of related grants.
            budget_applied_amount_difference (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's
                system currency as defined by the W3C's Payment Request standard: https://www.w3.org/TR/payment-
                request/#paymentcurrencyamount-dictionary
            co_managing_organizations (list[None | OrganizationRefType0] | None | Unset): A collection of co-managing
                organizational unit affiliations.
            collaborators (list[CollaboratorAssociation] | None | Unset): A collection of collaborators.
            descriptions (list[ClassifiedLocalizedValue] | None | Unset): A collection of descriptions for the application.
                Query the /applications/allowed-description-types endpoint for allowed types.
            expected_period (DateRange | Unset): A date range
            identifiers (list[Identifier] | None | Unset): Identifiers related to the application.
            funding_opportunity (FundingOpportunityRefType0 | None | Unset): A reference to a funding opportunity
            nature_types (list[ClassificationRefType0 | None] | None | Unset): Nature of activity types for the application.
            applications (list[ApplicationRefType0 | None] | None | Unset): A collection of related applications.
            short_title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
                invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
            total_academic_ownership (float | Unset): Total academic ownership of the application.
            total_applied_amount (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency
                as defined by the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-
                dictionary
            workflow (Workflow | Unset): Information about workflow
            visibility (Visibility | Unset): Visibility of an object
            links (list[Link] | None | Unset): Links associated with the application.
            keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the application.
            custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
                is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
            cluster (ApplicationClusterRefType0 | None | Unset): A reference to an application cluster
            system_name (str | Unset): The content system name
            award_date (datetime.date | None | Unset): The date the application was awarded by the funder.
            documents (list[ApplicationDocument] | None | Unset): A collection of documents related to the application.
            funder_reply (AwardManagementApplicationFunderReply | Unset): Funder reply value
            pre_approver (None | Unset | UserRefType0): A reference to an user
            rejected_date (datetime.date | None | Unset): The date the application was rejected by the funder.
            submission_date (datetime.date | None | Unset): The date the application was submitted to the funder.
            submission_deadline (datetime.date | None | Unset): The submission deadline of the application.
    """

    fundings: list[ApplicationFundingAssociation]
    organizations: list[None | OrganizationRefType0]
    managing_organization: None | OrganizationRefType0
    title: LocalizedStringType0 | None
    type_: ClassificationRefType0 | None
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
    acronym: None | str | Unset = UNSET
    applicants: list[AbstractApplicantAssociation] | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    application_date: datetime.date | Unset = UNSET
    awards: list[AwardRefType0 | None] | None | Unset = UNSET
    budget_applied_amount_difference: SystemCurrencyAmount | Unset = UNSET
    co_managing_organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    collaborators: list[CollaboratorAssociation] | None | Unset = UNSET
    descriptions: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    expected_period: DateRange | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    funding_opportunity: FundingOpportunityRefType0 | None | Unset = UNSET
    nature_types: list[ClassificationRefType0 | None] | None | Unset = UNSET
    applications: list[ApplicationRefType0 | None] | None | Unset = UNSET
    short_title: LocalizedStringType0 | None | Unset = UNSET
    total_academic_ownership: float | Unset = UNSET
    total_applied_amount: SystemCurrencyAmount | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    cluster: ApplicationClusterRefType0 | None | Unset = UNSET
    system_name: str | Unset = UNSET
    award_date: datetime.date | None | Unset = UNSET
    documents: list[ApplicationDocument] | None | Unset = UNSET
    funder_reply: AwardManagementApplicationFunderReply | Unset = UNSET
    pre_approver: None | Unset | UserRefType0 = UNSET
    rejected_date: datetime.date | None | Unset = UNSET
    submission_date: datetime.date | None | Unset = UNSET
    submission_deadline: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_cluster_ref_type_0 import ApplicationClusterRefType0
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.funding_opportunity_ref_type_0 import FundingOpportunityRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.user_ref_type_0 import UserRefType0

        fundings = []
        for fundings_item_data in self.fundings:
            fundings_item = fundings_item_data.to_dict()
            fundings.append(fundings_item)

        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item: dict[str, Any] | None
            if isinstance(organizations_item_data, OrganizationRefType0):
                organizations_item = organizations_item_data.to_dict()
            else:
                organizations_item = organizations_item_data
            organizations.append(organizations_item)

        managing_organization: dict[str, Any] | None
        if isinstance(self.managing_organization, OrganizationRefType0):
            managing_organization = self.managing_organization.to_dict()
        else:
            managing_organization = self.managing_organization

        title: dict[str, Any] | None
        if isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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

        acronym: None | str | Unset
        if isinstance(self.acronym, Unset):
            acronym = UNSET
        else:
            acronym = self.acronym

        applicants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applicants, Unset):
            applicants = []
            for applicants_item_data in self.applicants:
                applicants_item = applicants_item_data.to_dict()
                applicants.append(applicants_item)

        external_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.external_organizations, Unset):
            external_organizations = UNSET
        elif isinstance(self.external_organizations, list):
            external_organizations = []
            for external_organizations_type_0_item_data in self.external_organizations:
                external_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    external_organizations_type_0_item_data,
                    ExternalOrganizationRefType0,
                ):
                    external_organizations_type_0_item = (
                        external_organizations_type_0_item_data.to_dict()
                    )
                else:
                    external_organizations_type_0_item = (
                        external_organizations_type_0_item_data
                    )
                external_organizations.append(external_organizations_type_0_item)

        else:
            external_organizations = self.external_organizations

        application_date: str | Unset = UNSET
        if not isinstance(self.application_date, Unset):
            application_date = self.application_date.isoformat()

        awards: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.awards, Unset):
            awards = UNSET
        elif isinstance(self.awards, list):
            awards = []
            for awards_type_0_item_data in self.awards:
                awards_type_0_item: dict[str, Any] | None
                if isinstance(awards_type_0_item_data, AwardRefType0):
                    awards_type_0_item = awards_type_0_item_data.to_dict()
                else:
                    awards_type_0_item = awards_type_0_item_data
                awards.append(awards_type_0_item)

        else:
            awards = self.awards

        budget_applied_amount_difference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_applied_amount_difference, Unset):
            budget_applied_amount_difference = (
                self.budget_applied_amount_difference.to_dict()
            )

        co_managing_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.co_managing_organizations, Unset):
            co_managing_organizations = UNSET
        elif isinstance(self.co_managing_organizations, list):
            co_managing_organizations = []
            for (
                co_managing_organizations_type_0_item_data
            ) in self.co_managing_organizations:
                co_managing_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    co_managing_organizations_type_0_item_data, OrganizationRefType0
                ):
                    co_managing_organizations_type_0_item = (
                        co_managing_organizations_type_0_item_data.to_dict()
                    )
                else:
                    co_managing_organizations_type_0_item = (
                        co_managing_organizations_type_0_item_data
                    )
                co_managing_organizations.append(co_managing_organizations_type_0_item)

        else:
            co_managing_organizations = self.co_managing_organizations

        collaborators: list[dict[str, Any]] | None | Unset
        if isinstance(self.collaborators, Unset):
            collaborators = UNSET
        elif isinstance(self.collaborators, list):
            collaborators = []
            for collaborators_type_0_item_data in self.collaborators:
                collaborators_type_0_item = collaborators_type_0_item_data.to_dict()
                collaborators.append(collaborators_type_0_item)

        else:
            collaborators = self.collaborators

        descriptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.descriptions, Unset):
            descriptions = UNSET
        elif isinstance(self.descriptions, list):
            descriptions = []
            for descriptions_type_0_item_data in self.descriptions:
                descriptions_type_0_item = descriptions_type_0_item_data.to_dict()
                descriptions.append(descriptions_type_0_item)

        else:
            descriptions = self.descriptions

        expected_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_period, Unset):
            expected_period = self.expected_period.to_dict()

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

        funding_opportunity: dict[str, Any] | None | Unset
        if isinstance(self.funding_opportunity, Unset):
            funding_opportunity = UNSET
        elif isinstance(self.funding_opportunity, FundingOpportunityRefType0):
            funding_opportunity = self.funding_opportunity.to_dict()
        else:
            funding_opportunity = self.funding_opportunity

        nature_types: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.nature_types, Unset):
            nature_types = UNSET
        elif isinstance(self.nature_types, list):
            nature_types = []
            for nature_types_type_0_item_data in self.nature_types:
                nature_types_type_0_item: dict[str, Any] | None
                if isinstance(nature_types_type_0_item_data, ClassificationRefType0):
                    nature_types_type_0_item = nature_types_type_0_item_data.to_dict()
                else:
                    nature_types_type_0_item = nature_types_type_0_item_data
                nature_types.append(nature_types_type_0_item)

        else:
            nature_types = self.nature_types

        applications: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.applications, Unset):
            applications = UNSET
        elif isinstance(self.applications, list):
            applications = []
            for applications_type_0_item_data in self.applications:
                applications_type_0_item: dict[str, Any] | None
                if isinstance(applications_type_0_item_data, ApplicationRefType0):
                    applications_type_0_item = applications_type_0_item_data.to_dict()
                else:
                    applications_type_0_item = applications_type_0_item_data
                applications.append(applications_type_0_item)

        else:
            applications = self.applications

        short_title: dict[str, Any] | None | Unset
        if isinstance(self.short_title, Unset):
            short_title = UNSET
        elif isinstance(self.short_title, LocalizedStringType0):
            short_title = self.short_title.to_dict()
        else:
            short_title = self.short_title

        total_academic_ownership = self.total_academic_ownership

        total_applied_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_applied_amount, Unset):
            total_applied_amount = self.total_applied_amount.to_dict()

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        links: list[dict[str, Any]] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        else:
            links = self.links

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

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

        cluster: dict[str, Any] | None | Unset
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, ApplicationClusterRefType0):
            cluster = self.cluster.to_dict()
        else:
            cluster = self.cluster

        system_name = self.system_name

        award_date: None | str | Unset
        if isinstance(self.award_date, Unset):
            award_date = UNSET
        elif isinstance(self.award_date, datetime.date):
            award_date = self.award_date.isoformat()
        else:
            award_date = self.award_date

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

        funder_reply: str | Unset = UNSET
        if not isinstance(self.funder_reply, Unset):
            funder_reply = self.funder_reply.value

        pre_approver: dict[str, Any] | None | Unset
        if isinstance(self.pre_approver, Unset):
            pre_approver = UNSET
        elif isinstance(self.pre_approver, UserRefType0):
            pre_approver = self.pre_approver.to_dict()
        else:
            pre_approver = self.pre_approver

        rejected_date: None | str | Unset
        if isinstance(self.rejected_date, Unset):
            rejected_date = UNSET
        elif isinstance(self.rejected_date, datetime.date):
            rejected_date = self.rejected_date.isoformat()
        else:
            rejected_date = self.rejected_date

        submission_date: None | str | Unset
        if isinstance(self.submission_date, Unset):
            submission_date = UNSET
        elif isinstance(self.submission_date, datetime.date):
            submission_date = self.submission_date.isoformat()
        else:
            submission_date = self.submission_date

        submission_deadline: None | str | Unset
        if isinstance(self.submission_deadline, Unset):
            submission_deadline = UNSET
        elif isinstance(self.submission_deadline, datetime.date):
            submission_deadline = self.submission_deadline.isoformat()
        else:
            submission_deadline = self.submission_deadline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fundings": fundings,
                "organizations": organizations,
                "managingOrganization": managing_organization,
                "title": title,
                "type": type_,
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
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if applicants is not UNSET:
            field_dict["applicants"] = applicants
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if application_date is not UNSET:
            field_dict["applicationDate"] = application_date
        if awards is not UNSET:
            field_dict["awards"] = awards
        if budget_applied_amount_difference is not UNSET:
            field_dict["budgetAppliedAmountDifference"] = (
                budget_applied_amount_difference
            )
        if co_managing_organizations is not UNSET:
            field_dict["coManagingOrganizations"] = co_managing_organizations
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if expected_period is not UNSET:
            field_dict["expectedPeriod"] = expected_period
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if funding_opportunity is not UNSET:
            field_dict["fundingOpportunity"] = funding_opportunity
        if nature_types is not UNSET:
            field_dict["natureTypes"] = nature_types
        if applications is not UNSET:
            field_dict["applications"] = applications
        if short_title is not UNSET:
            field_dict["shortTitle"] = short_title
        if total_academic_ownership is not UNSET:
            field_dict["totalAcademicOwnership"] = total_academic_ownership
        if total_applied_amount is not UNSET:
            field_dict["totalAppliedAmount"] = total_applied_amount
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if links is not UNSET:
            field_dict["links"] = links
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if award_date is not UNSET:
            field_dict["awardDate"] = award_date
        if documents is not UNSET:
            field_dict["documents"] = documents
        if funder_reply is not UNSET:
            field_dict["funderReply"] = funder_reply
        if pre_approver is not UNSET:
            field_dict["preApprover"] = pre_approver
        if rejected_date is not UNSET:
            field_dict["rejectedDate"] = rejected_date
        if submission_date is not UNSET:
            field_dict["submissionDate"] = submission_date
        if submission_deadline is not UNSET:
            field_dict["submissionDeadline"] = submission_deadline

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_applicant_association import AbstractApplicantAssociation
        from ..models.application_cluster_ref_type_0 import ApplicationClusterRefType0
        from ..models.application_document import ApplicationDocument
        from ..models.application_funding_association import (
            ApplicationFundingAssociation,
        )
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_localized_value import ClassifiedLocalizedValue
        from ..models.collaborator_association import CollaboratorAssociation
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.date_range import DateRange
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.funding_opportunity_ref_type_0 import FundingOpportunityRefType0
        from ..models.identifier import Identifier
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.system_currency_amount import SystemCurrencyAmount
        from ..models.user_ref_type_0 import UserRefType0
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)
        fundings = []
        _fundings = d.pop("fundings")
        for fundings_item_data in _fundings:
            fundings_item = ApplicationFundingAssociation.from_dict(fundings_item_data)

            fundings.append(fundings_item)

        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:

            def _parse_organizations_item(data: object) -> None | OrganizationRefType0:
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

            organizations_item = _parse_organizations_item(organizations_item_data)

            organizations.append(organizations_item)

        def _parse_managing_organization(data: object) -> None | OrganizationRefType0:
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

        managing_organization = _parse_managing_organization(
            d.pop("managingOrganization")
        )

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

        def _parse_acronym(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acronym = _parse_acronym(d.pop("acronym", UNSET))

        _applicants = d.pop("applicants", UNSET)
        applicants: list[AbstractApplicantAssociation] | Unset = UNSET
        if _applicants is not UNSET:
            applicants = []
            for applicants_item_data in _applicants:
                applicants_item = AbstractApplicantAssociation.from_dict(
                    applicants_item_data
                )

                applicants.append(applicants_item)

        def _parse_external_organizations(
            data: object,
        ) -> list[ExternalOrganizationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_organizations_type_0 = []
                _external_organizations_type_0 = data
                for (
                    external_organizations_type_0_item_data
                ) in _external_organizations_type_0:

                    def _parse_external_organizations_type_0_item(
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

                    external_organizations_type_0_item = (
                        _parse_external_organizations_type_0_item(
                            external_organizations_type_0_item_data
                        )
                    )

                    external_organizations_type_0.append(
                        external_organizations_type_0_item
                    )

                return external_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalOrganizationRefType0 | None] | None | Unset, data)

        external_organizations = _parse_external_organizations(
            d.pop("externalOrganizations", UNSET)
        )

        _application_date = d.pop("applicationDate", UNSET)
        application_date: datetime.date | Unset
        if isinstance(_application_date, Unset):
            application_date = UNSET
        else:
            application_date = isoparse(_application_date).date()

        def _parse_awards(data: object) -> list[AwardRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                awards_type_0 = []
                _awards_type_0 = data
                for awards_type_0_item_data in _awards_type_0:

                    def _parse_awards_type_0_item(data: object) -> AwardRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_award_ref_type_0 = (
                                AwardRefType0.from_dict(data)
                            )

                            return componentsschemas_award_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(AwardRefType0 | None, data)

                    awards_type_0_item = _parse_awards_type_0_item(
                        awards_type_0_item_data
                    )

                    awards_type_0.append(awards_type_0_item)

                return awards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AwardRefType0 | None] | None | Unset, data)

        awards = _parse_awards(d.pop("awards", UNSET))

        _budget_applied_amount_difference = d.pop(
            "budgetAppliedAmountDifference", UNSET
        )
        budget_applied_amount_difference: SystemCurrencyAmount | Unset
        if isinstance(_budget_applied_amount_difference, Unset):
            budget_applied_amount_difference = UNSET
        else:
            budget_applied_amount_difference = SystemCurrencyAmount.from_dict(
                _budget_applied_amount_difference
            )

        def _parse_co_managing_organizations(
            data: object,
        ) -> list[None | OrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                co_managing_organizations_type_0 = []
                _co_managing_organizations_type_0 = data
                for (
                    co_managing_organizations_type_0_item_data
                ) in _co_managing_organizations_type_0:

                    def _parse_co_managing_organizations_type_0_item(
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

                    co_managing_organizations_type_0_item = (
                        _parse_co_managing_organizations_type_0_item(
                            co_managing_organizations_type_0_item_data
                        )
                    )

                    co_managing_organizations_type_0.append(
                        co_managing_organizations_type_0_item
                    )

                return co_managing_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | OrganizationRefType0] | None | Unset, data)

        co_managing_organizations = _parse_co_managing_organizations(
            d.pop("coManagingOrganizations", UNSET)
        )

        def _parse_collaborators(
            data: object,
        ) -> list[CollaboratorAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collaborators_type_0 = []
                _collaborators_type_0 = data
                for collaborators_type_0_item_data in _collaborators_type_0:
                    collaborators_type_0_item = CollaboratorAssociation.from_dict(
                        collaborators_type_0_item_data
                    )

                    collaborators_type_0.append(collaborators_type_0_item)

                return collaborators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CollaboratorAssociation] | None | Unset, data)

        collaborators = _parse_collaborators(d.pop("collaborators", UNSET))

        def _parse_descriptions(
            data: object,
        ) -> list[ClassifiedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                descriptions_type_0 = []
                _descriptions_type_0 = data
                for descriptions_type_0_item_data in _descriptions_type_0:
                    descriptions_type_0_item = ClassifiedLocalizedValue.from_dict(
                        descriptions_type_0_item_data
                    )

                    descriptions_type_0.append(descriptions_type_0_item)

                return descriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedLocalizedValue] | None | Unset, data)

        descriptions = _parse_descriptions(d.pop("descriptions", UNSET))

        _expected_period = d.pop("expectedPeriod", UNSET)
        expected_period: DateRange | Unset
        if isinstance(_expected_period, Unset):
            expected_period = UNSET
        else:
            expected_period = DateRange.from_dict(_expected_period)

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

        def _parse_funding_opportunity(
            data: object,
        ) -> FundingOpportunityRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_funding_opportunity_ref_type_0 = (
                    FundingOpportunityRefType0.from_dict(data)
                )

                return componentsschemas_funding_opportunity_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FundingOpportunityRefType0 | None | Unset, data)

        funding_opportunity = _parse_funding_opportunity(
            d.pop("fundingOpportunity", UNSET)
        )

        def _parse_nature_types(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nature_types_type_0 = []
                _nature_types_type_0 = data
                for nature_types_type_0_item_data in _nature_types_type_0:

                    def _parse_nature_types_type_0_item(
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

                    nature_types_type_0_item = _parse_nature_types_type_0_item(
                        nature_types_type_0_item_data
                    )

                    nature_types_type_0.append(nature_types_type_0_item)

                return nature_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        nature_types = _parse_nature_types(d.pop("natureTypes", UNSET))

        def _parse_applications(
            data: object,
        ) -> list[ApplicationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applications_type_0 = []
                _applications_type_0 = data
                for applications_type_0_item_data in _applications_type_0:

                    def _parse_applications_type_0_item(
                        data: object,
                    ) -> ApplicationRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_application_ref_type_0 = (
                                ApplicationRefType0.from_dict(data)
                            )

                            return componentsschemas_application_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ApplicationRefType0 | None, data)

                    applications_type_0_item = _parse_applications_type_0_item(
                        applications_type_0_item_data
                    )

                    applications_type_0.append(applications_type_0_item)

                return applications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplicationRefType0 | None] | None | Unset, data)

        applications = _parse_applications(d.pop("applications", UNSET))

        def _parse_short_title(data: object) -> LocalizedStringType0 | None | Unset:
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

        short_title = _parse_short_title(d.pop("shortTitle", UNSET))

        total_academic_ownership = d.pop("totalAcademicOwnership", UNSET)

        _total_applied_amount = d.pop("totalAppliedAmount", UNSET)
        total_applied_amount: SystemCurrencyAmount | Unset
        if isinstance(_total_applied_amount, Unset):
            total_applied_amount = UNSET
        else:
            total_applied_amount = SystemCurrencyAmount.from_dict(_total_applied_amount)

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        def _parse_links(data: object) -> list[Link] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = Link.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Link] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))

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

        def _parse_cluster(data: object) -> ApplicationClusterRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_application_cluster_ref_type_0 = (
                    ApplicationClusterRefType0.from_dict(data)
                )

                return componentsschemas_application_cluster_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicationClusterRefType0 | None | Unset, data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        system_name = d.pop("systemName", UNSET)

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

        def _parse_documents(data: object) -> list[ApplicationDocument] | None | Unset:
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
                    documents_type_0_item = ApplicationDocument.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplicationDocument] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

        _funder_reply = d.pop("funderReply", UNSET)
        funder_reply: AwardManagementApplicationFunderReply | Unset
        if isinstance(_funder_reply, Unset):
            funder_reply = UNSET
        else:
            funder_reply = AwardManagementApplicationFunderReply(_funder_reply)

        def _parse_pre_approver(data: object) -> None | Unset | UserRefType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                return componentsschemas_user_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRefType0, data)

        pre_approver = _parse_pre_approver(d.pop("preApprover", UNSET))

        def _parse_rejected_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_date_type_0 = isoparse(data).date()

                return rejected_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        rejected_date = _parse_rejected_date(d.pop("rejectedDate", UNSET))

        def _parse_submission_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submission_date_type_0 = isoparse(data).date()

                return submission_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        submission_date = _parse_submission_date(d.pop("submissionDate", UNSET))

        def _parse_submission_deadline(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submission_deadline_type_0 = isoparse(data).date()

                return submission_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        submission_deadline = _parse_submission_deadline(
            d.pop("submissionDeadline", UNSET)
        )

        award_management_application = cls(
            fundings=fundings,
            organizations=organizations,
            managing_organization=managing_organization,
            title=title,
            type_=type_,
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
            acronym=acronym,
            applicants=applicants,
            external_organizations=external_organizations,
            application_date=application_date,
            awards=awards,
            budget_applied_amount_difference=budget_applied_amount_difference,
            co_managing_organizations=co_managing_organizations,
            collaborators=collaborators,
            descriptions=descriptions,
            expected_period=expected_period,
            identifiers=identifiers,
            funding_opportunity=funding_opportunity,
            nature_types=nature_types,
            applications=applications,
            short_title=short_title,
            total_academic_ownership=total_academic_ownership,
            total_applied_amount=total_applied_amount,
            workflow=workflow,
            visibility=visibility,
            links=links,
            keyword_groups=keyword_groups,
            custom_defined_fields=custom_defined_fields,
            cluster=cluster,
            system_name=system_name,
            award_date=award_date,
            documents=documents,
            funder_reply=funder_reply,
            pre_approver=pre_approver,
            rejected_date=rejected_date,
            submission_date=submission_date,
            submission_deadline=submission_deadline,
        )

        award_management_application.additional_properties = d
        return award_management_application

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
