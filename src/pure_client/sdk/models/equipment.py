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
    from ..models.abstract_equipment_person_association import (
        AbstractEquipmentPersonAssociation,
    )
    from ..models.activity_ref_type_0 import ActivityRefType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_address import ClassifiedAddress
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.classified_localized_value import ClassifiedLocalizedValue
    from ..models.classified_value import ClassifiedValue
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.equipment_data_set_association import EquipmentDataSetAssociation
    from ..models.equipment_details import EquipmentDetails
    from ..models.equipment_press_media_association import (
        EquipmentPressMediaAssociation,
    )
    from ..models.equipment_prize_association import EquipmentPrizeAssociation
    from ..models.equipment_project_association import EquipmentProjectAssociation
    from ..models.equipment_ref_type_0 import EquipmentRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.impact_ref_type_0 import ImpactRefType0
    from ..models.keyword_group import KeywordGroup
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.person_ref_type_0 import PersonRefType0
    from ..models.research_output_ref_type_0 import ResearchOutputRefType0
    from ..models.student_thesis_ref_type_0 import StudentThesisRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Equipment")


@_attrs_define
class Equipment:
    """An equipment known to an institution

    Attributes:
        title (FormattedLocalizedStringType0 | None): A set of localized strings that support formatting. Invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        organizations (list[None | OrganizationRefType0]): A collection of affiliated organizations
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
        loan_type (ClassificationRefType0 | None): A reference to a classification value
        visibility (Visibility): Visibility of an object
        type_ (ClassificationRefType0 | None): A reference to a classification value
        workflow (Workflow): Information about workflow
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
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions about or
            related to the equipment
        details (list[EquipmentDetails] | None | Unset): A collection of details bout or related to the equipment
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations
        contact_persons (list[None | PersonRefType0] | None | Unset): A collection of contact persons
        addresses (list[ClassifiedAddress] | None | Unset): A collection of classified addresses
        phone_numbers (list[ClassifiedValue] | None | Unset): A collection of classified phone numbers
        emails (list[ClassifiedValue] | None | Unset): A collection of classified e-mail addresses
        web_addresses (list[ClassifiedLocalizedValue] | None | Unset): A collection of classified web addresses
        loan_terms (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        press_media (list[EquipmentPressMediaAssociation] | None | Unset): A collection of related press media
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        persons (list[AbstractEquipmentPersonAssociation] | None | Unset): The persons that the equipment is associated
            with
        research_output_relations (list[None | ResearchOutputRefType0] | None | Unset): A collection of research output
            relations
        impact_relations (list[ImpactRefType0 | None] | None | Unset): A collection of impacts relations
        student_thesis_relations (list[None | StudentThesisRefType0] | None | Unset): A collection of student thesis
            relations
        activity_relations (list[ActivityRefType0 | None] | None | Unset): A collection of activity relations
        prizes (list[EquipmentPrizeAssociation] | None | Unset): A collection of related prizes
        projects (list[EquipmentProjectAssociation] | None | Unset): A collection of related projects
        datasets (list[EquipmentDataSetAssociation] | None | Unset): A collection of related data sets
        parents (list[EquipmentRefType0 | None] | None | Unset): A collection of parent equipments
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the Equipment.
        system_name (str | Unset): The content system name
    """

    title: FormattedLocalizedStringType0 | None
    organizations: list[None | OrganizationRefType0]
    managing_organization: None | OrganizationRefType0
    loan_type: ClassificationRefType0 | None
    visibility: Visibility
    type_: ClassificationRefType0 | None
    workflow: Workflow
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
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    details: list[EquipmentDetails] | None | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    contact_persons: list[None | PersonRefType0] | None | Unset = UNSET
    addresses: list[ClassifiedAddress] | None | Unset = UNSET
    phone_numbers: list[ClassifiedValue] | None | Unset = UNSET
    emails: list[ClassifiedValue] | None | Unset = UNSET
    web_addresses: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    loan_terms: FormattedLocalizedStringType0 | None | Unset = UNSET
    press_media: list[EquipmentPressMediaAssociation] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    persons: list[AbstractEquipmentPersonAssociation] | None | Unset = UNSET
    research_output_relations: list[None | ResearchOutputRefType0] | None | Unset = (
        UNSET
    )
    impact_relations: list[ImpactRefType0 | None] | None | Unset = UNSET
    student_thesis_relations: list[None | StudentThesisRefType0] | None | Unset = UNSET
    activity_relations: list[ActivityRefType0 | None] | None | Unset = UNSET
    prizes: list[EquipmentPrizeAssociation] | None | Unset = UNSET
    projects: list[EquipmentProjectAssociation] | None | Unset = UNSET
    datasets: list[EquipmentDataSetAssociation] | None | Unset = UNSET
    parents: list[EquipmentRefType0 | None] | None | Unset = UNSET
    category: ClassificationRefType0 | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0

        title: dict[str, Any] | None
        if isinstance(self.title, FormattedLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

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

        loan_type: dict[str, Any] | None
        if isinstance(self.loan_type, ClassificationRefType0):
            loan_type = self.loan_type.to_dict()
        else:
            loan_type = self.loan_type

        visibility = self.visibility.to_dict()

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        workflow = self.workflow.to_dict()

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

        details: list[dict[str, Any]] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = []
            for details_type_0_item_data in self.details:
                details_type_0_item = details_type_0_item_data.to_dict()
                details.append(details_type_0_item)

        else:
            details = self.details

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

        contact_persons: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.contact_persons, Unset):
            contact_persons = UNSET
        elif isinstance(self.contact_persons, list):
            contact_persons = []
            for contact_persons_type_0_item_data in self.contact_persons:
                contact_persons_type_0_item: dict[str, Any] | None
                if isinstance(contact_persons_type_0_item_data, PersonRefType0):
                    contact_persons_type_0_item = (
                        contact_persons_type_0_item_data.to_dict()
                    )
                else:
                    contact_persons_type_0_item = contact_persons_type_0_item_data
                contact_persons.append(contact_persons_type_0_item)

        else:
            contact_persons = self.contact_persons

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

        loan_terms: dict[str, Any] | None | Unset
        if isinstance(self.loan_terms, Unset):
            loan_terms = UNSET
        elif isinstance(self.loan_terms, FormattedLocalizedStringType0):
            loan_terms = self.loan_terms.to_dict()
        else:
            loan_terms = self.loan_terms

        press_media: list[dict[str, Any]] | None | Unset
        if isinstance(self.press_media, Unset):
            press_media = UNSET
        elif isinstance(self.press_media, list):
            press_media = []
            for press_media_type_0_item_data in self.press_media:
                press_media_type_0_item = press_media_type_0_item_data.to_dict()
                press_media.append(press_media_type_0_item)

        else:
            press_media = self.press_media

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

        images: list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        persons: list[dict[str, Any]] | None | Unset
        if isinstance(self.persons, Unset):
            persons = UNSET
        elif isinstance(self.persons, list):
            persons = []
            for persons_type_0_item_data in self.persons:
                persons_type_0_item = persons_type_0_item_data.to_dict()
                persons.append(persons_type_0_item)

        else:
            persons = self.persons

        research_output_relations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.research_output_relations, Unset):
            research_output_relations = UNSET
        elif isinstance(self.research_output_relations, list):
            research_output_relations = []
            for (
                research_output_relations_type_0_item_data
            ) in self.research_output_relations:
                research_output_relations_type_0_item: dict[str, Any] | None
                if isinstance(
                    research_output_relations_type_0_item_data, ResearchOutputRefType0
                ):
                    research_output_relations_type_0_item = (
                        research_output_relations_type_0_item_data.to_dict()
                    )
                else:
                    research_output_relations_type_0_item = (
                        research_output_relations_type_0_item_data
                    )
                research_output_relations.append(research_output_relations_type_0_item)

        else:
            research_output_relations = self.research_output_relations

        impact_relations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.impact_relations, Unset):
            impact_relations = UNSET
        elif isinstance(self.impact_relations, list):
            impact_relations = []
            for impact_relations_type_0_item_data in self.impact_relations:
                impact_relations_type_0_item: dict[str, Any] | None
                if isinstance(impact_relations_type_0_item_data, ImpactRefType0):
                    impact_relations_type_0_item = (
                        impact_relations_type_0_item_data.to_dict()
                    )
                else:
                    impact_relations_type_0_item = impact_relations_type_0_item_data
                impact_relations.append(impact_relations_type_0_item)

        else:
            impact_relations = self.impact_relations

        student_thesis_relations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.student_thesis_relations, Unset):
            student_thesis_relations = UNSET
        elif isinstance(self.student_thesis_relations, list):
            student_thesis_relations = []
            for (
                student_thesis_relations_type_0_item_data
            ) in self.student_thesis_relations:
                student_thesis_relations_type_0_item: dict[str, Any] | None
                if isinstance(
                    student_thesis_relations_type_0_item_data, StudentThesisRefType0
                ):
                    student_thesis_relations_type_0_item = (
                        student_thesis_relations_type_0_item_data.to_dict()
                    )
                else:
                    student_thesis_relations_type_0_item = (
                        student_thesis_relations_type_0_item_data
                    )
                student_thesis_relations.append(student_thesis_relations_type_0_item)

        else:
            student_thesis_relations = self.student_thesis_relations

        activity_relations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.activity_relations, Unset):
            activity_relations = UNSET
        elif isinstance(self.activity_relations, list):
            activity_relations = []
            for activity_relations_type_0_item_data in self.activity_relations:
                activity_relations_type_0_item: dict[str, Any] | None
                if isinstance(activity_relations_type_0_item_data, ActivityRefType0):
                    activity_relations_type_0_item = (
                        activity_relations_type_0_item_data.to_dict()
                    )
                else:
                    activity_relations_type_0_item = activity_relations_type_0_item_data
                activity_relations.append(activity_relations_type_0_item)

        else:
            activity_relations = self.activity_relations

        prizes: list[dict[str, Any]] | None | Unset
        if isinstance(self.prizes, Unset):
            prizes = UNSET
        elif isinstance(self.prizes, list):
            prizes = []
            for prizes_type_0_item_data in self.prizes:
                prizes_type_0_item = prizes_type_0_item_data.to_dict()
                prizes.append(prizes_type_0_item)

        else:
            prizes = self.prizes

        projects: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        datasets: list[dict[str, Any]] | None | Unset
        if isinstance(self.datasets, Unset):
            datasets = UNSET
        elif isinstance(self.datasets, list):
            datasets = []
            for datasets_type_0_item_data in self.datasets:
                datasets_type_0_item = datasets_type_0_item_data.to_dict()
                datasets.append(datasets_type_0_item)

        else:
            datasets = self.datasets

        parents: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.parents, Unset):
            parents = UNSET
        elif isinstance(self.parents, list):
            parents = []
            for parents_type_0_item_data in self.parents:
                parents_type_0_item: dict[str, Any] | None
                if isinstance(parents_type_0_item_data, EquipmentRefType0):
                    parents_type_0_item = parents_type_0_item_data.to_dict()
                else:
                    parents_type_0_item = parents_type_0_item_data
                parents.append(parents_type_0_item)

        else:
            parents = self.parents

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "organizations": organizations,
                "managingOrganization": managing_organization,
                "loanType": loan_type,
                "visibility": visibility,
                "type": type_,
                "workflow": workflow,
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
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if details is not UNSET:
            field_dict["details"] = details
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if contact_persons is not UNSET:
            field_dict["contactPersons"] = contact_persons
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if emails is not UNSET:
            field_dict["emails"] = emails
        if web_addresses is not UNSET:
            field_dict["webAddresses"] = web_addresses
        if loan_terms is not UNSET:
            field_dict["loanTerms"] = loan_terms
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if images is not UNSET:
            field_dict["images"] = images
        if persons is not UNSET:
            field_dict["persons"] = persons
        if research_output_relations is not UNSET:
            field_dict["researchOutputRelations"] = research_output_relations
        if impact_relations is not UNSET:
            field_dict["impactRelations"] = impact_relations
        if student_thesis_relations is not UNSET:
            field_dict["studentThesisRelations"] = student_thesis_relations
        if activity_relations is not UNSET:
            field_dict["activityRelations"] = activity_relations
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if projects is not UNSET:
            field_dict["projects"] = projects
        if datasets is not UNSET:
            field_dict["datasets"] = datasets
        if parents is not UNSET:
            field_dict["parents"] = parents
        if category is not UNSET:
            field_dict["category"] = category
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_equipment_person_association import (
            AbstractEquipmentPersonAssociation,
        )
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_address import ClassifiedAddress
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.classified_localized_value import ClassifiedLocalizedValue
        from ..models.classified_value import ClassifiedValue
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.equipment_data_set_association import EquipmentDataSetAssociation
        from ..models.equipment_details import EquipmentDetails
        from ..models.equipment_press_media_association import (
            EquipmentPressMediaAssociation,
        )
        from ..models.equipment_prize_association import EquipmentPrizeAssociation
        from ..models.equipment_project_association import EquipmentProjectAssociation
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.keyword_group import KeywordGroup
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)

        def _parse_title(data: object) -> FormattedLocalizedStringType0 | None:
            if data is None:
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
            return cast(FormattedLocalizedStringType0 | None, data)

        title = _parse_title(d.pop("title"))

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

        def _parse_loan_type(data: object) -> ClassificationRefType0 | None:
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

        loan_type = _parse_loan_type(d.pop("loanType"))

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

        workflow = Workflow.from_dict(d.pop("workflow"))

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

        def _parse_details(data: object) -> list[EquipmentDetails] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = []
                _details_type_0 = data
                for details_type_0_item_data in _details_type_0:
                    details_type_0_item = EquipmentDetails.from_dict(
                        details_type_0_item_data
                    )

                    details_type_0.append(details_type_0_item)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentDetails] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

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

        def _parse_contact_persons(
            data: object,
        ) -> list[None | PersonRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contact_persons_type_0 = []
                _contact_persons_type_0 = data
                for contact_persons_type_0_item_data in _contact_persons_type_0:

                    def _parse_contact_persons_type_0_item(
                        data: object,
                    ) -> None | PersonRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_person_ref_type_0 = (
                                PersonRefType0.from_dict(data)
                            )

                            return componentsschemas_person_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | PersonRefType0, data)

                    contact_persons_type_0_item = _parse_contact_persons_type_0_item(
                        contact_persons_type_0_item_data
                    )

                    contact_persons_type_0.append(contact_persons_type_0_item)

                return contact_persons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | PersonRefType0] | None | Unset, data)

        contact_persons = _parse_contact_persons(d.pop("contactPersons", UNSET))

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

        def _parse_loan_terms(
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

        loan_terms = _parse_loan_terms(d.pop("loanTerms", UNSET))

        def _parse_press_media(
            data: object,
        ) -> list[EquipmentPressMediaAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                press_media_type_0 = []
                _press_media_type_0 = data
                for press_media_type_0_item_data in _press_media_type_0:
                    press_media_type_0_item = EquipmentPressMediaAssociation.from_dict(
                        press_media_type_0_item_data
                    )

                    press_media_type_0.append(press_media_type_0_item)

                return press_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentPressMediaAssociation] | None | Unset, data)

        press_media = _parse_press_media(d.pop("pressMedia", UNSET))

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

        def _parse_images(data: object) -> list[ImageFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = ImageFile.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageFile] | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_persons(
            data: object,
        ) -> list[AbstractEquipmentPersonAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                persons_type_0 = []
                _persons_type_0 = data
                for persons_type_0_item_data in _persons_type_0:
                    persons_type_0_item = AbstractEquipmentPersonAssociation.from_dict(
                        persons_type_0_item_data
                    )

                    persons_type_0.append(persons_type_0_item)

                return persons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AbstractEquipmentPersonAssociation] | None | Unset, data)

        persons = _parse_persons(d.pop("persons", UNSET))

        def _parse_research_output_relations(
            data: object,
        ) -> list[None | ResearchOutputRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                research_output_relations_type_0 = []
                _research_output_relations_type_0 = data
                for (
                    research_output_relations_type_0_item_data
                ) in _research_output_relations_type_0:

                    def _parse_research_output_relations_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_ref_type_0 = (
                                ResearchOutputRefType0.from_dict(data)
                            )

                            return componentsschemas_research_output_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ResearchOutputRefType0, data)

                    research_output_relations_type_0_item = (
                        _parse_research_output_relations_type_0_item(
                            research_output_relations_type_0_item_data
                        )
                    )

                    research_output_relations_type_0.append(
                        research_output_relations_type_0_item
                    )

                return research_output_relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | ResearchOutputRefType0] | None | Unset, data)

        research_output_relations = _parse_research_output_relations(
            d.pop("researchOutputRelations", UNSET)
        )

        def _parse_impact_relations(
            data: object,
        ) -> list[ImpactRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                impact_relations_type_0 = []
                _impact_relations_type_0 = data
                for impact_relations_type_0_item_data in _impact_relations_type_0:

                    def _parse_impact_relations_type_0_item(
                        data: object,
                    ) -> ImpactRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_impact_ref_type_0 = (
                                ImpactRefType0.from_dict(data)
                            )

                            return componentsschemas_impact_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ImpactRefType0 | None, data)

                    impact_relations_type_0_item = _parse_impact_relations_type_0_item(
                        impact_relations_type_0_item_data
                    )

                    impact_relations_type_0.append(impact_relations_type_0_item)

                return impact_relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImpactRefType0 | None] | None | Unset, data)

        impact_relations = _parse_impact_relations(d.pop("impactRelations", UNSET))

        def _parse_student_thesis_relations(
            data: object,
        ) -> list[None | StudentThesisRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                student_thesis_relations_type_0 = []
                _student_thesis_relations_type_0 = data
                for (
                    student_thesis_relations_type_0_item_data
                ) in _student_thesis_relations_type_0:

                    def _parse_student_thesis_relations_type_0_item(
                        data: object,
                    ) -> None | StudentThesisRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_student_thesis_ref_type_0 = (
                                StudentThesisRefType0.from_dict(data)
                            )

                            return componentsschemas_student_thesis_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | StudentThesisRefType0, data)

                    student_thesis_relations_type_0_item = (
                        _parse_student_thesis_relations_type_0_item(
                            student_thesis_relations_type_0_item_data
                        )
                    )

                    student_thesis_relations_type_0.append(
                        student_thesis_relations_type_0_item
                    )

                return student_thesis_relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | StudentThesisRefType0] | None | Unset, data)

        student_thesis_relations = _parse_student_thesis_relations(
            d.pop("studentThesisRelations", UNSET)
        )

        def _parse_activity_relations(
            data: object,
        ) -> list[ActivityRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                activity_relations_type_0 = []
                _activity_relations_type_0 = data
                for activity_relations_type_0_item_data in _activity_relations_type_0:

                    def _parse_activity_relations_type_0_item(
                        data: object,
                    ) -> ActivityRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_activity_ref_type_0 = (
                                ActivityRefType0.from_dict(data)
                            )

                            return componentsschemas_activity_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ActivityRefType0 | None, data)

                    activity_relations_type_0_item = (
                        _parse_activity_relations_type_0_item(
                            activity_relations_type_0_item_data
                        )
                    )

                    activity_relations_type_0.append(activity_relations_type_0_item)

                return activity_relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityRefType0 | None] | None | Unset, data)

        activity_relations = _parse_activity_relations(
            d.pop("activityRelations", UNSET)
        )

        def _parse_prizes(
            data: object,
        ) -> list[EquipmentPrizeAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prizes_type_0 = []
                _prizes_type_0 = data
                for prizes_type_0_item_data in _prizes_type_0:
                    prizes_type_0_item = EquipmentPrizeAssociation.from_dict(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentPrizeAssociation] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[EquipmentProjectAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in _projects_type_0:
                    projects_type_0_item = EquipmentProjectAssociation.from_dict(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentProjectAssociation] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_datasets(
            data: object,
        ) -> list[EquipmentDataSetAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                datasets_type_0 = []
                _datasets_type_0 = data
                for datasets_type_0_item_data in _datasets_type_0:
                    datasets_type_0_item = EquipmentDataSetAssociation.from_dict(
                        datasets_type_0_item_data
                    )

                    datasets_type_0.append(datasets_type_0_item)

                return datasets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentDataSetAssociation] | None | Unset, data)

        datasets = _parse_datasets(d.pop("datasets", UNSET))

        def _parse_parents(
            data: object,
        ) -> list[EquipmentRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parents_type_0 = []
                _parents_type_0 = data
                for parents_type_0_item_data in _parents_type_0:

                    def _parse_parents_type_0_item(
                        data: object,
                    ) -> EquipmentRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_equipment_ref_type_0 = (
                                EquipmentRefType0.from_dict(data)
                            )

                            return componentsschemas_equipment_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(EquipmentRefType0 | None, data)

                    parents_type_0_item = _parse_parents_type_0_item(
                        parents_type_0_item_data
                    )

                    parents_type_0.append(parents_type_0_item)

                return parents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentRefType0 | None] | None | Unset, data)

        parents = _parse_parents(d.pop("parents", UNSET))

        def _parse_category(data: object) -> ClassificationRefType0 | None | Unset:
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

        category = _parse_category(d.pop("category", UNSET))

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

        system_name = d.pop("systemName", UNSET)

        equipment = cls(
            title=title,
            organizations=organizations,
            managing_organization=managing_organization,
            loan_type=loan_type,
            visibility=visibility,
            type_=type_,
            workflow=workflow,
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
            descriptions=descriptions,
            details=details,
            external_organizations=external_organizations,
            contact_persons=contact_persons,
            addresses=addresses,
            phone_numbers=phone_numbers,
            emails=emails,
            web_addresses=web_addresses,
            loan_terms=loan_terms,
            press_media=press_media,
            keyword_groups=keyword_groups,
            images=images,
            persons=persons,
            research_output_relations=research_output_relations,
            impact_relations=impact_relations,
            student_thesis_relations=student_thesis_relations,
            activity_relations=activity_relations,
            prizes=prizes,
            projects=projects,
            datasets=datasets,
            parents=parents,
            category=category,
            custom_defined_fields=custom_defined_fields,
            identifiers=identifiers,
            system_name=system_name,
        )

        equipment.additional_properties = d
        return equipment

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
