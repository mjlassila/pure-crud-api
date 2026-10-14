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
    from ..models.abstract_activity_person_association import (
        AbstractActivityPersonAssociation,
    )
    from ..models.activity_dataset_association import ActivityDatasetAssociation
    from ..models.activity_prize_association import ActivityPrizeAssociation
    from ..models.activity_project_association import ActivityProjectAssociation
    from ..models.activity_ref_type_0 import ActivityRefType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.compound_date_range import CompoundDateRange
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.document import Document
    from ..models.equipment_ref_type_0 import EquipmentRefType0
    from ..models.event_ref_type_0 import EventRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.impact_ref_type_0 import ImpactRefType0
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.press_media_ref_type_0 import PressMediaRefType0
    from ..models.research_output_ref_type_0 import ResearchOutputRefType0
    from ..models.student_thesis_ref_type_0 import StudentThesisRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Attendance")


@_attrs_define
class Attendance:
    """Participating in or organizing an event

    Attributes:
        persons (list[AbstractActivityPersonAssociation]): A collection of persons.
        period (CompoundDateRange): A date range of that can be defined by only year, year and month or a full date
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
        type_ (ClassificationRefType0 | None): A reference to a classification value
        visibility (Visibility): Visibility of an object
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
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organization associations.
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        links (list[Link] | None | Unset): Additional links associated with this activity.
        workflow (Workflow | Unset): Information about workflow
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the activity.
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the research output.
        activities (list[ActivityRefType0 | None] | None | Unset): A collection of related activities.
        press_media (list[None | PressMediaRefType0] | None | Unset): A collection of related press media.
        student_theses (list[None | StudentThesisRefType0] | None | Unset): A collection of related student theses.
        prizes (list[ActivityPrizeAssociation] | None | Unset): A collection of related prizes.
        projects (list[ActivityProjectAssociation] | None | Unset): A collection of related projects.
        data_sets (list[ActivityDatasetAssociation] | None | Unset): A collection of related data sets.
        research_outputs (list[None | ResearchOutputRefType0] | None | Unset): A collection of related research outputs.
        impacts (list[ImpactRefType0 | None] | None | Unset): A collection of related impacts.
        equipment (list[EquipmentRefType0 | None] | None | Unset): A collection of equipment.
        degree_of_recognition (ClassificationRefType0 | None | Unset): A reference to a classification value
        documents (list[Document] | None | Unset): Associated documents for the activity.
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB.
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        indicators (list[ClassificationRefType0 | None] | None | Unset): Indicators for the activity.
        system_name (str | Unset): The content system name
        event (EventRefType0 | None | Unset): A reference to an event
    """

    persons: list[AbstractActivityPersonAssociation]
    period: CompoundDateRange
    managing_organization: None | OrganizationRefType0
    type_: ClassificationRefType0 | None
    visibility: Visibility
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
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    category: ClassificationRefType0 | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    identifiers: list[Identifier] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    activities: list[ActivityRefType0 | None] | None | Unset = UNSET
    press_media: list[None | PressMediaRefType0] | None | Unset = UNSET
    student_theses: list[None | StudentThesisRefType0] | None | Unset = UNSET
    prizes: list[ActivityPrizeAssociation] | None | Unset = UNSET
    projects: list[ActivityProjectAssociation] | None | Unset = UNSET
    data_sets: list[ActivityDatasetAssociation] | None | Unset = UNSET
    research_outputs: list[None | ResearchOutputRefType0] | None | Unset = UNSET
    impacts: list[ImpactRefType0 | None] | None | Unset = UNSET
    equipment: list[EquipmentRefType0 | None] | None | Unset = UNSET
    degree_of_recognition: ClassificationRefType0 | None | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    indicators: list[ClassificationRefType0 | None] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    event: EventRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.press_media_ref_type_0 import PressMediaRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0

        persons = []
        for persons_item_data in self.persons:
            persons_item = persons_item_data.to_dict()
            persons.append(persons_item)

        period = self.period.to_dict()

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

        visibility = self.visibility.to_dict()

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

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

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

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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

        activities: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.activities, Unset):
            activities = UNSET
        elif isinstance(self.activities, list):
            activities = []
            for activities_type_0_item_data in self.activities:
                activities_type_0_item: dict[str, Any] | None
                if isinstance(activities_type_0_item_data, ActivityRefType0):
                    activities_type_0_item = activities_type_0_item_data.to_dict()
                else:
                    activities_type_0_item = activities_type_0_item_data
                activities.append(activities_type_0_item)

        else:
            activities = self.activities

        press_media: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.press_media, Unset):
            press_media = UNSET
        elif isinstance(self.press_media, list):
            press_media = []
            for press_media_type_0_item_data in self.press_media:
                press_media_type_0_item: dict[str, Any] | None
                if isinstance(press_media_type_0_item_data, PressMediaRefType0):
                    press_media_type_0_item = press_media_type_0_item_data.to_dict()
                else:
                    press_media_type_0_item = press_media_type_0_item_data
                press_media.append(press_media_type_0_item)

        else:
            press_media = self.press_media

        student_theses: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.student_theses, Unset):
            student_theses = UNSET
        elif isinstance(self.student_theses, list):
            student_theses = []
            for student_theses_type_0_item_data in self.student_theses:
                student_theses_type_0_item: dict[str, Any] | None
                if isinstance(student_theses_type_0_item_data, StudentThesisRefType0):
                    student_theses_type_0_item = (
                        student_theses_type_0_item_data.to_dict()
                    )
                else:
                    student_theses_type_0_item = student_theses_type_0_item_data
                student_theses.append(student_theses_type_0_item)

        else:
            student_theses = self.student_theses

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

        research_outputs: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.research_outputs, Unset):
            research_outputs = UNSET
        elif isinstance(self.research_outputs, list):
            research_outputs = []
            for research_outputs_type_0_item_data in self.research_outputs:
                research_outputs_type_0_item: dict[str, Any] | None
                if isinstance(
                    research_outputs_type_0_item_data, ResearchOutputRefType0
                ):
                    research_outputs_type_0_item = (
                        research_outputs_type_0_item_data.to_dict()
                    )
                else:
                    research_outputs_type_0_item = research_outputs_type_0_item_data
                research_outputs.append(research_outputs_type_0_item)

        else:
            research_outputs = self.research_outputs

        impacts: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.impacts, Unset):
            impacts = UNSET
        elif isinstance(self.impacts, list):
            impacts = []
            for impacts_type_0_item_data in self.impacts:
                impacts_type_0_item: dict[str, Any] | None
                if isinstance(impacts_type_0_item_data, ImpactRefType0):
                    impacts_type_0_item = impacts_type_0_item_data.to_dict()
                else:
                    impacts_type_0_item = impacts_type_0_item_data
                impacts.append(impacts_type_0_item)

        else:
            impacts = self.impacts

        equipment: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.equipment, Unset):
            equipment = UNSET
        elif isinstance(self.equipment, list):
            equipment = []
            for equipment_type_0_item_data in self.equipment:
                equipment_type_0_item: dict[str, Any] | None
                if isinstance(equipment_type_0_item_data, EquipmentRefType0):
                    equipment_type_0_item = equipment_type_0_item_data.to_dict()
                else:
                    equipment_type_0_item = equipment_type_0_item_data
                equipment.append(equipment_type_0_item)

        else:
            equipment = self.equipment

        degree_of_recognition: dict[str, Any] | None | Unset
        if isinstance(self.degree_of_recognition, Unset):
            degree_of_recognition = UNSET
        elif isinstance(self.degree_of_recognition, ClassificationRefType0):
            degree_of_recognition = self.degree_of_recognition.to_dict()
        else:
            degree_of_recognition = self.degree_of_recognition

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

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

        indicators: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.indicators, Unset):
            indicators = UNSET
        elif isinstance(self.indicators, list):
            indicators = []
            for indicators_type_0_item_data in self.indicators:
                indicators_type_0_item: dict[str, Any] | None
                if isinstance(indicators_type_0_item_data, ClassificationRefType0):
                    indicators_type_0_item = indicators_type_0_item_data.to_dict()
                else:
                    indicators_type_0_item = indicators_type_0_item_data
                indicators.append(indicators_type_0_item)

        else:
            indicators = self.indicators

        system_name = self.system_name

        event: dict[str, Any] | None | Unset
        if isinstance(self.event, Unset):
            event = UNSET
        elif isinstance(self.event, EventRefType0):
            event = self.event.to_dict()
        else:
            event = self.event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "persons": persons,
                "period": period,
                "managingOrganization": managing_organization,
                "type": type_,
                "visibility": visibility,
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
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if category is not UNSET:
            field_dict["category"] = category
        if links is not UNSET:
            field_dict["links"] = links
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if activities is not UNSET:
            field_dict["activities"] = activities
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if student_theses is not UNSET:
            field_dict["studentTheses"] = student_theses
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if projects is not UNSET:
            field_dict["projects"] = projects
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if degree_of_recognition is not UNSET:
            field_dict["degreeOfRecognition"] = degree_of_recognition
        if documents is not UNSET:
            field_dict["documents"] = documents
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if images is not UNSET:
            field_dict["images"] = images
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if indicators is not UNSET:
            field_dict["indicators"] = indicators
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_activity_person_association import (
            AbstractActivityPersonAssociation,
        )
        from ..models.activity_dataset_association import ActivityDatasetAssociation
        from ..models.activity_prize_association import ActivityPrizeAssociation
        from ..models.activity_project_association import ActivityProjectAssociation
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.compound_date_range import CompoundDateRange
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.document import Document
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.press_media_ref_type_0 import PressMediaRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)
        persons = []
        _persons = d.pop("persons")
        for persons_item_data in _persons:
            persons_item = AbstractActivityPersonAssociation.from_dict(
                persons_item_data
            )

            persons.append(persons_item)

        period = CompoundDateRange.from_dict(d.pop("period"))

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

        visibility = Visibility.from_dict(d.pop("visibility"))

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

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

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

        def _parse_activities(
            data: object,
        ) -> list[ActivityRefType0 | None] | None | Unset:
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

                    def _parse_activities_type_0_item(
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

                    activities_type_0_item = _parse_activities_type_0_item(
                        activities_type_0_item_data
                    )

                    activities_type_0.append(activities_type_0_item)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityRefType0 | None] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_press_media(
            data: object,
        ) -> list[None | PressMediaRefType0] | None | Unset:
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

                    def _parse_press_media_type_0_item(
                        data: object,
                    ) -> None | PressMediaRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_press_media_ref_type_0 = (
                                PressMediaRefType0.from_dict(data)
                            )

                            return componentsschemas_press_media_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | PressMediaRefType0, data)

                    press_media_type_0_item = _parse_press_media_type_0_item(
                        press_media_type_0_item_data
                    )

                    press_media_type_0.append(press_media_type_0_item)

                return press_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | PressMediaRefType0] | None | Unset, data)

        press_media = _parse_press_media(d.pop("pressMedia", UNSET))

        def _parse_student_theses(
            data: object,
        ) -> list[None | StudentThesisRefType0] | None | Unset:
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

                    def _parse_student_theses_type_0_item(
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

                    student_theses_type_0_item = _parse_student_theses_type_0_item(
                        student_theses_type_0_item_data
                    )

                    student_theses_type_0.append(student_theses_type_0_item)

                return student_theses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | StudentThesisRefType0] | None | Unset, data)

        student_theses = _parse_student_theses(d.pop("studentTheses", UNSET))

        def _parse_prizes(
            data: object,
        ) -> list[ActivityPrizeAssociation] | None | Unset:
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
                    prizes_type_0_item = ActivityPrizeAssociation.from_dict(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityPrizeAssociation] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[ActivityProjectAssociation] | None | Unset:
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
                    projects_type_0_item = ActivityProjectAssociation.from_dict(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityProjectAssociation] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_data_sets(
            data: object,
        ) -> list[ActivityDatasetAssociation] | None | Unset:
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
                    data_sets_type_0_item = ActivityDatasetAssociation.from_dict(
                        data_sets_type_0_item_data
                    )

                    data_sets_type_0.append(data_sets_type_0_item)

                return data_sets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityDatasetAssociation] | None | Unset, data)

        data_sets = _parse_data_sets(d.pop("dataSets", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[None | ResearchOutputRefType0] | None | Unset:
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

                    def _parse_research_outputs_type_0_item(
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

                    research_outputs_type_0_item = _parse_research_outputs_type_0_item(
                        research_outputs_type_0_item_data
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | ResearchOutputRefType0] | None | Unset, data)

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

        def _parse_impacts(data: object) -> list[ImpactRefType0 | None] | None | Unset:
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

                    def _parse_impacts_type_0_item(
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

                    impacts_type_0_item = _parse_impacts_type_0_item(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImpactRefType0 | None] | None | Unset, data)

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_equipment(
            data: object,
        ) -> list[EquipmentRefType0 | None] | None | Unset:
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

                    def _parse_equipment_type_0_item(
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

                    equipment_type_0_item = _parse_equipment_type_0_item(
                        equipment_type_0_item_data
                    )

                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentRefType0 | None] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))

        def _parse_degree_of_recognition(
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

        degree_of_recognition = _parse_degree_of_recognition(
            d.pop("degreeOfRecognition", UNSET)
        )

        def _parse_documents(data: object) -> list[Document] | None | Unset:
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
                    documents_type_0_item = Document.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Document] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

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

        def _parse_indicators(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indicators_type_0 = []
                _indicators_type_0 = data
                for indicators_type_0_item_data in _indicators_type_0:

                    def _parse_indicators_type_0_item(
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

                    indicators_type_0_item = _parse_indicators_type_0_item(
                        indicators_type_0_item_data
                    )

                    indicators_type_0.append(indicators_type_0_item)

                return indicators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        indicators = _parse_indicators(d.pop("indicators", UNSET))

        system_name = d.pop("systemName", UNSET)

        def _parse_event(data: object) -> EventRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_event_ref_type_0 = EventRefType0.from_dict(data)

                return componentsschemas_event_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventRefType0 | None | Unset, data)

        event = _parse_event(d.pop("event", UNSET))

        attendance = cls(
            persons=persons,
            period=period,
            managing_organization=managing_organization,
            type_=type_,
            visibility=visibility,
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
            organizations=organizations,
            category=category,
            links=links,
            workflow=workflow,
            external_organizations=external_organizations,
            identifiers=identifiers,
            keyword_groups=keyword_groups,
            activities=activities,
            press_media=press_media,
            student_theses=student_theses,
            prizes=prizes,
            projects=projects,
            data_sets=data_sets,
            research_outputs=research_outputs,
            impacts=impacts,
            equipment=equipment,
            degree_of_recognition=degree_of_recognition,
            documents=documents,
            descriptions=descriptions,
            images=images,
            custom_defined_fields=custom_defined_fields,
            indicators=indicators,
            system_name=system_name,
            event=event,
        )

        attendance.additional_properties = d
        return attendance

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
