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
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.event_ref_type_0 import EventRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.media_coverage import MediaCoverage
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.press_media_activity_association import PressMediaActivityAssociation
    from ..models.press_media_data_set_association import PressMediaDataSetAssociation
    from ..models.press_media_equipment_association import (
        PressMediaEquipmentAssociation,
    )
    from ..models.press_media_impact_association import PressMediaImpactAssociation
    from ..models.press_media_press_media_association import (
        PressMediaPressMediaAssociation,
    )
    from ..models.press_media_prize_association import PressMediaPrizeAssociation
    from ..models.press_media_project_association import PressMediaProjectAssociation
    from ..models.press_media_research_output_association import (
        PressMediaResearchOutputAssociation,
    )
    from ..models.press_media_student_thesis_association import (
        PressMediaStudentThesisAssociation,
    )
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="PressMedia")


@_attrs_define
class PressMedia:
    """A piece of press, media, or other sort of news clipping.

    Attributes:
        title (FormattedLocalizedStringType0 | None): A set of localized strings that support formatting. Invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        media_coverages (list[MediaCoverage]): MediaCoverages
        type_ (ClassificationRefType0 | None): A reference to a classification value
        visibility (Visibility): Visibility of an object
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
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the press media.
        event (EventRefType0 | None | Unset): A reference to an event
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A list of descriptions for this press
            media. Query the relevant /press-media/allowed-*-description-types endpoint for allowed types.
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        managing_organization (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
        identifiers (list[Identifier] | None | Unset): Identifiers related to the project.
        activities (list[PressMediaActivityAssociation] | None | Unset): A collection of related activities.
        data_sets (list[PressMediaDataSetAssociation] | None | Unset): A collection of related datasets.
        equipment (list[PressMediaEquipmentAssociation] | None | Unset): A collection of related equipment.
        impacts (list[PressMediaImpactAssociation] | None | Unset): A collection of related impacts.
        press_media (list[PressMediaPressMediaAssociation] | None | Unset): A collection of related press media.
        prizes (list[PressMediaPrizeAssociation] | None | Unset): A collection of related prizes.
        projects (list[PressMediaProjectAssociation] | None | Unset): A collection of related projects.
        research_outputs (list[PressMediaResearchOutputAssociation] | None | Unset): A collection of related research
            outputs.
        student_theses (list[PressMediaStudentThesisAssociation] | None | Unset): A collection of related student
            theses.
        system_name (str | Unset): The content system name
    """

    title: FormattedLocalizedStringType0 | None
    media_coverages: list[MediaCoverage]
    type_: ClassificationRefType0 | None
    visibility: Visibility
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
    category: ClassificationRefType0 | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    event: EventRefType0 | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    managing_organization: None | OrganizationRefType0 | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    activities: list[PressMediaActivityAssociation] | None | Unset = UNSET
    data_sets: list[PressMediaDataSetAssociation] | None | Unset = UNSET
    equipment: list[PressMediaEquipmentAssociation] | None | Unset = UNSET
    impacts: list[PressMediaImpactAssociation] | None | Unset = UNSET
    press_media: list[PressMediaPressMediaAssociation] | None | Unset = UNSET
    prizes: list[PressMediaPrizeAssociation] | None | Unset = UNSET
    projects: list[PressMediaProjectAssociation] | None | Unset = UNSET
    research_outputs: list[PressMediaResearchOutputAssociation] | None | Unset = UNSET
    student_theses: list[PressMediaStudentThesisAssociation] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        title: dict[str, Any] | None
        if isinstance(self.title, FormattedLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        media_coverages = []
        for media_coverages_item_data in self.media_coverages:
            media_coverages_item = media_coverages_item_data.to_dict()
            media_coverages.append(media_coverages_item)

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        visibility = self.visibility.to_dict()

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

        event: dict[str, Any] | None | Unset
        if isinstance(self.event, Unset):
            event = UNSET
        elif isinstance(self.event, EventRefType0):
            event = self.event.to_dict()
        else:
            event = self.event

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

        managing_organization: dict[str, Any] | None | Unset
        if isinstance(self.managing_organization, Unset):
            managing_organization = UNSET
        elif isinstance(self.managing_organization, OrganizationRefType0):
            managing_organization = self.managing_organization.to_dict()
        else:
            managing_organization = self.managing_organization

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "mediaCoverages": media_coverages,
                "type": type_,
                "visibility": visibility,
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
        if category is not UNSET:
            field_dict["category"] = category
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if event is not UNSET:
            field_dict["event"] = event
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if images is not UNSET:
            field_dict["images"] = images
        if managing_organization is not UNSET:
            field_dict["managingOrganization"] = managing_organization
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if activities is not UNSET:
            field_dict["activities"] = activities
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if projects is not UNSET:
            field_dict["projects"] = projects
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if student_theses is not UNSET:
            field_dict["studentTheses"] = student_theses
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.media_coverage import MediaCoverage
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.press_media_activity_association import (
            PressMediaActivityAssociation,
        )
        from ..models.press_media_data_set_association import (
            PressMediaDataSetAssociation,
        )
        from ..models.press_media_equipment_association import (
            PressMediaEquipmentAssociation,
        )
        from ..models.press_media_impact_association import PressMediaImpactAssociation
        from ..models.press_media_press_media_association import (
            PressMediaPressMediaAssociation,
        )
        from ..models.press_media_prize_association import PressMediaPrizeAssociation
        from ..models.press_media_project_association import (
            PressMediaProjectAssociation,
        )
        from ..models.press_media_research_output_association import (
            PressMediaResearchOutputAssociation,
        )
        from ..models.press_media_student_thesis_association import (
            PressMediaStudentThesisAssociation,
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

        media_coverages = []
        _media_coverages = d.pop("mediaCoverages")
        for media_coverages_item_data in _media_coverages:
            media_coverages_item = MediaCoverage.from_dict(media_coverages_item_data)

            media_coverages.append(media_coverages_item)

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

        def _parse_managing_organization(
            data: object,
        ) -> None | OrganizationRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(None | OrganizationRefType0 | Unset, data)

        managing_organization = _parse_managing_organization(
            d.pop("managingOrganization", UNSET)
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

        def _parse_activities(
            data: object,
        ) -> list[PressMediaActivityAssociation] | None | Unset:
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
                    activities_type_0_item = PressMediaActivityAssociation.from_dict(
                        activities_type_0_item_data
                    )

                    activities_type_0.append(activities_type_0_item)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaActivityAssociation] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_data_sets(
            data: object,
        ) -> list[PressMediaDataSetAssociation] | None | Unset:
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
                    data_sets_type_0_item = PressMediaDataSetAssociation.from_dict(
                        data_sets_type_0_item_data
                    )

                    data_sets_type_0.append(data_sets_type_0_item)

                return data_sets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaDataSetAssociation] | None | Unset, data)

        data_sets = _parse_data_sets(d.pop("dataSets", UNSET))

        def _parse_equipment(
            data: object,
        ) -> list[PressMediaEquipmentAssociation] | None | Unset:
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
                    equipment_type_0_item = PressMediaEquipmentAssociation.from_dict(
                        equipment_type_0_item_data
                    )

                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaEquipmentAssociation] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))

        def _parse_impacts(
            data: object,
        ) -> list[PressMediaImpactAssociation] | None | Unset:
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
                    impacts_type_0_item = PressMediaImpactAssociation.from_dict(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaImpactAssociation] | None | Unset, data)

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_press_media(
            data: object,
        ) -> list[PressMediaPressMediaAssociation] | None | Unset:
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
                    press_media_type_0_item = PressMediaPressMediaAssociation.from_dict(
                        press_media_type_0_item_data
                    )

                    press_media_type_0.append(press_media_type_0_item)

                return press_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaPressMediaAssociation] | None | Unset, data)

        press_media = _parse_press_media(d.pop("pressMedia", UNSET))

        def _parse_prizes(
            data: object,
        ) -> list[PressMediaPrizeAssociation] | None | Unset:
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
                    prizes_type_0_item = PressMediaPrizeAssociation.from_dict(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaPrizeAssociation] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[PressMediaProjectAssociation] | None | Unset:
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
                    projects_type_0_item = PressMediaProjectAssociation.from_dict(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaProjectAssociation] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[PressMediaResearchOutputAssociation] | None | Unset:
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
                        PressMediaResearchOutputAssociation.from_dict(
                            research_outputs_type_0_item_data
                        )
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaResearchOutputAssociation] | None | Unset, data)

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

        def _parse_student_theses(
            data: object,
        ) -> list[PressMediaStudentThesisAssociation] | None | Unset:
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
                        PressMediaStudentThesisAssociation.from_dict(
                            student_theses_type_0_item_data
                        )
                    )

                    student_theses_type_0.append(student_theses_type_0_item)

                return student_theses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PressMediaStudentThesisAssociation] | None | Unset, data)

        student_theses = _parse_student_theses(d.pop("studentTheses", UNSET))

        system_name = d.pop("systemName", UNSET)

        press_media = cls(
            title=title,
            media_coverages=media_coverages,
            type_=type_,
            visibility=visibility,
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
            category=category,
            keyword_groups=keyword_groups,
            event=event,
            descriptions=descriptions,
            custom_defined_fields=custom_defined_fields,
            images=images,
            managing_organization=managing_organization,
            identifiers=identifiers,
            activities=activities,
            data_sets=data_sets,
            equipment=equipment,
            impacts=impacts,
            press_media=press_media,
            prizes=prizes,
            projects=projects,
            research_outputs=research_outputs,
            student_theses=student_theses,
            system_name=system_name,
        )

        press_media.additional_properties = d
        return press_media

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
