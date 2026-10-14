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
    from ..models.classified_course_developed_by_association import (
        ClassifiedCourseDevelopedByAssociation,
    )
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.course_file import CourseFile
    from ..models.course_occurrence import CourseOccurrence
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.date_range import DateRange
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Course")


@_attrs_define
class Course:
    """A course.

    Attributes:
        title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
        implemented_start_end_date (DateRange): A date range
        workflow (Workflow): Information about workflow
        type_ (ClassificationRefType0 | None): A reference to a classification value
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
        prefix (None | str | Unset): Course prefix (e.g., 'CS' in 'CS 101 A')
        number (None | str | Unset): Course number (e.g., '101' in 'CS 101 A')
        designation (None | str | Unset): Course designation (e.g., 'A' in 'CS 101 A')
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organization associations.
        level (ClassificationRefType0 | None | Unset): A reference to a classification value
        format_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        developed_by (list[ClassifiedCourseDevelopedByAssociation] | Unset): A collection of persons and/or
            organizations associated with the course
        course_occurrences (list[CourseOccurrence] | None | Unset): A collection of occurrences for the course
        language (ClassificationRefType0 | None | Unset): A reference to a classification value
        credit_count (float | None | Unset): The actual amount of credit given by the course
        credit_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        course_files (list[CourseFile] | None | Unset): A collection of files associated with the course
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the course
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        links (list[Link] | None | Unset): Additional links associated with this course
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the course
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A collection of descriptions.
        system_name (str | Unset): The content system name
    """

    title: LocalizedStringType0 | None
    managing_organization: None | OrganizationRefType0
    implemented_start_end_date: DateRange
    workflow: Workflow
    type_: ClassificationRefType0 | None
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
    prefix: None | str | Unset = UNSET
    number: None | str | Unset = UNSET
    designation: None | str | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    level: ClassificationRefType0 | None | Unset = UNSET
    format_: ClassificationRefType0 | None | Unset = UNSET
    developed_by: list[ClassifiedCourseDevelopedByAssociation] | Unset = UNSET
    course_occurrences: list[CourseOccurrence] | None | Unset = UNSET
    language: ClassificationRefType0 | None | Unset = UNSET
    credit_count: float | None | Unset = UNSET
    credit_type: ClassificationRefType0 | None | Unset = UNSET
    course_files: list[CourseFile] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0

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

        implemented_start_end_date = self.implemented_start_end_date.to_dict()

        workflow = self.workflow.to_dict()

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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

        prefix: None | str | Unset
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        number: None | str | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        designation: None | str | Unset
        if isinstance(self.designation, Unset):
            designation = UNSET
        else:
            designation = self.designation

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

        level: dict[str, Any] | None | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        elif isinstance(self.level, ClassificationRefType0):
            level = self.level.to_dict()
        else:
            level = self.level

        format_: dict[str, Any] | None | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        elif isinstance(self.format_, ClassificationRefType0):
            format_ = self.format_.to_dict()
        else:
            format_ = self.format_

        developed_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.developed_by, Unset):
            developed_by = []
            for developed_by_item_data in self.developed_by:
                developed_by_item = developed_by_item_data.to_dict()
                developed_by.append(developed_by_item)

        course_occurrences: list[dict[str, Any]] | None | Unset
        if isinstance(self.course_occurrences, Unset):
            course_occurrences = UNSET
        elif isinstance(self.course_occurrences, list):
            course_occurrences = []
            for course_occurrences_type_0_item_data in self.course_occurrences:
                course_occurrences_type_0_item = (
                    course_occurrences_type_0_item_data.to_dict()
                )
                course_occurrences.append(course_occurrences_type_0_item)

        else:
            course_occurrences = self.course_occurrences

        language: dict[str, Any] | None | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        elif isinstance(self.language, ClassificationRefType0):
            language = self.language.to_dict()
        else:
            language = self.language

        credit_count: float | None | Unset
        if isinstance(self.credit_count, Unset):
            credit_count = UNSET
        else:
            credit_count = self.credit_count

        credit_type: dict[str, Any] | None | Unset
        if isinstance(self.credit_type, Unset):
            credit_type = UNSET
        elif isinstance(self.credit_type, ClassificationRefType0):
            credit_type = self.credit_type.to_dict()
        else:
            credit_type = self.credit_type

        course_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.course_files, Unset):
            course_files = UNSET
        elif isinstance(self.course_files, list):
            course_files = []
            for course_files_type_0_item_data in self.course_files:
                course_files_type_0_item = course_files_type_0_item_data.to_dict()
                course_files.append(course_files_type_0_item)

        else:
            course_files = self.course_files

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "managingOrganization": managing_organization,
                "implementedStartEndDate": implemented_start_end_date,
                "workflow": workflow,
                "type": type_,
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
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if number is not UNSET:
            field_dict["number"] = number
        if designation is not UNSET:
            field_dict["designation"] = designation
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if level is not UNSET:
            field_dict["level"] = level
        if format_ is not UNSET:
            field_dict["format"] = format_
        if developed_by is not UNSET:
            field_dict["developedBy"] = developed_by
        if course_occurrences is not UNSET:
            field_dict["courseOccurrences"] = course_occurrences
        if language is not UNSET:
            field_dict["language"] = language
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count
        if credit_type is not UNSET:
            field_dict["creditType"] = credit_type
        if course_files is not UNSET:
            field_dict["courseFiles"] = course_files
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if images is not UNSET:
            field_dict["images"] = images
        if links is not UNSET:
            field_dict["links"] = links
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_course_developed_by_association import (
            ClassifiedCourseDevelopedByAssociation,
        )
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.course_file import CourseFile
        from ..models.course_occurrence import CourseOccurrence
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.date_range import DateRange
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
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

        implemented_start_end_date = DateRange.from_dict(
            d.pop("implementedStartEndDate")
        )

        workflow = Workflow.from_dict(d.pop("workflow"))

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

        def _parse_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))

        def _parse_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_designation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        designation = _parse_designation(d.pop("designation", UNSET))

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

        def _parse_level(data: object) -> ClassificationRefType0 | None | Unset:
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

        level = _parse_level(d.pop("level", UNSET))

        def _parse_format_(data: object) -> ClassificationRefType0 | None | Unset:
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

        format_ = _parse_format_(d.pop("format", UNSET))

        _developed_by = d.pop("developedBy", UNSET)
        developed_by: list[ClassifiedCourseDevelopedByAssociation] | Unset = UNSET
        if _developed_by is not UNSET:
            developed_by = []
            for developed_by_item_data in _developed_by:
                developed_by_item = ClassifiedCourseDevelopedByAssociation.from_dict(
                    developed_by_item_data
                )

                developed_by.append(developed_by_item)

        def _parse_course_occurrences(
            data: object,
        ) -> list[CourseOccurrence] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                course_occurrences_type_0 = []
                _course_occurrences_type_0 = data
                for course_occurrences_type_0_item_data in _course_occurrences_type_0:
                    course_occurrences_type_0_item = CourseOccurrence.from_dict(
                        course_occurrences_type_0_item_data
                    )

                    course_occurrences_type_0.append(course_occurrences_type_0_item)

                return course_occurrences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CourseOccurrence] | None | Unset, data)

        course_occurrences = _parse_course_occurrences(
            d.pop("courseOccurrences", UNSET)
        )

        def _parse_language(data: object) -> ClassificationRefType0 | None | Unset:
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

        language = _parse_language(d.pop("language", UNSET))

        def _parse_credit_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credit_count = _parse_credit_count(d.pop("creditCount", UNSET))

        def _parse_credit_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        credit_type = _parse_credit_type(d.pop("creditType", UNSET))

        def _parse_course_files(data: object) -> list[CourseFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                course_files_type_0 = []
                _course_files_type_0 = data
                for course_files_type_0_item_data in _course_files_type_0:
                    course_files_type_0_item = CourseFile.from_dict(
                        course_files_type_0_item_data
                    )

                    course_files_type_0.append(course_files_type_0_item)

                return course_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CourseFile] | None | Unset, data)

        course_files = _parse_course_files(d.pop("courseFiles", UNSET))

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

        system_name = d.pop("systemName", UNSET)

        course = cls(
            title=title,
            managing_organization=managing_organization,
            implemented_start_end_date=implemented_start_end_date,
            workflow=workflow,
            type_=type_,
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
            prefix=prefix,
            number=number,
            designation=designation,
            organizations=organizations,
            level=level,
            format_=format_,
            developed_by=developed_by,
            course_occurrences=course_occurrences,
            language=language,
            credit_count=credit_count,
            credit_type=credit_type,
            course_files=course_files,
            keyword_groups=keyword_groups,
            images=images,
            links=links,
            custom_defined_fields=custom_defined_fields,
            identifiers=identifiers,
            descriptions=descriptions,
            system_name=system_name,
        )

        course.additional_properties = d
        return course

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
