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
    from ..models.abstract_data_set_contributor_association import (
        AbstractDataSetContributorAssociation,
    )
    from ..models.abstract_data_set_person_association import (
        AbstractDataSetPersonAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_localized_value import ClassifiedLocalizedValue
    from ..models.compound_date_range import CompoundDateRange
    from ..models.compound_date_type_0 import CompoundDateType0
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.data_set_activity_association import DataSetActivityAssociation
    from ..models.data_set_association import DataSetAssociation
    from ..models.data_set_document import DataSetDocument
    from ..models.data_set_doi import DataSetDoi
    from ..models.data_set_equipment_association import DataSetEquipmentAssociation
    from ..models.data_set_geo_location import DataSetGeoLocation
    from ..models.data_set_impact_association import DataSetImpactAssociation
    from ..models.data_set_legal_condition import DataSetLegalCondition
    from ..models.data_set_physical_data import DataSetPhysicalData
    from ..models.data_set_press_media_association import DataSetPressMediaAssociation
    from ..models.data_set_prize_association import DataSetPrizeAssociation
    from ..models.data_set_project_association import DataSetProjectAssociation
    from ..models.data_set_research_output_association import (
        DataSetResearchOutputAssociation,
    )
    from ..models.data_set_student_thesis_association import (
        DataSetStudentThesisAssociation,
    )
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.funding_details import FundingDetails
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.open_access import OpenAccess
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.person_ref_type_0 import PersonRefType0
    from ..models.publisher_ref_type_0 import PublisherRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="DataSet")


