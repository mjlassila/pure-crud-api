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
    from ..models.abstract_student_thesis_contributor_association import (
        AbstractStudentThesisContributorAssociation,
    )
    from ..models.activity_ref_type_0 import ActivityRefType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.compound_date_type_0 import CompoundDateType0
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.data_set_ref_type_0 import DataSetRefType0
    from ..models.equipment_ref_type_0 import EquipmentRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.formatted_string import FormattedString
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.impact_ref_type_0 import ImpactRefType0
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.press_media_ref_type_0 import PressMediaRefType0
    from ..models.prize_ref_type_0 import PrizeRefType0
    from ..models.project_ref_type_0 import ProjectRefType0
    from ..models.research_output_ref_type_0 import ResearchOutputRefType0
    from ..models.student_thesis_document import StudentThesisDocument
    from ..models.supervisor_association import SupervisorAssociation
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="StudentThesis")


@_attrs_define
class StudentThesis:
    """A student thesis

    Attributes:
        title (FormattedString): A string containing HTML formatted text
        language (ClassificationRefType0 | None): A reference to a classification value
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
        type_ (ClassificationRefType0 | None): A reference to a classification value
        visibility (Visibility): Visibility of an object
        contributors (list[AbstractStudentThesisContributorAssociation]): Contributors and their affiliations
        award_date (CompoundDateType0 | None): A date that can be defined by only year, year and month or a full date
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
        sub_title (FormattedString | Unset): A string containing HTML formatted text
        translated_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support
            formatting. Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        translated_sub_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support
            formatting. Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        bibliographical_note (LocalizedStringType0 | None | Unset): A set of string values, one for each submission
            locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
        documents (list[StudentThesisDocument] | None | Unset): A collection of documents.
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organizational unit
            affiliations.
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        research_outputs (list[None | ResearchOutputRefType0] | None | Unset): A collection of related research outputs.
        activities (list[ActivityRefType0 | None] | None | Unset): A collection of related activities.
        press_media (list[None | PressMediaRefType0] | None | Unset): A collection of related press media.
        impacts (list[ImpactRefType0 | None] | None | Unset): A collection of related impacts.
        equipment (list[EquipmentRefType0 | None] | None | Unset): A collection of related equipment.
        projects (list[None | ProjectRefType0] | None | Unset): A collection of related projects.
        prizes (list[None | PrizeRefType0] | None | Unset): A collection of related prizes.
        datasets (list[DataSetRefType0 | None] | None | Unset): A collection of related datasets.
        links (list[Link] | None | Unset): A collection of links.
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        workflow (Workflow | Unset): Information about workflow
        supervisor_organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organizational
            affiliations associated with supervisors of this student thesis.
        supervisor_external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of
            external organization affiliations associated with supervisors of this research output.
        supervisors (list[SupervisorAssociation] | None | Unset): The supervisors of this student thesis.
        sponsors (list[ExternalOrganizationRefType0 | None] | None | Unset): The sponsors of this student thesis.
        awarding_institutions (list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset): The awarding
            institution.
        abstract (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        system_name (str | Unset): The content system name
    """

    title: FormattedString
    language: ClassificationRefType0 | None
    managing_organization: None | OrganizationRefType0
    type_: ClassificationRefType0 | None
    visibility: Visibility
    contributors: list[AbstractStudentThesisContributorAssociation]
    award_date: CompoundDateType0 | None
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
    sub_title: FormattedString | Unset = UNSET
    translated_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    translated_sub_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    bibliographical_note: LocalizedStringType0 | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    documents: list[StudentThesisDocument] | None | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    research_outputs: list[None | ResearchOutputRefType0] | None | Unset = UNSET
    activities: list[ActivityRefType0 | None] | None | Unset = UNSET
    press_media: list[None | PressMediaRefType0] | None | Unset = UNSET
    impacts: list[ImpactRefType0 | None] | None | Unset = UNSET
    equipment: list[EquipmentRefType0 | None] | None | Unset = UNSET
    projects: list[None | ProjectRefType0] | None | Unset = UNSET
    prizes: list[None | PrizeRefType0] | None | Unset = UNSET
    datasets: list[DataSetRefType0 | None] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    supervisor_organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    supervisor_external_organizations: (
        list[ExternalOrganizationRefType0 | None] | None | Unset
    ) = UNSET
    supervisors: list[SupervisorAssociation] | None | Unset = UNSET
    sponsors: list[ExternalOrganizationRefType0 | None] | None | Unset = UNSET
    awarding_institutions: (
        list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset
    ) = UNSET
    abstract: FormattedLocalizedStringType0 | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.data_set_ref_type_0 import DataSetRefType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.press_media_ref_type_0 import PressMediaRefType0
        from ..models.prize_ref_type_0 import PrizeRefType0
        from ..models.project_ref_type_0 import ProjectRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0

        title = self.title.to_dict()

        language: dict[str, Any] | None
        if isinstance(self.language, ClassificationRefType0):
            language = self.language.to_dict()
        else:
            language = self.language

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

        contributors = []
        for contributors_item_data in self.contributors:
            contributors_item = contributors_item_data.to_dict()
            contributors.append(contributors_item)

        award_date: dict[str, Any] | None
        if isinstance(self.award_date, CompoundDateType0):
            award_date = self.award_date.to_dict()
        else:
            award_date = self.award_date

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

        sub_title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_title, Unset):
            sub_title = self.sub_title.to_dict()

        translated_title: dict[str, Any] | None | Unset
        if isinstance(self.translated_title, Unset):
            translated_title = UNSET
        elif isinstance(self.translated_title, FormattedLocalizedStringType0):
            translated_title = self.translated_title.to_dict()
        else:
            translated_title = self.translated_title

        translated_sub_title: dict[str, Any] | None | Unset
        if isinstance(self.translated_sub_title, Unset):
            translated_sub_title = UNSET
        elif isinstance(self.translated_sub_title, FormattedLocalizedStringType0):
            translated_sub_title = self.translated_sub_title.to_dict()
        else:
            translated_sub_title = self.translated_sub_title

        bibliographical_note: dict[str, Any] | None | Unset
        if isinstance(self.bibliographical_note, Unset):
            bibliographical_note = UNSET
        elif isinstance(self.bibliographical_note, LocalizedStringType0):
            bibliographical_note = self.bibliographical_note.to_dict()
        else:
            bibliographical_note = self.bibliographical_note

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

        projects: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item: dict[str, Any] | None
                if isinstance(projects_type_0_item_data, ProjectRefType0):
                    projects_type_0_item = projects_type_0_item_data.to_dict()
                else:
                    projects_type_0_item = projects_type_0_item_data
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        prizes: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.prizes, Unset):
            prizes = UNSET
        elif isinstance(self.prizes, list):
            prizes = []
            for prizes_type_0_item_data in self.prizes:
                prizes_type_0_item: dict[str, Any] | None
                if isinstance(prizes_type_0_item_data, PrizeRefType0):
                    prizes_type_0_item = prizes_type_0_item_data.to_dict()
                else:
                    prizes_type_0_item = prizes_type_0_item_data
                prizes.append(prizes_type_0_item)

        else:
            prizes = self.prizes

        datasets: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.datasets, Unset):
            datasets = UNSET
        elif isinstance(self.datasets, list):
            datasets = []
            for datasets_type_0_item_data in self.datasets:
                datasets_type_0_item: dict[str, Any] | None
                if isinstance(datasets_type_0_item_data, DataSetRefType0):
                    datasets_type_0_item = datasets_type_0_item_data.to_dict()
                else:
                    datasets_type_0_item = datasets_type_0_item_data
                datasets.append(datasets_type_0_item)

        else:
            datasets = self.datasets

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

        supervisor_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.supervisor_organizations, Unset):
            supervisor_organizations = UNSET
        elif isinstance(self.supervisor_organizations, list):
            supervisor_organizations = []
            for (
                supervisor_organizations_type_0_item_data
            ) in self.supervisor_organizations:
                supervisor_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    supervisor_organizations_type_0_item_data, OrganizationRefType0
                ):
                    supervisor_organizations_type_0_item = (
                        supervisor_organizations_type_0_item_data.to_dict()
                    )
                else:
                    supervisor_organizations_type_0_item = (
                        supervisor_organizations_type_0_item_data
                    )
                supervisor_organizations.append(supervisor_organizations_type_0_item)

        else:
            supervisor_organizations = self.supervisor_organizations

        supervisor_external_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.supervisor_external_organizations, Unset):
            supervisor_external_organizations = UNSET
        elif isinstance(self.supervisor_external_organizations, list):
            supervisor_external_organizations = []
            for (
                supervisor_external_organizations_type_0_item_data
            ) in self.supervisor_external_organizations:
                supervisor_external_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    supervisor_external_organizations_type_0_item_data,
                    ExternalOrganizationRefType0,
                ):
                    supervisor_external_organizations_type_0_item = (
                        supervisor_external_organizations_type_0_item_data.to_dict()
                    )
                else:
                    supervisor_external_organizations_type_0_item = (
                        supervisor_external_organizations_type_0_item_data
                    )
                supervisor_external_organizations.append(
                    supervisor_external_organizations_type_0_item
                )

        else:
            supervisor_external_organizations = self.supervisor_external_organizations

        supervisors: list[dict[str, Any]] | None | Unset
        if isinstance(self.supervisors, Unset):
            supervisors = UNSET
        elif isinstance(self.supervisors, list):
            supervisors = []
            for supervisors_type_0_item_data in self.supervisors:
                supervisors_type_0_item = supervisors_type_0_item_data.to_dict()
                supervisors.append(supervisors_type_0_item)

        else:
            supervisors = self.supervisors

        sponsors: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.sponsors, Unset):
            sponsors = UNSET
        elif isinstance(self.sponsors, list):
            sponsors = []
            for sponsors_type_0_item_data in self.sponsors:
                sponsors_type_0_item: dict[str, Any] | None
                if isinstance(sponsors_type_0_item_data, ExternalOrganizationRefType0):
                    sponsors_type_0_item = sponsors_type_0_item_data.to_dict()
                else:
                    sponsors_type_0_item = sponsors_type_0_item_data
                sponsors.append(sponsors_type_0_item)

        else:
            sponsors = self.sponsors

        awarding_institutions: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.awarding_institutions, Unset):
            awarding_institutions = UNSET
        elif isinstance(self.awarding_institutions, list):
            awarding_institutions = []
            for awarding_institutions_type_0_item_data in self.awarding_institutions:
                awarding_institutions_type_0_item: dict[str, Any] | None
                if isinstance(
                    awarding_institutions_type_0_item_data,
                    OrganizationOrExternalOrganizationRefType0,
                ):
                    awarding_institutions_type_0_item = (
                        awarding_institutions_type_0_item_data.to_dict()
                    )
                else:
                    awarding_institutions_type_0_item = (
                        awarding_institutions_type_0_item_data
                    )
                awarding_institutions.append(awarding_institutions_type_0_item)

        else:
            awarding_institutions = self.awarding_institutions

        abstract: dict[str, Any] | None | Unset
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        elif isinstance(self.abstract, FormattedLocalizedStringType0):
            abstract = self.abstract.to_dict()
        else:
            abstract = self.abstract

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "language": language,
                "managingOrganization": managing_organization,
                "type": type_,
                "visibility": visibility,
                "contributors": contributors,
                "awardDate": award_date,
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
        if sub_title is not UNSET:
            field_dict["subTitle"] = sub_title
        if translated_title is not UNSET:
            field_dict["translatedTitle"] = translated_title
        if translated_sub_title is not UNSET:
            field_dict["translatedSubTitle"] = translated_sub_title
        if bibliographical_note is not UNSET:
            field_dict["bibliographicalNote"] = bibliographical_note
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if documents is not UNSET:
            field_dict["documents"] = documents
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if activities is not UNSET:
            field_dict["activities"] = activities
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if projects is not UNSET:
            field_dict["projects"] = projects
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if datasets is not UNSET:
            field_dict["datasets"] = datasets
        if links is not UNSET:
            field_dict["links"] = links
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if images is not UNSET:
            field_dict["images"] = images
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if supervisor_organizations is not UNSET:
            field_dict["supervisorOrganizations"] = supervisor_organizations
        if supervisor_external_organizations is not UNSET:
            field_dict["supervisorExternalOrganizations"] = (
                supervisor_external_organizations
            )
        if supervisors is not UNSET:
            field_dict["supervisors"] = supervisors
        if sponsors is not UNSET:
            field_dict["sponsors"] = sponsors
        if awarding_institutions is not UNSET:
            field_dict["awardingInstitutions"] = awarding_institutions
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_student_thesis_contributor_association import (
            AbstractStudentThesisContributorAssociation,
        )
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.data_set_ref_type_0 import DataSetRefType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.formatted_string import FormattedString
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.press_media_ref_type_0 import PressMediaRefType0
        from ..models.prize_ref_type_0 import PrizeRefType0
        from ..models.project_ref_type_0 import ProjectRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_document import StudentThesisDocument
        from ..models.supervisor_association import SupervisorAssociation
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)
        title = FormattedString.from_dict(d.pop("title"))

        def _parse_language(data: object) -> ClassificationRefType0 | None:
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

        language = _parse_language(d.pop("language"))

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

        contributors = []
        _contributors = d.pop("contributors")
        for contributors_item_data in _contributors:
            contributors_item = AbstractStudentThesisContributorAssociation.from_dict(
                contributors_item_data
            )

            contributors.append(contributors_item)

        def _parse_award_date(data: object) -> CompoundDateType0 | None:
            if data is None:
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
            return cast(CompoundDateType0 | None, data)

        award_date = _parse_award_date(d.pop("awardDate"))

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

        _sub_title = d.pop("subTitle", UNSET)
        sub_title: FormattedString | Unset
        if isinstance(_sub_title, Unset):
            sub_title = UNSET
        else:
            sub_title = FormattedString.from_dict(_sub_title)

        def _parse_translated_title(
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

        translated_title = _parse_translated_title(d.pop("translatedTitle", UNSET))

        def _parse_translated_sub_title(
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

        translated_sub_title = _parse_translated_sub_title(
            d.pop("translatedSubTitle", UNSET)
        )

        def _parse_bibliographical_note(
            data: object,
        ) -> LocalizedStringType0 | None | Unset:
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

        bibliographical_note = _parse_bibliographical_note(
            d.pop("bibliographicalNote", UNSET)
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

        def _parse_documents(
            data: object,
        ) -> list[StudentThesisDocument] | None | Unset:
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
                    documents_type_0_item = StudentThesisDocument.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StudentThesisDocument] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

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

        def _parse_projects(
            data: object,
        ) -> list[None | ProjectRefType0] | None | Unset:
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

                    def _parse_projects_type_0_item(
                        data: object,
                    ) -> None | ProjectRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_project_ref_type_0 = (
                                ProjectRefType0.from_dict(data)
                            )

                            return componentsschemas_project_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ProjectRefType0, data)

                    projects_type_0_item = _parse_projects_type_0_item(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | ProjectRefType0] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_prizes(data: object) -> list[None | PrizeRefType0] | None | Unset:
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

                    def _parse_prizes_type_0_item(data: object) -> None | PrizeRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_prize_ref_type_0 = (
                                PrizeRefType0.from_dict(data)
                            )

                            return componentsschemas_prize_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | PrizeRefType0, data)

                    prizes_type_0_item = _parse_prizes_type_0_item(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | PrizeRefType0] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_datasets(
            data: object,
        ) -> list[DataSetRefType0 | None] | None | Unset:
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

                    def _parse_datasets_type_0_item(
                        data: object,
                    ) -> DataSetRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_data_set_ref_type_0 = (
                                DataSetRefType0.from_dict(data)
                            )

                            return componentsschemas_data_set_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(DataSetRefType0 | None, data)

                    datasets_type_0_item = _parse_datasets_type_0_item(
                        datasets_type_0_item_data
                    )

                    datasets_type_0.append(datasets_type_0_item)

                return datasets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetRefType0 | None] | None | Unset, data)

        datasets = _parse_datasets(d.pop("datasets", UNSET))

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

        def _parse_supervisor_organizations(
            data: object,
        ) -> list[None | OrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supervisor_organizations_type_0 = []
                _supervisor_organizations_type_0 = data
                for (
                    supervisor_organizations_type_0_item_data
                ) in _supervisor_organizations_type_0:

                    def _parse_supervisor_organizations_type_0_item(
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

                    supervisor_organizations_type_0_item = (
                        _parse_supervisor_organizations_type_0_item(
                            supervisor_organizations_type_0_item_data
                        )
                    )

                    supervisor_organizations_type_0.append(
                        supervisor_organizations_type_0_item
                    )

                return supervisor_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | OrganizationRefType0] | None | Unset, data)

        supervisor_organizations = _parse_supervisor_organizations(
            d.pop("supervisorOrganizations", UNSET)
        )

        def _parse_supervisor_external_organizations(
            data: object,
        ) -> list[ExternalOrganizationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supervisor_external_organizations_type_0 = []
                _supervisor_external_organizations_type_0 = data
                for (
                    supervisor_external_organizations_type_0_item_data
                ) in _supervisor_external_organizations_type_0:

                    def _parse_supervisor_external_organizations_type_0_item(
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

                    supervisor_external_organizations_type_0_item = (
                        _parse_supervisor_external_organizations_type_0_item(
                            supervisor_external_organizations_type_0_item_data
                        )
                    )

                    supervisor_external_organizations_type_0.append(
                        supervisor_external_organizations_type_0_item
                    )

                return supervisor_external_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalOrganizationRefType0 | None] | None | Unset, data)

        supervisor_external_organizations = _parse_supervisor_external_organizations(
            d.pop("supervisorExternalOrganizations", UNSET)
        )

        def _parse_supervisors(
            data: object,
        ) -> list[SupervisorAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supervisors_type_0 = []
                _supervisors_type_0 = data
                for supervisors_type_0_item_data in _supervisors_type_0:
                    supervisors_type_0_item = SupervisorAssociation.from_dict(
                        supervisors_type_0_item_data
                    )

                    supervisors_type_0.append(supervisors_type_0_item)

                return supervisors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SupervisorAssociation] | None | Unset, data)

        supervisors = _parse_supervisors(d.pop("supervisors", UNSET))

        def _parse_sponsors(
            data: object,
        ) -> list[ExternalOrganizationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sponsors_type_0 = []
                _sponsors_type_0 = data
                for sponsors_type_0_item_data in _sponsors_type_0:

                    def _parse_sponsors_type_0_item(
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

                    sponsors_type_0_item = _parse_sponsors_type_0_item(
                        sponsors_type_0_item_data
                    )

                    sponsors_type_0.append(sponsors_type_0_item)

                return sponsors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalOrganizationRefType0 | None] | None | Unset, data)

        sponsors = _parse_sponsors(d.pop("sponsors", UNSET))

        def _parse_awarding_institutions(
            data: object,
        ) -> list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                awarding_institutions_type_0 = []
                _awarding_institutions_type_0 = data
                for (
                    awarding_institutions_type_0_item_data
                ) in _awarding_institutions_type_0:

                    def _parse_awarding_institutions_type_0_item(
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

                    awarding_institutions_type_0_item = (
                        _parse_awarding_institutions_type_0_item(
                            awarding_institutions_type_0_item_data
                        )
                    )

                    awarding_institutions_type_0.append(
                        awarding_institutions_type_0_item
                    )

                return awarding_institutions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset,
                data,
            )

        awarding_institutions = _parse_awarding_institutions(
            d.pop("awardingInstitutions", UNSET)
        )

        def _parse_abstract(
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

        abstract = _parse_abstract(d.pop("abstract", UNSET))

        system_name = d.pop("systemName", UNSET)

        student_thesis = cls(
            title=title,
            language=language,
            managing_organization=managing_organization,
            type_=type_,
            visibility=visibility,
            contributors=contributors,
            award_date=award_date,
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
            sub_title=sub_title,
            translated_title=translated_title,
            translated_sub_title=translated_sub_title,
            bibliographical_note=bibliographical_note,
            identifiers=identifiers,
            documents=documents,
            organizations=organizations,
            external_organizations=external_organizations,
            research_outputs=research_outputs,
            activities=activities,
            press_media=press_media,
            impacts=impacts,
            equipment=equipment,
            projects=projects,
            prizes=prizes,
            datasets=datasets,
            links=links,
            keyword_groups=keyword_groups,
            images=images,
            custom_defined_fields=custom_defined_fields,
            workflow=workflow,
            supervisor_organizations=supervisor_organizations,
            supervisor_external_organizations=supervisor_external_organizations,
            supervisors=supervisors,
            sponsors=sponsors,
            awarding_institutions=awarding_institutions,
            abstract=abstract,
            system_name=system_name,
        )

        student_thesis.additional_properties = d
        return student_thesis

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
