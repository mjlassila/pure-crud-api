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
    from ..models.abstract_prize_receiver_association import (
        AbstractPrizeReceiverAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.compound_date_type_0 import CompoundDateType0
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.document import Document
    from ..models.event_ref_type_0 import EventRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.prize_activity_association import PrizeActivityAssociation
    from ..models.prize_association import PrizeAssociation
    from ..models.prize_data_set_association import PrizeDataSetAssociation
    from ..models.prize_equipment_association import PrizeEquipmentAssociation
    from ..models.prize_impact_association import PrizeImpactAssociation
    from ..models.prize_press_media_association import PrizePressMediaAssociation
    from ..models.prize_project_association import PrizeProjectAssociation
    from ..models.prize_research_output_association import (
        PrizeResearchOutputAssociation,
    )
    from ..models.prize_student_thesis_association import PrizeStudentThesisAssociation
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Prize")


@_attrs_define
class Prize:
    """A prize.

    Attributes:
        title (FormattedLocalizedStringType0 | None): A set of localized strings that support formatting. Invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        receivers_of_prize (list[AbstractPrizeReceiverAssociation]): The receivers of the prize.
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
        granting_organizations (list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset): The granting
            organizations.
        degree_of_recognition (ClassificationRefType0 | None | Unset): A reference to a classification value
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
        awarded_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and month or a
            full date
        prizes (list[PrizeAssociation] | None | Unset): A collection of related prizes.
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present.
        visibility (Visibility | Unset): Visibility of an object
        workflow (Workflow | Unset): Information about workflow
        links (list[Link] | None | Unset): Additional links associated with this prize.
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organizational unit
            affiliations.
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        event (EventRefType0 | None | Unset): A reference to an event
        documents (list[Document] | None | Unset): Associated documents for the prize.
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        activities (list[PrizeActivityAssociation] | None | Unset): A collection of related activities.
        research_outputs (list[PrizeResearchOutputAssociation] | None | Unset): A collection of related research
            outputs.
        impacts (list[PrizeImpactAssociation] | None | Unset): A collection of related impacts.
        press_media (list[PrizePressMediaAssociation] | None | Unset): A collection of related press media.
        equipment (list[PrizeEquipmentAssociation] | None | Unset): A collection of related equipment.
        data_sets (list[PrizeDataSetAssociation] | None | Unset): A collection of related datasets.
        projects (list[PrizeProjectAssociation] | None | Unset): A collection of related projects.
        student_theses (list[PrizeStudentThesisAssociation] | None | Unset): A collection of related student theses.
        system_name (str | Unset): The content system name
    """

    title: FormattedLocalizedStringType0 | None
    receivers_of_prize: list[AbstractPrizeReceiverAssociation]
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
    granting_organizations: (
        list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset
    ) = UNSET
    degree_of_recognition: ClassificationRefType0 | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    awarded_date: CompoundDateType0 | None | Unset = UNSET
    prizes: list[PrizeAssociation] | None | Unset = UNSET
    category: ClassificationRefType0 | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    event: EventRefType0 | None | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    activities: list[PrizeActivityAssociation] | None | Unset = UNSET
    research_outputs: list[PrizeResearchOutputAssociation] | None | Unset = UNSET
    impacts: list[PrizeImpactAssociation] | None | Unset = UNSET
    press_media: list[PrizePressMediaAssociation] | None | Unset = UNSET
    equipment: list[PrizeEquipmentAssociation] | None | Unset = UNSET
    data_sets: list[PrizeDataSetAssociation] | None | Unset = UNSET
    projects: list[PrizeProjectAssociation] | None | Unset = UNSET
    student_theses: list[PrizeStudentThesisAssociation] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        title: dict[str, Any] | None
        if isinstance(self.title, FormattedLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        receivers_of_prize = []
        for receivers_of_prize_item_data in self.receivers_of_prize:
            receivers_of_prize_item = receivers_of_prize_item_data.to_dict()
            receivers_of_prize.append(receivers_of_prize_item)

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

        granting_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.granting_organizations, Unset):
            granting_organizations = UNSET
        elif isinstance(self.granting_organizations, list):
            granting_organizations = []
            for granting_organizations_type_0_item_data in self.granting_organizations:
                granting_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    granting_organizations_type_0_item_data,
                    OrganizationOrExternalOrganizationRefType0,
                ):
                    granting_organizations_type_0_item = (
                        granting_organizations_type_0_item_data.to_dict()
                    )
                else:
                    granting_organizations_type_0_item = (
                        granting_organizations_type_0_item_data
                    )
                granting_organizations.append(granting_organizations_type_0_item)

        else:
            granting_organizations = self.granting_organizations

        degree_of_recognition: dict[str, Any] | None | Unset
        if isinstance(self.degree_of_recognition, Unset):
            degree_of_recognition = UNSET
        elif isinstance(self.degree_of_recognition, ClassificationRefType0):
            degree_of_recognition = self.degree_of_recognition.to_dict()
        else:
            degree_of_recognition = self.degree_of_recognition

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

        awarded_date: dict[str, Any] | None | Unset
        if isinstance(self.awarded_date, Unset):
            awarded_date = UNSET
        elif isinstance(self.awarded_date, CompoundDateType0):
            awarded_date = self.awarded_date.to_dict()
        else:
            awarded_date = self.awarded_date

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

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

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

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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

        event: dict[str, Any] | None | Unset
        if isinstance(self.event, Unset):
            event = UNSET
        elif isinstance(self.event, EventRefType0):
            event = self.event.to_dict()
        else:
            event = self.event

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "receiversOfPrize": receivers_of_prize,
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
        if granting_organizations is not UNSET:
            field_dict["grantingOrganizations"] = granting_organizations
        if degree_of_recognition is not UNSET:
            field_dict["degreeOfRecognition"] = degree_of_recognition
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if awarded_date is not UNSET:
            field_dict["awardedDate"] = awarded_date
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if category is not UNSET:
            field_dict["category"] = category
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if links is not UNSET:
            field_dict["links"] = links
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if event is not UNSET:
            field_dict["event"] = event
        if documents is not UNSET:
            field_dict["documents"] = documents
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if images is not UNSET:
            field_dict["images"] = images
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if activities is not UNSET:
            field_dict["activities"] = activities
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if projects is not UNSET:
            field_dict["projects"] = projects
        if student_theses is not UNSET:
            field_dict["studentTheses"] = student_theses
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_prize_receiver_association import (
            AbstractPrizeReceiverAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.document import Document
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.prize_activity_association import PrizeActivityAssociation
        from ..models.prize_association import PrizeAssociation
        from ..models.prize_data_set_association import PrizeDataSetAssociation
        from ..models.prize_equipment_association import PrizeEquipmentAssociation
        from ..models.prize_impact_association import PrizeImpactAssociation
        from ..models.prize_press_media_association import PrizePressMediaAssociation
        from ..models.prize_project_association import PrizeProjectAssociation
        from ..models.prize_research_output_association import (
            PrizeResearchOutputAssociation,
        )
        from ..models.prize_student_thesis_association import (
            PrizeStudentThesisAssociation,
        )
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

        receivers_of_prize = []
        _receivers_of_prize = d.pop("receiversOfPrize")
        for receivers_of_prize_item_data in _receivers_of_prize:
            receivers_of_prize_item = AbstractPrizeReceiverAssociation.from_dict(
                receivers_of_prize_item_data
            )

            receivers_of_prize.append(receivers_of_prize_item)

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

        def _parse_granting_organizations(
            data: object,
        ) -> list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                granting_organizations_type_0 = []
                _granting_organizations_type_0 = data
                for (
                    granting_organizations_type_0_item_data
                ) in _granting_organizations_type_0:

                    def _parse_granting_organizations_type_0_item(
                        data: object,
                    ) -> None | OrganizationOrExternalOrganizationRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_organization_or_external_organization_ref_type_0 = OrganizationOrExternalOrganizationRefType0.from_dict(
                                data
                            )

                            return componentsschemas_organization_or_external_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | OrganizationOrExternalOrganizationRefType0, data
                        )

                    granting_organizations_type_0_item = (
                        _parse_granting_organizations_type_0_item(
                            granting_organizations_type_0_item_data
                        )
                    )

                    granting_organizations_type_0.append(
                        granting_organizations_type_0_item
                    )

                return granting_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset,
                data,
            )

        granting_organizations = _parse_granting_organizations(
            d.pop("grantingOrganizations", UNSET)
        )

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

        def _parse_awarded_date(data: object) -> CompoundDateType0 | None | Unset:
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

        awarded_date = _parse_awarded_date(d.pop("awardedDate", UNSET))

        def _parse_prizes(data: object) -> list[PrizeAssociation] | None | Unset:
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
                    prizes_type_0_item = PrizeAssociation.from_dict(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeAssociation] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

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

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

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

        def _parse_activities(
            data: object,
        ) -> list[PrizeActivityAssociation] | None | Unset:
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
                    activities_type_0_item = PrizeActivityAssociation.from_dict(
                        activities_type_0_item_data
                    )

                    activities_type_0.append(activities_type_0_item)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeActivityAssociation] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[PrizeResearchOutputAssociation] | None | Unset:
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
                        PrizeResearchOutputAssociation.from_dict(
                            research_outputs_type_0_item_data
                        )
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeResearchOutputAssociation] | None | Unset, data)

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

        def _parse_impacts(data: object) -> list[PrizeImpactAssociation] | None | Unset:
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
                    impacts_type_0_item = PrizeImpactAssociation.from_dict(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeImpactAssociation] | None | Unset, data)

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_press_media(
            data: object,
        ) -> list[PrizePressMediaAssociation] | None | Unset:
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
                    press_media_type_0_item = PrizePressMediaAssociation.from_dict(
                        press_media_type_0_item_data
                    )

                    press_media_type_0.append(press_media_type_0_item)

                return press_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizePressMediaAssociation] | None | Unset, data)

        press_media = _parse_press_media(d.pop("pressMedia", UNSET))

        def _parse_equipment(
            data: object,
        ) -> list[PrizeEquipmentAssociation] | None | Unset:
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
                    equipment_type_0_item = PrizeEquipmentAssociation.from_dict(
                        equipment_type_0_item_data
                    )

                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeEquipmentAssociation] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))

        def _parse_data_sets(
            data: object,
        ) -> list[PrizeDataSetAssociation] | None | Unset:
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
                    data_sets_type_0_item = PrizeDataSetAssociation.from_dict(
                        data_sets_type_0_item_data
                    )

                    data_sets_type_0.append(data_sets_type_0_item)

                return data_sets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeDataSetAssociation] | None | Unset, data)

        data_sets = _parse_data_sets(d.pop("dataSets", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[PrizeProjectAssociation] | None | Unset:
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
                    projects_type_0_item = PrizeProjectAssociation.from_dict(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeProjectAssociation] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_student_theses(
            data: object,
        ) -> list[PrizeStudentThesisAssociation] | None | Unset:
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
                        PrizeStudentThesisAssociation.from_dict(
                            student_theses_type_0_item_data
                        )
                    )

                    student_theses_type_0.append(student_theses_type_0_item)

                return student_theses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeStudentThesisAssociation] | None | Unset, data)

        student_theses = _parse_student_theses(d.pop("studentTheses", UNSET))

        system_name = d.pop("systemName", UNSET)

        prize = cls(
            title=title,
            receivers_of_prize=receivers_of_prize,
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
            granting_organizations=granting_organizations,
            degree_of_recognition=degree_of_recognition,
            identifiers=identifiers,
            awarded_date=awarded_date,
            prizes=prizes,
            category=category,
            keyword_groups=keyword_groups,
            visibility=visibility,
            workflow=workflow,
            links=links,
            organizations=organizations,
            external_organizations=external_organizations,
            event=event,
            documents=documents,
            descriptions=descriptions,
            images=images,
            custom_defined_fields=custom_defined_fields,
            activities=activities,
            research_outputs=research_outputs,
            impacts=impacts,
            press_media=press_media,
            equipment=equipment,
            data_sets=data_sets,
            projects=projects,
            student_theses=student_theses,
            system_name=system_name,
        )

        prize.additional_properties = d
        return prize

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
