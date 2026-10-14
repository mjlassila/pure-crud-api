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
    from ..models.abstract_participant_association import AbstractParticipantAssociation
    from ..models.activity_awardable_association import ActivityAwardableAssociation
    from ..models.application_cluster_ref_type_0 import ApplicationClusterRefType0
    from ..models.award_cluster_ref_type_0 import AwardClusterRefType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.collaborator_association import CollaboratorAssociation
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.data_set_awardable_association import DataSetAwardableAssociation
    from ..models.date_range import DateRange
    from ..models.deprecated_date_range import DeprecatedDateRange
    from ..models.document import Document
    from ..models.equipment_awardable_association import EquipmentAwardableAssociation
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.impact_awardable_association import ImpactAwardableAssociation
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.press_media_awardable_association import (
        PressMediaAwardableAssociation,
    )
    from ..models.prize_awardable_association import PrizeAwardableAssociation
    from ..models.project_association import ProjectAssociation
    from ..models.project_curtailed import ProjectCurtailed
    from ..models.research_output_awardable_association import (
        ResearchOutputAwardableAssociation,
    )
    from ..models.student_thesis_awardable_association import (
        StudentThesisAwardableAssociation,
    )
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="BasicProject")


@_attrs_define
class BasicProject:
    """The Basic project template is used when the Award Management module is not enabled for the Pure installation.

    Attributes:
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
        acronym (None | str | Unset): The acronym of the project.
        participants (list[AbstractParticipantAssociation] | Unset): Related participants and their affiliations.
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        co_managing_organizations (list[None | OrganizationRefType0] | None | Unset): A collection of co-managing
            organizational affiliations.
        collaborators (list[CollaboratorAssociation] | None | Unset): A collection of collaborators.
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions for the
            project. Query the /projects/allowed-description-types endpoint for allowed types.
        period (DateRange | Unset): A date range
        effective_period (DeprecatedDateRange | Unset): Deprecated version of DateRange
        identifiers (list[Identifier] | None | Unset): Identifiers related to the project.
        nature_types (list[ClassificationRefType0 | None] | None | Unset): Nature of activity types for the project.
        short_title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        total_academic_ownership (float | Unset): Total academic ownership of the project.
        workflow (Workflow | Unset): Information about workflow
        visibility (Visibility | Unset): Visibility of an object
        links (list[Link] | None | Unset): Links associated with the project.
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the project.
        documents (list[Document] | None | Unset): A collection of documents related to the project.
        curtailed (ProjectCurtailed | Unset): Information about project curtail.
        projects (list[ProjectAssociation] | None | Unset): A collection of related projects.
        application_clusters (list[ApplicationClusterRefType0 | None] | None | Unset): A collection of related
            application clusters.
        award_clusters (list[AwardClusterRefType0 | None] | None | Unset): A collection of related grant clusters.
        data_sets (list[DataSetAwardableAssociation] | None | Unset): A collection of related datasets.
        prizes (list[PrizeAwardableAssociation] | None | Unset): A collection of related prizes.
        activities (list[ActivityAwardableAssociation] | None | Unset): A collection of related activities.
        press_medias (list[PressMediaAwardableAssociation] | None | Unset): A collection of related press/media.
        equipment (list[EquipmentAwardableAssociation] | None | Unset): A collection of related equipment.
        impacts (list[ImpactAwardableAssociation] | None | Unset): A collection of related impacts.
        research_outputs (list[ResearchOutputAwardableAssociation] | None | Unset): A collection of related research
            output.
        student_theses (list[StudentThesisAwardableAssociation] | None | Unset): A collection of related student theses.
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        system_name (str | Unset): The content system name
    """

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
    participants: list[AbstractParticipantAssociation] | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    co_managing_organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    collaborators: list[CollaboratorAssociation] | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    period: DateRange | Unset = UNSET
    effective_period: DeprecatedDateRange | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    nature_types: list[ClassificationRefType0 | None] | None | Unset = UNSET
    short_title: LocalizedStringType0 | None | Unset = UNSET
    total_academic_ownership: float | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    curtailed: ProjectCurtailed | Unset = UNSET
    projects: list[ProjectAssociation] | None | Unset = UNSET
    application_clusters: list[ApplicationClusterRefType0 | None] | None | Unset = UNSET
    award_clusters: list[AwardClusterRefType0 | None] | None | Unset = UNSET
    data_sets: list[DataSetAwardableAssociation] | None | Unset = UNSET
    prizes: list[PrizeAwardableAssociation] | None | Unset = UNSET
    activities: list[ActivityAwardableAssociation] | None | Unset = UNSET
    press_medias: list[PressMediaAwardableAssociation] | None | Unset = UNSET
    equipment: list[EquipmentAwardableAssociation] | None | Unset = UNSET
    impacts: list[ImpactAwardableAssociation] | None | Unset = UNSET
    research_outputs: list[ResearchOutputAwardableAssociation] | None | Unset = UNSET
    student_theses: list[StudentThesisAwardableAssociation] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_cluster_ref_type_0 import ApplicationClusterRefType0
        from ..models.award_cluster_ref_type_0 import AwardClusterRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0

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

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

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

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        effective_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effective_period, Unset):
            effective_period = self.effective_period.to_dict()

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

        short_title: dict[str, Any] | None | Unset
        if isinstance(self.short_title, Unset):
            short_title = UNSET
        elif isinstance(self.short_title, LocalizedStringType0):
            short_title = self.short_title.to_dict()
        else:
            short_title = self.short_title

        total_academic_ownership = self.total_academic_ownership

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

        curtailed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.curtailed, Unset):
            curtailed = self.curtailed.to_dict()

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

        application_clusters: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.application_clusters, Unset):
            application_clusters = UNSET
        elif isinstance(self.application_clusters, list):
            application_clusters = []
            for application_clusters_type_0_item_data in self.application_clusters:
                application_clusters_type_0_item: dict[str, Any] | None
                if isinstance(
                    application_clusters_type_0_item_data, ApplicationClusterRefType0
                ):
                    application_clusters_type_0_item = (
                        application_clusters_type_0_item_data.to_dict()
                    )
                else:
                    application_clusters_type_0_item = (
                        application_clusters_type_0_item_data
                    )
                application_clusters.append(application_clusters_type_0_item)

        else:
            application_clusters = self.application_clusters

        award_clusters: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.award_clusters, Unset):
            award_clusters = UNSET
        elif isinstance(self.award_clusters, list):
            award_clusters = []
            for award_clusters_type_0_item_data in self.award_clusters:
                award_clusters_type_0_item: dict[str, Any] | None
                if isinstance(award_clusters_type_0_item_data, AwardClusterRefType0):
                    award_clusters_type_0_item = (
                        award_clusters_type_0_item_data.to_dict()
                    )
                else:
                    award_clusters_type_0_item = award_clusters_type_0_item_data
                award_clusters.append(award_clusters_type_0_item)

        else:
            award_clusters = self.award_clusters

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

        press_medias: list[dict[str, Any]] | None | Unset
        if isinstance(self.press_medias, Unset):
            press_medias = UNSET
        elif isinstance(self.press_medias, list):
            press_medias = []
            for press_medias_type_0_item_data in self.press_medias:
                press_medias_type_0_item = press_medias_type_0_item_data.to_dict()
                press_medias.append(press_medias_type_0_item)

        else:
            press_medias = self.press_medias

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

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if participants is not UNSET:
            field_dict["participants"] = participants
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if co_managing_organizations is not UNSET:
            field_dict["coManagingOrganizations"] = co_managing_organizations
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if period is not UNSET:
            field_dict["period"] = period
        if effective_period is not UNSET:
            field_dict["effectivePeriod"] = effective_period
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if nature_types is not UNSET:
            field_dict["natureTypes"] = nature_types
        if short_title is not UNSET:
            field_dict["shortTitle"] = short_title
        if total_academic_ownership is not UNSET:
            field_dict["totalAcademicOwnership"] = total_academic_ownership
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if links is not UNSET:
            field_dict["links"] = links
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if documents is not UNSET:
            field_dict["documents"] = documents
        if curtailed is not UNSET:
            field_dict["curtailed"] = curtailed
        if projects is not UNSET:
            field_dict["projects"] = projects
        if application_clusters is not UNSET:
            field_dict["applicationClusters"] = application_clusters
        if award_clusters is not UNSET:
            field_dict["awardClusters"] = award_clusters
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if activities is not UNSET:
            field_dict["activities"] = activities
        if press_medias is not UNSET:
            field_dict["pressMedias"] = press_medias
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if student_theses is not UNSET:
            field_dict["studentTheses"] = student_theses
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if images is not UNSET:
            field_dict["images"] = images
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_participant_association import (
            AbstractParticipantAssociation,
        )
        from ..models.activity_awardable_association import ActivityAwardableAssociation
        from ..models.application_cluster_ref_type_0 import ApplicationClusterRefType0
        from ..models.award_cluster_ref_type_0 import AwardClusterRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.collaborator_association import CollaboratorAssociation
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.data_set_awardable_association import DataSetAwardableAssociation
        from ..models.date_range import DateRange
        from ..models.deprecated_date_range import DeprecatedDateRange
        from ..models.document import Document
        from ..models.equipment_awardable_association import (
            EquipmentAwardableAssociation,
        )
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.impact_awardable_association import ImpactAwardableAssociation
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.press_media_awardable_association import (
            PressMediaAwardableAssociation,
        )
        from ..models.prize_awardable_association import PrizeAwardableAssociation
        from ..models.project_association import ProjectAssociation
        from ..models.project_curtailed import ProjectCurtailed
        from ..models.research_output_awardable_association import (
            ResearchOutputAwardableAssociation,
        )
        from ..models.student_thesis_awardable_association import (
            StudentThesisAwardableAssociation,
        )
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)
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

        _participants = d.pop("participants", UNSET)
        participants: list[AbstractParticipantAssociation] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = AbstractParticipantAssociation.from_dict(
                    participants_item_data
                )

                participants.append(participants_item)

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

        _period = d.pop("period", UNSET)
        period: DateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = DateRange.from_dict(_period)

        _effective_period = d.pop("effectivePeriod", UNSET)
        effective_period: DeprecatedDateRange | Unset
        if isinstance(_effective_period, Unset):
            effective_period = UNSET
        else:
            effective_period = DeprecatedDateRange.from_dict(_effective_period)

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

        _curtailed = d.pop("curtailed", UNSET)
        curtailed: ProjectCurtailed | Unset
        if isinstance(_curtailed, Unset):
            curtailed = UNSET
        else:
            curtailed = ProjectCurtailed.from_dict(_curtailed)

        def _parse_projects(data: object) -> list[ProjectAssociation] | None | Unset:
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
                    projects_type_0_item = ProjectAssociation.from_dict(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProjectAssociation] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_application_clusters(
            data: object,
        ) -> list[ApplicationClusterRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                application_clusters_type_0 = []
                _application_clusters_type_0 = data
                for (
                    application_clusters_type_0_item_data
                ) in _application_clusters_type_0:

                    def _parse_application_clusters_type_0_item(
                        data: object,
                    ) -> ApplicationClusterRefType0 | None:
                        if data is None:
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
                        return cast(ApplicationClusterRefType0 | None, data)

                    application_clusters_type_0_item = (
                        _parse_application_clusters_type_0_item(
                            application_clusters_type_0_item_data
                        )
                    )

                    application_clusters_type_0.append(application_clusters_type_0_item)

                return application_clusters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplicationClusterRefType0 | None] | None | Unset, data)

        application_clusters = _parse_application_clusters(
            d.pop("applicationClusters", UNSET)
        )

        def _parse_award_clusters(
            data: object,
        ) -> list[AwardClusterRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                award_clusters_type_0 = []
                _award_clusters_type_0 = data
                for award_clusters_type_0_item_data in _award_clusters_type_0:

                    def _parse_award_clusters_type_0_item(
                        data: object,
                    ) -> AwardClusterRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_award_cluster_ref_type_0 = (
                                AwardClusterRefType0.from_dict(data)
                            )

                            return componentsschemas_award_cluster_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(AwardClusterRefType0 | None, data)

                    award_clusters_type_0_item = _parse_award_clusters_type_0_item(
                        award_clusters_type_0_item_data
                    )

                    award_clusters_type_0.append(award_clusters_type_0_item)

                return award_clusters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AwardClusterRefType0 | None] | None | Unset, data)

        award_clusters = _parse_award_clusters(d.pop("awardClusters", UNSET))

        def _parse_data_sets(
            data: object,
        ) -> list[DataSetAwardableAssociation] | None | Unset:
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
                    data_sets_type_0_item = DataSetAwardableAssociation.from_dict(
                        data_sets_type_0_item_data
                    )

                    data_sets_type_0.append(data_sets_type_0_item)

                return data_sets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetAwardableAssociation] | None | Unset, data)

        data_sets = _parse_data_sets(d.pop("dataSets", UNSET))

        def _parse_prizes(
            data: object,
        ) -> list[PrizeAwardableAssociation] | None | Unset:
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
                    prizes_type_0_item = PrizeAwardableAssociation.from_dict(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrizeAwardableAssociation] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_activities(
            data: object,
        ) -> list[ActivityAwardableAssociation] | None | Unset:
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
                    activities_type_0_item = ActivityAwardableAssociation.from_dict(
                        activities_type_0_item_data
                    )

                    activities_type_0.append(activities_type_0_item)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityAwardableAssociation] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_press_medias(
            data: object,
        ) -> list[PressMediaAwardableAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                press_medias_type_0 = []
                _press_medias_type_0 = data
                for press_medias_type_0_item_data in _press_medias_type_0:
                    press_medias_type_0_item = PressMediaAwardableAssociation.from_dict(
                        press_medias_type_0_item_data
                    )

                    press_medias_type_0.append(press_medias_type_0_item)

                return press_medias_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaAwardableAssociation] | None | Unset, data)

        press_medias = _parse_press_medias(d.pop("pressMedias", UNSET))

        def _parse_equipment(
            data: object,
        ) -> list[EquipmentAwardableAssociation] | None | Unset:
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
                    equipment_type_0_item = EquipmentAwardableAssociation.from_dict(
                        equipment_type_0_item_data
                    )

                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentAwardableAssociation] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))

        def _parse_impacts(
            data: object,
        ) -> list[ImpactAwardableAssociation] | None | Unset:
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
                    impacts_type_0_item = ImpactAwardableAssociation.from_dict(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImpactAwardableAssociation] | None | Unset, data)

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[ResearchOutputAwardableAssociation] | None | Unset:
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
                        ResearchOutputAwardableAssociation.from_dict(
                            research_outputs_type_0_item_data
                        )
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResearchOutputAwardableAssociation] | None | Unset, data)

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

        def _parse_student_theses(
            data: object,
        ) -> list[StudentThesisAwardableAssociation] | None | Unset:
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
                        StudentThesisAwardableAssociation.from_dict(
                            student_theses_type_0_item_data
                        )
                    )

                    student_theses_type_0.append(student_theses_type_0_item)

                return student_theses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StudentThesisAwardableAssociation] | None | Unset, data)

        student_theses = _parse_student_theses(d.pop("studentTheses", UNSET))

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

        system_name = d.pop("systemName", UNSET)

        basic_project = cls(
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
            participants=participants,
            external_organizations=external_organizations,
            co_managing_organizations=co_managing_organizations,
            collaborators=collaborators,
            descriptions=descriptions,
            period=period,
            effective_period=effective_period,
            identifiers=identifiers,
            nature_types=nature_types,
            short_title=short_title,
            total_academic_ownership=total_academic_ownership,
            workflow=workflow,
            visibility=visibility,
            links=links,
            keyword_groups=keyword_groups,
            documents=documents,
            curtailed=curtailed,
            projects=projects,
            application_clusters=application_clusters,
            award_clusters=award_clusters,
            data_sets=data_sets,
            prizes=prizes,
            activities=activities,
            press_medias=press_medias,
            equipment=equipment,
            impacts=impacts,
            research_outputs=research_outputs,
            student_theses=student_theses,
            custom_defined_fields=custom_defined_fields,
            images=images,
            system_name=system_name,
        )

        basic_project.additional_properties = d
        return basic_project

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
