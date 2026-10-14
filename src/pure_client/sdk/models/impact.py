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
    from ..models.abstract_impact_classified_participant_association import (
        AbstractImpactClassifiedParticipantAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.compound_date_type_0 import CompoundDateType0
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.document import Document
    from ..models.equipment_impact_association import EquipmentImpactAssociation
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.impact_activity_association import ImpactActivityAssociation
    from ..models.impact_data_set_association import ImpactDataSetAssociation
    from ..models.impact_evidence import ImpactEvidence
    from ..models.impact_impact_association import ImpactImpactAssociation
    from ..models.impact_press_media_association import ImpactPressMediaAssociation
    from ..models.impact_prize_association import ImpactPrizeAssociation
    from ..models.impact_project_association import ImpactProjectAssociation
    from ..models.impact_research_output_association import (
        ImpactResearchOutputAssociation,
    )
    from ..models.impact_student_thesis_association import (
        ImpactStudentThesisAssociation,
    )
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Impact")


@_attrs_define
class Impact:
    """Impact

    Attributes:
        impact_status (ClassificationRefType0 | None): A reference to a classification value
        title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        type_ (ClassificationRefType0 | None): A reference to a classification value
        organizations (list[None | OrganizationRefType0]): A collection of organizational unit affiliations.
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
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
        start_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and month or a full
            date
        end_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and month or a full
            date
        impact_category (list[ClassificationRefType0 | None] | Unset):
        impact_level (ClassificationRefType0 | None | Unset): A reference to a classification value
        impact_evidence (list[ImpactEvidence] | Unset):
        persons (list[AbstractImpactClassifiedParticipantAssociation] | Unset):
        related_impacts (list[ImpactImpactAssociation] | Unset):
        research_output_relations (list[ImpactResearchOutputAssociation] | Unset):
        activity_relations (list[ImpactActivityAssociation] | Unset):
        press_media_relations (list[ImpactPressMediaAssociation] | Unset):
        student_thesis_relations (list[ImpactStudentThesisAssociation] | Unset):
        equipment_relations (list[EquipmentImpactAssociation] | Unset):
        visibility (Visibility | Unset): Visibility of an object
        documents (list[Document] | Unset):
        links (list[Link] | Unset):
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the impact.
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions for the
            impact. Query the /impacts/allowed-description-types endpoint for allowed types.
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the impact.
        data_sets (list[ImpactDataSetAssociation] | Unset):
        prizes (list[ImpactPrizeAssociation] | Unset):
        projects (list[ImpactProjectAssociation] | Unset):
        system_name (str | Unset): The content system name
    """

    impact_status: ClassificationRefType0 | None
    title: LocalizedStringType0 | None
    type_: ClassificationRefType0 | None
    organizations: list[None | OrganizationRefType0]
    managing_organization: None | OrganizationRefType0
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
    start_date: CompoundDateType0 | None | Unset = UNSET
    end_date: CompoundDateType0 | None | Unset = UNSET
    impact_category: list[ClassificationRefType0 | None] | Unset = UNSET
    impact_level: ClassificationRefType0 | None | Unset = UNSET
    impact_evidence: list[ImpactEvidence] | Unset = UNSET
    persons: list[AbstractImpactClassifiedParticipantAssociation] | Unset = UNSET
    related_impacts: list[ImpactImpactAssociation] | Unset = UNSET
    research_output_relations: list[ImpactResearchOutputAssociation] | Unset = UNSET
    activity_relations: list[ImpactActivityAssociation] | Unset = UNSET
    press_media_relations: list[ImpactPressMediaAssociation] | Unset = UNSET
    student_thesis_relations: list[ImpactStudentThesisAssociation] | Unset = UNSET
    equipment_relations: list[EquipmentImpactAssociation] | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    documents: list[Document] | Unset = UNSET
    links: list[Link] | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    identifiers: list[Identifier] | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    data_sets: list[ImpactDataSetAssociation] | Unset = UNSET
    prizes: list[ImpactPrizeAssociation] | Unset = UNSET
    projects: list[ImpactProjectAssociation] | Unset = UNSET
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

        impact_status: dict[str, Any] | None
        if isinstance(self.impact_status, ClassificationRefType0):
            impact_status = self.impact_status.to_dict()
        else:
            impact_status = self.impact_status

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

        start_date: dict[str, Any] | None | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, CompoundDateType0):
            start_date = self.start_date.to_dict()
        else:
            start_date = self.start_date

        end_date: dict[str, Any] | None | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, CompoundDateType0):
            end_date = self.end_date.to_dict()
        else:
            end_date = self.end_date

        impact_category: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.impact_category, Unset):
            impact_category = []
            for impact_category_item_data in self.impact_category:
                impact_category_item: dict[str, Any] | None
                if isinstance(impact_category_item_data, ClassificationRefType0):
                    impact_category_item = impact_category_item_data.to_dict()
                else:
                    impact_category_item = impact_category_item_data
                impact_category.append(impact_category_item)

        impact_level: dict[str, Any] | None | Unset
        if isinstance(self.impact_level, Unset):
            impact_level = UNSET
        elif isinstance(self.impact_level, ClassificationRefType0):
            impact_level = self.impact_level.to_dict()
        else:
            impact_level = self.impact_level

        impact_evidence: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.impact_evidence, Unset):
            impact_evidence = []
            for impact_evidence_item_data in self.impact_evidence:
                impact_evidence_item = impact_evidence_item_data.to_dict()
                impact_evidence.append(impact_evidence_item)

        persons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        related_impacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.related_impacts, Unset):
            related_impacts = []
            for related_impacts_item_data in self.related_impacts:
                related_impacts_item = related_impacts_item_data.to_dict()
                related_impacts.append(related_impacts_item)

        research_output_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_output_relations, Unset):
            research_output_relations = []
            for research_output_relations_item_data in self.research_output_relations:
                research_output_relations_item = (
                    research_output_relations_item_data.to_dict()
                )
                research_output_relations.append(research_output_relations_item)

        activity_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activity_relations, Unset):
            activity_relations = []
            for activity_relations_item_data in self.activity_relations:
                activity_relations_item = activity_relations_item_data.to_dict()
                activity_relations.append(activity_relations_item)

        press_media_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.press_media_relations, Unset):
            press_media_relations = []
            for press_media_relations_item_data in self.press_media_relations:
                press_media_relations_item = press_media_relations_item_data.to_dict()
                press_media_relations.append(press_media_relations_item)

        student_thesis_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.student_thesis_relations, Unset):
            student_thesis_relations = []
            for student_thesis_relations_item_data in self.student_thesis_relations:
                student_thesis_relations_item = (
                    student_thesis_relations_item_data.to_dict()
                )
                student_thesis_relations.append(student_thesis_relations_item)

        equipment_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.equipment_relations, Unset):
            equipment_relations = []
            for equipment_relations_item_data in self.equipment_relations:
                equipment_relations_item = equipment_relations_item_data.to_dict()
                equipment_relations.append(equipment_relations_item)

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

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

        data_sets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = []
            for data_sets_item_data in self.data_sets:
                data_sets_item = data_sets_item_data.to_dict()
                data_sets.append(data_sets_item)

        prizes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prizes, Unset):
            prizes = []
            for prizes_item_data in self.prizes:
                prizes_item = prizes_item_data.to_dict()
                prizes.append(prizes_item)

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "impactStatus": impact_status,
                "title": title,
                "type": type_,
                "organizations": organizations,
                "managingOrganization": managing_organization,
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
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if impact_category is not UNSET:
            field_dict["impactCategory"] = impact_category
        if impact_level is not UNSET:
            field_dict["impactLevel"] = impact_level
        if impact_evidence is not UNSET:
            field_dict["impactEvidence"] = impact_evidence
        if persons is not UNSET:
            field_dict["persons"] = persons
        if related_impacts is not UNSET:
            field_dict["relatedImpacts"] = related_impacts
        if research_output_relations is not UNSET:
            field_dict["researchOutputRelations"] = research_output_relations
        if activity_relations is not UNSET:
            field_dict["activityRelations"] = activity_relations
        if press_media_relations is not UNSET:
            field_dict["pressMediaRelations"] = press_media_relations
        if student_thesis_relations is not UNSET:
            field_dict["studentThesisRelations"] = student_thesis_relations
        if equipment_relations is not UNSET:
            field_dict["equipmentRelations"] = equipment_relations
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if documents is not UNSET:
            field_dict["documents"] = documents
        if links is not UNSET:
            field_dict["links"] = links
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if images is not UNSET:
            field_dict["images"] = images
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if projects is not UNSET:
            field_dict["projects"] = projects
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_impact_classified_participant_association import (
            AbstractImpactClassifiedParticipantAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.document import Document
        from ..models.equipment_impact_association import EquipmentImpactAssociation
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.impact_activity_association import ImpactActivityAssociation
        from ..models.impact_data_set_association import ImpactDataSetAssociation
        from ..models.impact_evidence import ImpactEvidence
        from ..models.impact_impact_association import ImpactImpactAssociation
        from ..models.impact_press_media_association import ImpactPressMediaAssociation
        from ..models.impact_prize_association import ImpactPrizeAssociation
        from ..models.impact_project_association import ImpactProjectAssociation
        from ..models.impact_research_output_association import (
            ImpactResearchOutputAssociation,
        )
        from ..models.impact_student_thesis_association import (
            ImpactStudentThesisAssociation,
        )
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)

        def _parse_impact_status(data: object) -> ClassificationRefType0 | None:
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

        impact_status = _parse_impact_status(d.pop("impactStatus"))

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

        def _parse_start_date(data: object) -> CompoundDateType0 | None | Unset:
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

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> CompoundDateType0 | None | Unset:
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

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        _impact_category = d.pop("impactCategory", UNSET)
        impact_category: list[ClassificationRefType0 | None] | Unset = UNSET
        if _impact_category is not UNSET:
            impact_category = []
            for impact_category_item_data in _impact_category:

                def _parse_impact_category_item(
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

                impact_category_item = _parse_impact_category_item(
                    impact_category_item_data
                )

                impact_category.append(impact_category_item)

        def _parse_impact_level(data: object) -> ClassificationRefType0 | None | Unset:
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

        impact_level = _parse_impact_level(d.pop("impactLevel", UNSET))

        _impact_evidence = d.pop("impactEvidence", UNSET)
        impact_evidence: list[ImpactEvidence] | Unset = UNSET
        if _impact_evidence is not UNSET:
            impact_evidence = []
            for impact_evidence_item_data in _impact_evidence:
                impact_evidence_item = ImpactEvidence.from_dict(
                    impact_evidence_item_data
                )

                impact_evidence.append(impact_evidence_item)

        _persons = d.pop("persons", UNSET)
        persons: list[AbstractImpactClassifiedParticipantAssociation] | Unset = UNSET
        if _persons is not UNSET:
            persons = []
            for persons_item_data in _persons:
                persons_item = AbstractImpactClassifiedParticipantAssociation.from_dict(
                    persons_item_data
                )

                persons.append(persons_item)

        _related_impacts = d.pop("relatedImpacts", UNSET)
        related_impacts: list[ImpactImpactAssociation] | Unset = UNSET
        if _related_impacts is not UNSET:
            related_impacts = []
            for related_impacts_item_data in _related_impacts:
                related_impacts_item = ImpactImpactAssociation.from_dict(
                    related_impacts_item_data
                )

                related_impacts.append(related_impacts_item)

        _research_output_relations = d.pop("researchOutputRelations", UNSET)
        research_output_relations: list[ImpactResearchOutputAssociation] | Unset = UNSET
        if _research_output_relations is not UNSET:
            research_output_relations = []
            for research_output_relations_item_data in _research_output_relations:
                research_output_relations_item = (
                    ImpactResearchOutputAssociation.from_dict(
                        research_output_relations_item_data
                    )
                )

                research_output_relations.append(research_output_relations_item)

        _activity_relations = d.pop("activityRelations", UNSET)
        activity_relations: list[ImpactActivityAssociation] | Unset = UNSET
        if _activity_relations is not UNSET:
            activity_relations = []
            for activity_relations_item_data in _activity_relations:
                activity_relations_item = ImpactActivityAssociation.from_dict(
                    activity_relations_item_data
                )

                activity_relations.append(activity_relations_item)

        _press_media_relations = d.pop("pressMediaRelations", UNSET)
        press_media_relations: list[ImpactPressMediaAssociation] | Unset = UNSET
        if _press_media_relations is not UNSET:
            press_media_relations = []
            for press_media_relations_item_data in _press_media_relations:
                press_media_relations_item = ImpactPressMediaAssociation.from_dict(
                    press_media_relations_item_data
                )

                press_media_relations.append(press_media_relations_item)

        _student_thesis_relations = d.pop("studentThesisRelations", UNSET)
        student_thesis_relations: list[ImpactStudentThesisAssociation] | Unset = UNSET
        if _student_thesis_relations is not UNSET:
            student_thesis_relations = []
            for student_thesis_relations_item_data in _student_thesis_relations:
                student_thesis_relations_item = (
                    ImpactStudentThesisAssociation.from_dict(
                        student_thesis_relations_item_data
                    )
                )

                student_thesis_relations.append(student_thesis_relations_item)

        _equipment_relations = d.pop("equipmentRelations", UNSET)
        equipment_relations: list[EquipmentImpactAssociation] | Unset = UNSET
        if _equipment_relations is not UNSET:
            equipment_relations = []
            for equipment_relations_item_data in _equipment_relations:
                equipment_relations_item = EquipmentImpactAssociation.from_dict(
                    equipment_relations_item_data
                )

                equipment_relations.append(equipment_relations_item)

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        _documents = d.pop("documents", UNSET)
        documents: list[Document] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = Document.from_dict(documents_item_data)

                documents.append(documents_item)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

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

        _data_sets = d.pop("dataSets", UNSET)
        data_sets: list[ImpactDataSetAssociation] | Unset = UNSET
        if _data_sets is not UNSET:
            data_sets = []
            for data_sets_item_data in _data_sets:
                data_sets_item = ImpactDataSetAssociation.from_dict(data_sets_item_data)

                data_sets.append(data_sets_item)

        _prizes = d.pop("prizes", UNSET)
        prizes: list[ImpactPrizeAssociation] | Unset = UNSET
        if _prizes is not UNSET:
            prizes = []
            for prizes_item_data in _prizes:
                prizes_item = ImpactPrizeAssociation.from_dict(prizes_item_data)

                prizes.append(prizes_item)

        _projects = d.pop("projects", UNSET)
        projects: list[ImpactProjectAssociation] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = ImpactProjectAssociation.from_dict(projects_item_data)

                projects.append(projects_item)

        system_name = d.pop("systemName", UNSET)

        impact = cls(
            impact_status=impact_status,
            title=title,
            type_=type_,
            organizations=organizations,
            managing_organization=managing_organization,
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
            start_date=start_date,
            end_date=end_date,
            impact_category=impact_category,
            impact_level=impact_level,
            impact_evidence=impact_evidence,
            persons=persons,
            related_impacts=related_impacts,
            research_output_relations=research_output_relations,
            activity_relations=activity_relations,
            press_media_relations=press_media_relations,
            student_thesis_relations=student_thesis_relations,
            equipment_relations=equipment_relations,
            visibility=visibility,
            documents=documents,
            links=links,
            external_organizations=external_organizations,
            identifiers=identifiers,
            descriptions=descriptions,
            custom_defined_fields=custom_defined_fields,
            images=images,
            keyword_groups=keyword_groups,
            data_sets=data_sets,
            prizes=prizes,
            projects=projects,
            system_name=system_name,
        )

        impact.additional_properties = d
        return impact

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