@_attrs_define
class DataSet:
    """A dataset

    Attributes:
        title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
        type_ (ClassificationRefType0 | None): A reference to a classification value
        publisher (None | PublisherRefType0): A reference to a publisher
        persons (list[AbstractDataSetPersonAssociation]): DEPRECATED - use contributors instead. The persons that the
            dataset is associated with
        visibility (Visibility): Visibility of an object
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
        descriptions (list[ClassifiedLocalizedValue] | None | Unset): A collection of descriptions.
        nature_types (list[ClassificationRefType0 | None] | None | Unset): Nature of activity types for the dataset.
        temporal_coverage_period (CompoundDateRange | Unset): A date range of that can be defined by only year, year and
            month or a full date
        data_production_period (CompoundDateRange | Unset): A date range of that can be defined by only year, year and
            month or a full date
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
        geo_location (DataSetGeoLocation | Unset): A data set geo-location.
        contributors (list[AbstractDataSetContributorAssociation] | Unset): The contributors that the dataset is
            associated with
        total_number_of_authors (int | None | Unset): The total number of authors from author collaborations.
        doi (DataSetDoi | Unset): A DOI.
        documents (list[DataSetDocument] | None | Unset): A collection of documents.
        physical_data (list[DataSetPhysicalData] | None | Unset): A collection of physical data.
        contact_person (None | PersonRefType0 | Unset): A reference to a person internal to the institution
        legal_conditions (list[DataSetLegalCondition] | None | Unset): A collection of legal conditions.
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organizational unit
            affiliations.
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        publication_available_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and
            month or a full date
        open_access (OpenAccess | Unset): Open Access information.
        open_aire_compliant (bool | Unset): OpenAire Compliancy.
        license_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        data_sets (list[DataSetAssociation] | None | Unset): A collection of related datasets.
        projects (list[DataSetProjectAssociation] | None | Unset): A collection of related projects.
        research_outputs (list[DataSetResearchOutputAssociation] | None | Unset): A collection of related research
            outputs.
        activities (list[DataSetActivityAssociation] | None | Unset): A collection of related activities.
        press_media (list[DataSetPressMediaAssociation] | None | Unset): A collection of related press media.
        student_theses (list[DataSetStudentThesisAssociation] | None | Unset): A collection of related student theses.
        impacts (list[DataSetImpactAssociation] | None | Unset): A collection of related impacts.
        prizes (list[DataSetPrizeAssociation] | None | Unset): A collection of related prizes.
        equipment (list[DataSetEquipmentAssociation] | None | Unset): A collection of related equipment.
        links (list[Link] | None | Unset): A collection of links.
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        funding_text (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        funding_details (list[FundingDetails] | None | Unset): The funding details for the dataset
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        workflow (Workflow | Unset): Information about workflow
        system_name (str | Unset): The content system name
    """

    title: LocalizedStringType0 | None
    managing_organization: None | OrganizationRefType0
    type_: ClassificationRefType0 | None
    publisher: None | PublisherRefType0
    persons: list[AbstractDataSetPersonAssociation]
    visibility: Visibility
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
    descriptions: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    nature_types: list[ClassificationRefType0 | None] | None | Unset = UNSET
    temporal_coverage_period: CompoundDateRange | Unset = UNSET
    data_production_period: CompoundDateRange | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    geo_location: DataSetGeoLocation | Unset = UNSET
    contributors: list[AbstractDataSetContributorAssociation] | Unset = UNSET
    total_number_of_authors: int | None | Unset = UNSET
    doi: DataSetDoi | Unset = UNSET
    documents: list[DataSetDocument] | None | Unset = UNSET
    physical_data: list[DataSetPhysicalData] | None | Unset = UNSET
    contact_person: None | PersonRefType0 | Unset = UNSET
    legal_conditions: list[DataSetLegalCondition] | None | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    publication_available_date: CompoundDateType0 | None | Unset = UNSET
    open_access: OpenAccess | Unset = UNSET
    open_aire_compliant: bool | Unset = UNSET
    license_: ClassificationRefType0 | None | Unset = UNSET
    data_sets: list[DataSetAssociation] | None | Unset = UNSET
    projects: list[DataSetProjectAssociation] | None | Unset = UNSET
    research_outputs: list[DataSetResearchOutputAssociation] | None | Unset = UNSET
    activities: list[DataSetActivityAssociation] | None | Unset = UNSET
    press_media: list[DataSetPressMediaAssociation] | None | Unset = UNSET
    student_theses: list[DataSetStudentThesisAssociation] | None | Unset = UNSET
    impacts: list[DataSetImpactAssociation] | None | Unset = UNSET
    prizes: list[DataSetPrizeAssociation] | None | Unset = UNSET
    equipment: list[DataSetEquipmentAssociation] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    funding_text: LocalizedStringType0 | None | Unset = UNSET
    funding_details: list[FundingDetails] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0
        from ..models.publisher_ref_type_0 import PublisherRefType0

        title: dict[str, Any] | None
        if isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        managing_organization: dict[str, Any] | None
        if isinstance(self.managing_organization, OrganizationRefType0):
            managing_organization = self.managing_organization.to_dict()
        else:
            managing_organization = self.managing_organization

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        publisher: dict[str, Any] | None
        if isinstance(self.publisher, PublisherRefType0):
            publisher = self.publisher.to_dict()
        else:
            publisher = self.publisher

        persons = []
        for persons_item_data in self.persons:
            persons_item = persons_item_data.to_dict()
            persons.append(persons_item)

        visibility = self.visibility.to_dict()

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

        temporal_coverage_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.temporal_coverage_period, Unset):
            temporal_coverage_period = self.temporal_coverage_period.to_dict()

        data_production_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_production_period, Unset):
            data_production_period = self.data_production_period.to_dict()

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

        geo_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geo_location, Unset):
            geo_location = self.geo_location.to_dict()

        contributors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contributors, Unset):
            contributors = []
            for contributors_item_data in self.contributors:
                contributors_item = contributors_item_data.to_dict()
                contributors.append(contributors_item)

        total_number_of_authors: int | None | Unset
        if isinstance(self.total_number_of_authors, Unset):
            total_number_of_authors = UNSET
        else:
            total_number_of_authors = self.total_number_of_authors

        doi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doi, Unset):
            doi = self.doi.to_dict()

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

        physical_data: list[dict[str, Any]] | None | Unset
        if isinstance(self.physical_data, Unset):
            physical_data = UNSET
        elif isinstance(self.physical_data, list):
            physical_data = []
            for physical_data_type_0_item_data in self.physical_data:
                physical_data_type_0_item = physical_data_type_0_item_data.to_dict()
                physical_data.append(physical_data_type_0_item)

        else:
            physical_data = self.physical_data

        contact_person: dict[str, Any] | None | Unset
        if isinstance(self.contact_person, Unset):
            contact_person = UNSET
        elif isinstance(self.contact_person, PersonRefType0):
            contact_person = self.contact_person.to_dict()
        else:
            contact_person = self.contact_person

        legal_conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.legal_conditions, Unset):
            legal_conditions = UNSET
        elif isinstance(self.legal_conditions, list):
            legal_conditions = []
            for legal_conditions_type_0_item_data in self.legal_conditions:
                legal_conditions_type_0_item = (
                    legal_conditions_type_0_item_data.to_dict()
                )
                legal_conditions.append(legal_conditions_type_0_item)

        else:
            legal_conditions = self.legal_conditions

        organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item: dict[str, Any] | None
                if isinstance(organizations_type_0_item_data, OrganizationRefType0):
                    organizations_type_0_item = organizations_type_0_item_data.to_dict()
                else:
                    organizations_type_0_item = organizations_type_0_item_data
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

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

        publication_available_date: dict[str, Any] | None | Unset
        if isinstance(self.publication_available_date, Unset):
            publication_available_date = UNSET
        elif isinstance(self.publication_available_date, CompoundDateType0):
            publication_available_date = self.publication_available_date.to_dict()
        else:
            publication_available_date = self.publication_available_date

        open_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_access, Unset):
            open_access = self.open_access.to_dict()

        open_aire_compliant = self.open_aire_compliant

        license_: dict[str, Any] | None | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        elif isinstance(self.license_, ClassificationRefType0):
            license_ = self.license_.to_dict()
        else:
            license_ = self.license_

        data_sets: list[dict[str, Any]] | None | Unset
        if isinstance(self.data_sets, Unset):
            data_sets = UNSET
        elif isinstance(self.data_sets, list):
            data_sets = []
            for data_sets_type_0_item_data in self.data_sets:
                data_sets_type_0_item = data_sets_type_0_item_data.to_dict()
                data_sets.append(data_sets_type_0_item)

        else:
            data_sets = self.data_sets

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

        research_outputs: list[dict[str, Any]] | None | Unset
        if isinstance(self.research_outputs, Unset):
            research_outputs = UNSET
        elif isinstance(self.research_outputs, list):
            research_outputs = []
            for research_outputs_type_0_item_data in self.research_outputs:
                research_outputs_type_0_item = (
                    research_outputs_type_0_item_data.to_dict()
                )
                research_outputs.append(research_outputs_type_0_item)

        else:
            research_outputs = self.research_outputs

        activities: list[dict[str, Any]] | None | Unset
        if isinstance(self.activities, Unset):
            activities = UNSET
        elif isinstance(self.activities, list):
            activities = []
            for activities_type_0_item_data in self.activities:
                activities_type_0_item = activities_type_0_item_data.to_dict()
                activities.append(activities_type_0_item)

        else:
            activities = self.activities

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

        student_theses: list[dict[str, Any]] | None | Unset
        if isinstance(self.student_theses, Unset):
            student_theses = UNSET
        elif isinstance(self.student_theses, list):
            student_theses = []
            for student_theses_type_0_item_data in self.student_theses:
                student_theses_type_0_item = student_theses_type_0_item_data.to_dict()
                student_theses.append(student_theses_type_0_item)

        else:
            student_theses = self.student_theses

        impacts: list[dict[str, Any]] | None | Unset
        if isinstance(self.impacts, Unset):
            impacts = UNSET
        elif isinstance(self.impacts, list):
            impacts = []
            for impacts_type_0_item_data in self.impacts:
                impacts_type_0_item = impacts_type_0_item_data.to_dict()
                impacts.append(impacts_type_0_item)

        else:
            impacts = self.impacts

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

        equipment: list[dict[str, Any]] | None | Unset
        if isinstance(self.equipment, Unset):
            equipment = UNSET
        elif isinstance(self.equipment, list):
            equipment = []
            for equipment_type_0_item_data in self.equipment:
                equipment_type_0_item = equipment_type_0_item_data.to_dict()
                equipment.append(equipment_type_0_item)

        else:
            equipment = self.equipment

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

        funding_text: dict[str, Any] | None | Unset
        if isinstance(self.funding_text, Unset):
            funding_text = UNSET
        elif isinstance(self.funding_text, LocalizedStringType0):
            funding_text = self.funding_text.to_dict()
        else:
            funding_text = self.funding_text

        funding_details: list[dict[str, Any]] | None | Unset
        if isinstance(self.funding_details, Unset):
            funding_details = UNSET
        elif isinstance(self.funding_details, list):
            funding_details = []
            for funding_details_type_0_item_data in self.funding_details:
                funding_details_type_0_item = funding_details_type_0_item_data.to_dict()
                funding_details.append(funding_details_type_0_item)

        else:
            funding_details = self.funding_details

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "managingOrganization": managing_organization,
                "type": type_,
                "publisher": publisher,
                "persons": persons,
                "visibility": visibility,
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
        if nature_types is not UNSET:
            field_dict["natureTypes"] = nature_types
        if temporal_coverage_period is not UNSET:
            field_dict["temporalCoveragePeriod"] = temporal_coverage_period
        if data_production_period is not UNSET:
            field_dict["dataProductionPeriod"] = data_production_period
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if contributors is not UNSET:
            field_dict["contributors"] = contributors
        if total_number_of_authors is not UNSET:
            field_dict["totalNumberOfAuthors"] = total_number_of_authors
        if doi is not UNSET:
            field_dict["doi"] = doi
        if documents is not UNSET:
            field_dict["documents"] = documents
        if physical_data is not UNSET:
            field_dict["physicalData"] = physical_data
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if legal_conditions is not UNSET:
            field_dict["legalConditions"] = legal_conditions
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if publication_available_date is not UNSET:
            field_dict["publicationAvailableDate"] = publication_available_date
        if open_access is not UNSET:
            field_dict["openAccess"] = open_access
        if open_aire_compliant is not UNSET:
            field_dict["openAireCompliant"] = open_aire_compliant
        if license_ is not UNSET:
            field_dict["license"] = license_
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if projects is not UNSET:
            field_dict["projects"] = projects
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if activities is not UNSET:
            field_dict["activities"] = activities
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if student_theses is not UNSET:
            field_dict["studentTheses"] = student_theses
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if links is not UNSET:
            field_dict["links"] = links
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if images is not UNSET:
            field_dict["images"] = images
        if funding_text is not UNSET:
            field_dict["fundingText"] = funding_text
        if funding_details is not UNSET:
            field_dict["fundingDetails"] = funding_details
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_data_set_contributor_association import (
            AbstractDataSetContributorAssociation,
        )
        from ..models.abstract_data_set_person_association import (
            AbstractDataSetPersonAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_localized_value import ClassifiedLocalizedValue
        from ..models.compound_date_range import CompoundDateRange
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.data_set_activity_association import DataSetActivityAssociation
        from ..models.data_set_association import DataSetAssociation
        from ..models.data_set_document import DataSetDocument
        from ..models.data_set_doi import DataSetDoi
        from ..models.data_set_equipment_association import DataSetEquipmentAssociation
        from ..models.data_set_geo_location import DataSetGeoLocation
        from ..models.data_set_impact_association import DataSetImpactAssociation
        from ..models.data_set_legal_condition import DataSetLegalCondition
        from ..models.data_set_physical_data import DataSetPhysicalData
        from ..models.data_set_press_media_association import (
            DataSetPressMediaAssociation,
        )
        from ..models.data_set_prize_association import DataSetPrizeAssociation
        from ..models.data_set_project_association import DataSetProjectAssociation
        from ..models.data_set_research_output_association import (
            DataSetResearchOutputAssociation,
        )
        from ..models.data_set_student_thesis_association import (
            DataSetStudentThesisAssociation,
        )
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.funding_details import FundingDetails
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.open_access import OpenAccess
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0
        from ..models.publisher_ref_type_0 import PublisherRefType0
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

        def _parse_publisher(data: object) -> None | PublisherRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_publisher_ref_type_0 = PublisherRefType0.from_dict(
                    data
                )

                return componentsschemas_publisher_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublisherRefType0, data)

        publisher = _parse_publisher(d.pop("publisher"))

        persons = []
        _persons = d.pop("persons")
        for persons_item_data in _persons:
            persons_item = AbstractDataSetPersonAssociation.from_dict(persons_item_data)

            persons.append(persons_item)

        visibility = Visibility.from_dict(d.pop("visibility"))

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

        _temporal_coverage_period = d.pop("temporalCoveragePeriod", UNSET)
        temporal_coverage_period: CompoundDateRange | Unset
        if isinstance(_temporal_coverage_period, Unset):
            temporal_coverage_period = UNSET
        else:
            temporal_coverage_period = CompoundDateRange.from_dict(
                _temporal_coverage_period
            )

        _data_production_period = d.pop("dataProductionPeriod", UNSET)
        data_production_period: CompoundDateRange | Unset
        if isinstance(_data_production_period, Unset):
            data_production_period = UNSET
        else:
            data_production_period = CompoundDateRange.from_dict(
                _data_production_period
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

        _geo_location = d.pop("geoLocation", UNSET)
        geo_location: DataSetGeoLocation | Unset
        if isinstance(_geo_location, Unset):
            geo_location = UNSET
        else:
            geo_location = DataSetGeoLocation.from_dict(_geo_location)

        _contributors = d.pop("contributors", UNSET)
        contributors: list[AbstractDataSetContributorAssociation] | Unset = UNSET
        if _contributors is not UNSET:
            contributors = []
            for contributors_item_data in _contributors:
                contributors_item = AbstractDataSetContributorAssociation.from_dict(
                    contributors_item_data
                )

                contributors.append(contributors_item)

        def _parse_total_number_of_authors(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_number_of_authors = _parse_total_number_of_authors(
            d.pop("totalNumberOfAuthors", UNSET)
        )

        _doi = d.pop("doi", UNSET)
        doi: DataSetDoi | Unset
        if isinstance(_doi, Unset):
            doi = UNSET
        else:
            doi = DataSetDoi.from_dict(_doi)

        def _parse_documents(data: object) -> list[DataSetDocument] | None | Unset:
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
                    documents_type_0_item = DataSetDocument.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetDocument] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

        def _parse_physical_data(
            data: object,
        ) -> list[DataSetPhysicalData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                physical_data_type_0 = []
                _physical_data_type_0 = data
                for physical_data_type_0_item_data in _physical_data_type_0:
                    physical_data_type_0_item = DataSetPhysicalData.from_dict(
                        physical_data_type_0_item_data
                    )

                    physical_data_type_0.append(physical_data_type_0_item)

                return physical_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetPhysicalData] | None | Unset, data)

        physical_data = _parse_physical_data(d.pop("physicalData", UNSET))

        def _parse_contact_person(data: object) -> None | PersonRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_ref_type_0 = PersonRefType0.from_dict(data)

                return componentsschemas_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonRefType0 | Unset, data)

        contact_person = _parse_contact_person(d.pop("contactPerson", UNSET))

        def _parse_legal_conditions(
            data: object,
        ) -> list[DataSetLegalCondition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                legal_conditions_type_0 = []
                _legal_conditions_type_0 = data
                for legal_conditions_type_0_item_data in _legal_conditions_type_0:
                    legal_conditions_type_0_item = DataSetLegalCondition.from_dict(
                        legal_conditions_type_0_item_data
                    )

                    legal_conditions_type_0.append(legal_conditions_type_0_item)

                return legal_conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetLegalCondition] | None | Unset, data)

        legal_conditions = _parse_legal_conditions(d.pop("legalConditions", UNSET))

        def _parse_organizations(
            data: object,
        ) -> list[None | OrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:

                    def _parse_organizations_type_0_item(
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

                    organizations_type_0_item = _parse_organizations_type_0_item(
                        organizations_type_0_item_data
                    )

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | OrganizationRefType0] | None | Unset, data)

        organizations = _parse_organizations(d.pop("organizations", UNSET))

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

        def _parse_publication_available_date(
            data: object,
        ) -> CompoundDateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compound_date_type_0 = CompoundDateType0.from_dict(
                    data
                )

                return componentsschemas_compound_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompoundDateType0 | None | Unset, data)

        publication_available_date = _parse_publication_available_date(
            d.pop("publicationAvailableDate", UNSET)
        )

        _open_access = d.pop("openAccess", UNSET)
        open_access: OpenAccess | Unset
        if isinstance(_open_access, Unset):
            open_access = UNSET
        else:
            open_access = OpenAccess.from_dict(_open_access)

        open_aire_compliant = d.pop("openAireCompliant", UNSET)

        def _parse_license_(data: object) -> ClassificationRefType0 | None | Unset:
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

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_data_sets(data: object) -> list[DataSetAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_sets_type_0 = []
                _data_sets_type_0 = data
                for data_sets_type_0_item_data in _data_sets_type_0:
                    data_sets_type_0_item = DataSetAssociation.from_dict(
                        data_sets_type_0_item_data
                    )

                    data_sets_type_0.append(data_sets_type_0_item)

                return data_sets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetAssociation] | None | Unset, data)

        data_sets = _parse_data_sets(d.pop("dataSets", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[DataSetProjectAssociation] | None | Unset:
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
                    projects_type_0_item = DataSetProjectAssociation.from_dict(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetProjectAssociation] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[DataSetResearchOutputAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                research_outputs_type_0 = []
                _research_outputs_type_0 = data
                for research_outputs_type_0_item_data in _research_outputs_type_0:
                    research_outputs_type_0_item = (
                        DataSetResearchOutputAssociation.from_dict(
                            research_outputs_type_0_item_data
                        )
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetResearchOutputAssociation] | None | Unset, data)

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

        def _parse_activities(
            data: object,
        ) -> list[DataSetActivityAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                activities_type_0 = []
                _activities_type_0 = data
                for activities_type_0_item_data in _activities_type_0:
                    activities_type_0_item = DataSetActivityAssociation.from_dict(
                        activities_type_0_item_data
                    )

                    activities_type_0.append(activities_type_0_item)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetActivityAssociation] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_press_media(
            data: object,
        ) -> list[DataSetPressMediaAssociation] | None | Unset:
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
                    press_media_type_0_item = DataSetPressMediaAssociation.from_dict(
                        press_media_type_0_item_data
                    )

                    press_media_type_0.append(press_media_type_0_item)

                return press_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetPressMediaAssociation] | None | Unset, data)

        press_media = _parse_press_media(d.pop("pressMedia", UNSET))

        def _parse_student_theses(
            data: object,
        ) -> list[DataSetStudentThesisAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                student_theses_type_0 = []
                _student_theses_type_0 = data
                for student_theses_type_0_item_data in _student_theses_type_0:
                    student_theses_type_0_item = (
                        DataSetStudentThesisAssociation.from_dict(
                            student_theses_type_0_item_data
                        )
                    )

                    student_theses_type_0.append(student_theses_type_0_item)

                return student_theses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetStudentThesisAssociation] | None | Unset, data)

        student_theses = _parse_student_theses(d.pop("studentTheses", UNSET))

        def _parse_impacts(
            data: object,
        ) -> list[DataSetImpactAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                impacts_type_0 = []
                _impacts_type_0 = data
                for impacts_type_0_item_data in _impacts_type_0:
                    impacts_type_0_item = DataSetImpactAssociation.from_dict(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetImpactAssociation] | None | Unset, data)

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_prizes(data: object) -> list[DataSetPrizeAssociation] | None | Unset:
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
                    prizes_type_0_item = DataSetPrizeAssociation.from_dict(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetPrizeAssociation] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_equipment(
            data: object,
        ) -> list[DataSetEquipmentAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                equipment_type_0 = []
                _equipment_type_0 = data
                for equipment_type_0_item_data in _equipment_type_0:
                    equipment_type_0_item = DataSetEquipmentAssociation.from_dict(
                        equipment_type_0_item_data
                    )

                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetEquipmentAssociation] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))

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

        def _parse_funding_text(data: object) -> LocalizedStringType0 | None | Unset:
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

        funding_text = _parse_funding_text(d.pop("fundingText", UNSET))

        def _parse_funding_details(data: object) -> list[FundingDetails] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_details_type_0 = []
                _funding_details_type_0 = data
                for funding_details_type_0_item_data in _funding_details_type_0:
                    funding_details_type_0_item = FundingDetails.from_dict(
                        funding_details_type_0_item_data
                    )

                    funding_details_type_0.append(funding_details_type_0_item)

                return funding_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FundingDetails] | None | Unset, data)

        funding_details = _parse_funding_details(d.pop("fundingDetails", UNSET))

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

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        system_name = d.pop("systemName", UNSET)

        data_set = cls(
            title=title,
            managing_organization=managing_organization,
            type_=type_,
            publisher=publisher,
            persons=persons,
            visibility=visibility,
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
            nature_types=nature_types,
            temporal_coverage_period=temporal_coverage_period,
            data_production_period=data_production_period,
            identifiers=identifiers,
            geo_location=geo_location,
            contributors=contributors,
            total_number_of_authors=total_number_of_authors,
            doi=doi,
            documents=documents,
            physical_data=physical_data,
            contact_person=contact_person,
            legal_conditions=legal_conditions,
            organizations=organizations,
            external_organizations=external_organizations,
            publication_available_date=publication_available_date,
            open_access=open_access,
            open_aire_compliant=open_aire_compliant,
            license_=license_,
            data_sets=data_sets,
            projects=projects,
            research_outputs=research_outputs,
            activities=activities,
            press_media=press_media,
            student_theses=student_theses,
            impacts=impacts,
            prizes=prizes,
            equipment=equipment,
            links=links,
            keyword_groups=keyword_groups,
            images=images,
            funding_text=funding_text,
            funding_details=funding_details,
            custom_defined_fields=custom_defined_fields,
            workflow=workflow,
            system_name=system_name,
        )

        data_set.additional_properties = d
        return data_set

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
