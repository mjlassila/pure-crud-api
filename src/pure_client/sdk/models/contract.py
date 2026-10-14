from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.contract_priority import ContractPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_classified_contract_person_association import (
        AbstractClassifiedContractPersonAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.contract_application_association import ContractApplicationAssociation
    from ..models.contract_award_association import ContractAwardAssociation
    from ..models.contract_collaborator_association import (
        ContractCollaboratorAssociation,
    )
    from ..models.contract_contract_association import ContractContractAssociation
    from ..models.contract_curtailed import ContractCurtailed
    from ..models.contract_document import ContractDocument
    from ..models.contract_extended import ContractExtended
    from ..models.date_range import DateRange
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.identifier import Identifier
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.user_ref_type_0 import UserRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Contract")


@_attrs_define
class Contract:
    """A contract

    Attributes:
        title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        persons (list[AbstractClassifiedContractPersonAssociation]): The persons associated with this contract
        visibility (Visibility): Visibility of an object
        type_ (ClassificationRefType0 | None): A reference to a classification value
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
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
        requirement (ClassificationRefType0 | None | Unset): A reference to a classification value
        priority (ContractPriority | Unset): Specifies the priority of the contract
        deadline (datetime.date | None | Unset): Contract deadline
        valid_dates (DateRange | Unset): A date range
        organizations (list[None | OrganizationRefType0] | Unset): A collection of organizational unit affiliations.
        applications (list[ContractApplicationAssociation] | Unset): Applications related to the contract
        awards (list[ContractAwardAssociation] | Unset): Awards related to the contract
        contracts (list[ContractContractAssociation] | Unset): Contracts related to the contract
        collaborators (list[ContractCollaboratorAssociation] | Unset): Contract collaborators
        extension (ContractExtended | Unset): Information about the contract extension.
        nature_types (list[ClassificationRefType0 | None] | None | Unset): Nature of activity types for the contract.
        external_organizations (list[ExternalOrganizationRefType0 | None] | Unset): A collection of organizational unit
            affiliations.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the contract.
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the contract.
        documents (list[ContractDocument] | Unset): The contract documents
        links (list[Link] | None | Unset): Links associated with the contract.
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions for the
            contract. Query the /contracts/allowed-description-types endpoint for allowed types.
        workflow (Workflow | Unset): Information about workflow
        responsible_users (list[None | UserRefType0] | Unset): The specific users chosen to be responsible for the
            content
        curtailed (ContractCurtailed | Unset): Information about the reason the contract is curtailed.
        system_name (str | Unset): The content system name
    """

    title: LocalizedStringType0 | None
    persons: list[AbstractClassifiedContractPersonAssociation]
    visibility: Visibility
    type_: ClassificationRefType0 | None
    managing_organization: None | OrganizationRefType0
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
    requirement: ClassificationRefType0 | None | Unset = UNSET
    priority: ContractPriority | Unset = UNSET
    deadline: datetime.date | None | Unset = UNSET
    valid_dates: DateRange | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | Unset = UNSET
    applications: list[ContractApplicationAssociation] | Unset = UNSET
    awards: list[ContractAwardAssociation] | Unset = UNSET
    contracts: list[ContractContractAssociation] | Unset = UNSET
    collaborators: list[ContractCollaboratorAssociation] | Unset = UNSET
    extension: ContractExtended | Unset = UNSET
    nature_types: list[ClassificationRefType0 | None] | None | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    documents: list[ContractDocument] | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    responsible_users: list[None | UserRefType0] | Unset = UNSET
    curtailed: ContractCurtailed | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.user_ref_type_0 import UserRefType0

        title: dict[str, Any] | None
        if isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        persons = []
        for persons_item_data in self.persons:
            persons_item = persons_item_data.to_dict()
            persons.append(persons_item)

        visibility = self.visibility.to_dict()

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        managing_organization: dict[str, Any] | None
        if isinstance(self.managing_organization, OrganizationRefType0):
            managing_organization = self.managing_organization.to_dict()
        else:
            managing_organization = self.managing_organization

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

        requirement: dict[str, Any] | None | Unset
        if isinstance(self.requirement, Unset):
            requirement = UNSET
        elif isinstance(self.requirement, ClassificationRefType0):
            requirement = self.requirement.to_dict()
        else:
            requirement = self.requirement

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        deadline: None | str | Unset
        if isinstance(self.deadline, Unset):
            deadline = UNSET
        elif isinstance(self.deadline, datetime.date):
            deadline = self.deadline.isoformat()
        else:
            deadline = self.deadline

        valid_dates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valid_dates, Unset):
            valid_dates = self.valid_dates.to_dict()

        organizations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item: dict[str, Any] | None
                if isinstance(organizations_item_data, OrganizationRefType0):
                    organizations_item = organizations_item_data.to_dict()
                else:
                    organizations_item = organizations_item_data
                organizations.append(organizations_item)

        applications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        awards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        contracts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contracts, Unset):
            contracts = []
            for contracts_item_data in self.contracts:
                contracts_item = contracts_item_data.to_dict()
                contracts.append(contracts_item)

        collaborators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collaborators, Unset):
            collaborators = []
            for collaborators_item_data in self.collaborators:
                collaborators_item = collaborators_item_data.to_dict()
                collaborators.append(collaborators_item)

        extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension, Unset):
            extension = self.extension.to_dict()

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

        external_organizations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.external_organizations, Unset):
            external_organizations = []
            for external_organizations_item_data in self.external_organizations:
                external_organizations_item: dict[str, Any] | None
                if isinstance(
                    external_organizations_item_data, ExternalOrganizationRefType0
                ):
                    external_organizations_item = (
                        external_organizations_item_data.to_dict()
                    )
                else:
                    external_organizations_item = external_organizations_item_data
                external_organizations.append(external_organizations_item)

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

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

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

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        responsible_users: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.responsible_users, Unset):
            responsible_users = []
            for responsible_users_item_data in self.responsible_users:
                responsible_users_item: dict[str, Any] | None
                if isinstance(responsible_users_item_data, UserRefType0):
                    responsible_users_item = responsible_users_item_data.to_dict()
                else:
                    responsible_users_item = responsible_users_item_data
                responsible_users.append(responsible_users_item)

        curtailed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.curtailed, Unset):
            curtailed = self.curtailed.to_dict()

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "persons": persons,
                "visibility": visibility,
                "type": type_,
                "managingOrganization": managing_organization,
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
        if requirement is not UNSET:
            field_dict["requirement"] = requirement
        if priority is not UNSET:
            field_dict["priority"] = priority
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if valid_dates is not UNSET:
            field_dict["validDates"] = valid_dates
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if applications is not UNSET:
            field_dict["applications"] = applications
        if awards is not UNSET:
            field_dict["awards"] = awards
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if extension is not UNSET:
            field_dict["extension"] = extension
        if nature_types is not UNSET:
            field_dict["natureTypes"] = nature_types
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if documents is not UNSET:
            field_dict["documents"] = documents
        if links is not UNSET:
            field_dict["links"] = links
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if responsible_users is not UNSET:
            field_dict["responsibleUsers"] = responsible_users
        if curtailed is not UNSET:
            field_dict["curtailed"] = curtailed
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_classified_contract_person_association import (
            AbstractClassifiedContractPersonAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.contract_application_association import (
            ContractApplicationAssociation,
        )
        from ..models.contract_award_association import ContractAwardAssociation
        from ..models.contract_collaborator_association import (
            ContractCollaboratorAssociation,
        )
        from ..models.contract_contract_association import ContractContractAssociation
        from ..models.contract_curtailed import ContractCurtailed
        from ..models.contract_document import ContractDocument
        from ..models.contract_extended import ContractExtended
        from ..models.date_range import DateRange
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.identifier import Identifier
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.user_ref_type_0 import UserRefType0
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)

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

        persons = []
        _persons = d.pop("persons")
        for persons_item_data in _persons:
            persons_item = AbstractClassifiedContractPersonAssociation.from_dict(
                persons_item_data
            )

            persons.append(persons_item)

        visibility = Visibility.from_dict(d.pop("visibility"))

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

        def _parse_requirement(data: object) -> ClassificationRefType0 | None | Unset:
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

        requirement = _parse_requirement(d.pop("requirement", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: ContractPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ContractPriority(_priority)

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

        _valid_dates = d.pop("validDates", UNSET)
        valid_dates: DateRange | Unset
        if isinstance(_valid_dates, Unset):
            valid_dates = UNSET
        else:
            valid_dates = DateRange.from_dict(_valid_dates)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[None | OrganizationRefType0] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:

                def _parse_organizations_item(
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

                organizations_item = _parse_organizations_item(organizations_item_data)

                organizations.append(organizations_item)

        _applications = d.pop("applications", UNSET)
        applications: list[ContractApplicationAssociation] | Unset = UNSET
        if _applications is not UNSET:
            applications = []
            for applications_item_data in _applications:
                applications_item = ContractApplicationAssociation.from_dict(
                    applications_item_data
                )

                applications.append(applications_item)

        _awards = d.pop("awards", UNSET)
        awards: list[ContractAwardAssociation] | Unset = UNSET
        if _awards is not UNSET:
            awards = []
            for awards_item_data in _awards:
                awards_item = ContractAwardAssociation.from_dict(awards_item_data)

                awards.append(awards_item)

        _contracts = d.pop("contracts", UNSET)
        contracts: list[ContractContractAssociation] | Unset = UNSET
        if _contracts is not UNSET:
            contracts = []
            for contracts_item_data in _contracts:
                contracts_item = ContractContractAssociation.from_dict(
                    contracts_item_data
                )

                contracts.append(contracts_item)

        _collaborators = d.pop("collaborators", UNSET)
        collaborators: list[ContractCollaboratorAssociation] | Unset = UNSET
        if _collaborators is not UNSET:
            collaborators = []
            for collaborators_item_data in _collaborators:
                collaborators_item = ContractCollaboratorAssociation.from_dict(
                    collaborators_item_data
                )

                collaborators.append(collaborators_item)

        _extension = d.pop("extension", UNSET)
        extension: ContractExtended | Unset
        if isinstance(_extension, Unset):
            extension = UNSET
        else:
            extension = ContractExtended.from_dict(_extension)

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

        _external_organizations = d.pop("externalOrganizations", UNSET)
        external_organizations: list[ExternalOrganizationRefType0 | None] | Unset = (
            UNSET
        )
        if _external_organizations is not UNSET:
            external_organizations = []
            for external_organizations_item_data in _external_organizations:

                def _parse_external_organizations_item(
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

                external_organizations_item = _parse_external_organizations_item(
                    external_organizations_item_data
                )

                external_organizations.append(external_organizations_item)

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

        _documents = d.pop("documents", UNSET)
        documents: list[ContractDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = ContractDocument.from_dict(documents_item_data)

                documents.append(documents_item)

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

        def _parse_descriptions(
            data: object,
        ) -> list[ClassifiedFormattedLocalizedValue] | None | Unset:
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
                    descriptions_type_0_item = (
                        ClassifiedFormattedLocalizedValue.from_dict(
                            descriptions_type_0_item_data
                        )
                    )

                    descriptions_type_0.append(descriptions_type_0_item)

                return descriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedFormattedLocalizedValue] | None | Unset, data)

        descriptions = _parse_descriptions(d.pop("descriptions", UNSET))

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        _responsible_users = d.pop("responsibleUsers", UNSET)
        responsible_users: list[None | UserRefType0] | Unset = UNSET
        if _responsible_users is not UNSET:
            responsible_users = []
            for responsible_users_item_data in _responsible_users:

                def _parse_responsible_users_item(data: object) -> None | UserRefType0:
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

                responsible_users_item = _parse_responsible_users_item(
                    responsible_users_item_data
                )

                responsible_users.append(responsible_users_item)

        _curtailed = d.pop("curtailed", UNSET)
        curtailed: ContractCurtailed | Unset
        if isinstance(_curtailed, Unset):
            curtailed = UNSET
        else:
            curtailed = ContractCurtailed.from_dict(_curtailed)

        system_name = d.pop("systemName", UNSET)

        contract = cls(
            title=title,
            persons=persons,
            visibility=visibility,
            type_=type_,
            managing_organization=managing_organization,
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
            requirement=requirement,
            priority=priority,
            deadline=deadline,
            valid_dates=valid_dates,
            organizations=organizations,
            applications=applications,
            awards=awards,
            contracts=contracts,
            collaborators=collaborators,
            extension=extension,
            nature_types=nature_types,
            external_organizations=external_organizations,
            identifiers=identifiers,
            keyword_groups=keyword_groups,
            documents=documents,
            links=links,
            descriptions=descriptions,
            workflow=workflow,
            responsible_users=responsible_users,
            curtailed=curtailed,
            system_name=system_name,
        )

        contract.additional_properties = d
        return contract

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
