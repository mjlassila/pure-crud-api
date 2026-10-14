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
    from ..models.compound_date_type_0 import CompoundDateType0
    from ..models.education_association import EducationAssociation
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.student_project_appendix_document import (
        StudentProjectAppendixDocument,
    )
    from ..models.student_project_author import StudentProjectAuthor
    from ..models.student_project_document import StudentProjectDocument
    from ..models.student_project_external_collaborator import (
        StudentProjectExternalCollaborator,
    )
    from ..models.student_project_notification_recipient import (
        StudentProjectNotificationRecipient,
    )
    from ..models.student_project_supervisor import StudentProjectSupervisor
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="StudentProject")


@_attrs_define
class StudentProject:
    """A student project

    Attributes:
        has_supervisors (bool): Whether the student project has supervisors or not
        educations (list[EducationAssociation]): The educations of the student project
        external_collaboration (bool): Whether it has an external collaboration or not
        authors (list[StudentProjectAuthor]): The collection of authors of the student project
        title (FormattedLocalizedStringType0 | None): A set of localized strings that support formatting. Invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        language (ClassificationRefType0 | None): A reference to a classification value
        publication_date (CompoundDateType0 | None): A date that can be defined by only year, year and month or a full
            date
        confidential (bool): Indicates if the Student Project is confidential
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
        publishing_institution (None | str | Unset): The Publishing institution of the student thesis
        supervisors (list[StudentProjectSupervisor] | Unset): A collection of supervisors
        publishing_place (None | str | Unset): Place of Publishing
        location (None | str | Unset): The location
        placement (None | str | Unset): The placement
        contact_info (None | str | Unset): The contact info for the student project
        room (None | str | Unset): The room where the exam will take/took place
        time (None | str | Unset): The time when the exam will take/took place
        examiner (None | str | Unset): The examiner of the exam of the student thesis
        documents (list[StudentProjectDocument] | Unset): The student project documents
        appendices (list[StudentProjectAppendixDocument] | Unset): The student project appendix documents
        author_comment (None | str | Unset): Text field to capture any authors who could not be identified as an author
            model
        external_collaborators (list[StudentProjectExternalCollaborator] | Unset): The external collaborators of the
            student project
        campus (ClassificationRefType0 | None | Unset): A reference to a classification value
        organization (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
        notification_recipients (list[StudentProjectNotificationRecipient] | Unset): A number of email addresses that
            will be notified once this student project enters the validated workflow step
        sub_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        student_project_abstract (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support
            formatting. Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        number_of_pages (int | None | Unset): The number of pages in the production. Not used by patents
        links (list[Link] | Unset): A collection of links
        images (list[ImageFile] | Unset): A collection of images
        workflow (Workflow | Unset): Information about workflow
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the student project.
        system_name (str | Unset): The content system name
    """

    has_supervisors: bool
    educations: list[EducationAssociation]
    external_collaboration: bool
    authors: list[StudentProjectAuthor]
    title: FormattedLocalizedStringType0 | None
    language: ClassificationRefType0 | None
    publication_date: CompoundDateType0 | None
    confidential: bool
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
    publishing_institution: None | str | Unset = UNSET
    supervisors: list[StudentProjectSupervisor] | Unset = UNSET
    publishing_place: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    placement: None | str | Unset = UNSET
    contact_info: None | str | Unset = UNSET
    room: None | str | Unset = UNSET
    time: None | str | Unset = UNSET
    examiner: None | str | Unset = UNSET
    documents: list[StudentProjectDocument] | Unset = UNSET
    appendices: list[StudentProjectAppendixDocument] | Unset = UNSET
    author_comment: None | str | Unset = UNSET
    external_collaborators: list[StudentProjectExternalCollaborator] | Unset = UNSET
    campus: ClassificationRefType0 | None | Unset = UNSET
    organization: None | OrganizationRefType0 | Unset = UNSET
    notification_recipients: list[StudentProjectNotificationRecipient] | Unset = UNSET
    sub_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    student_project_abstract: FormattedLocalizedStringType0 | None | Unset = UNSET
    number_of_pages: int | None | Unset = UNSET
    links: list[Link] | Unset = UNSET
    images: list[ImageFile] | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        has_supervisors = self.has_supervisors

        educations = []
        for educations_item_data in self.educations:
            educations_item = educations_item_data.to_dict()
            educations.append(educations_item)

        external_collaboration = self.external_collaboration

        authors = []
        for authors_item_data in self.authors:
            authors_item = authors_item_data.to_dict()
            authors.append(authors_item)

        title: dict[str, Any] | None
        if isinstance(self.title, FormattedLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        language: dict[str, Any] | None
        if isinstance(self.language, ClassificationRefType0):
            language = self.language.to_dict()
        else:
            language = self.language

        publication_date: dict[str, Any] | None
        if isinstance(self.publication_date, CompoundDateType0):
            publication_date = self.publication_date.to_dict()
        else:
            publication_date = self.publication_date

        confidential = self.confidential

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

        publishing_institution: None | str | Unset
        if isinstance(self.publishing_institution, Unset):
            publishing_institution = UNSET
        else:
            publishing_institution = self.publishing_institution

        supervisors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.supervisors, Unset):
            supervisors = []
            for supervisors_item_data in self.supervisors:
                supervisors_item = supervisors_item_data.to_dict()
                supervisors.append(supervisors_item)

        publishing_place: None | str | Unset
        if isinstance(self.publishing_place, Unset):
            publishing_place = UNSET
        else:
            publishing_place = self.publishing_place

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        placement: None | str | Unset
        if isinstance(self.placement, Unset):
            placement = UNSET
        else:
            placement = self.placement

        contact_info: None | str | Unset
        if isinstance(self.contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = self.contact_info

        room: None | str | Unset
        if isinstance(self.room, Unset):
            room = UNSET
        else:
            room = self.room

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        examiner: None | str | Unset
        if isinstance(self.examiner, Unset):
            examiner = UNSET
        else:
            examiner = self.examiner

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        appendices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.appendices, Unset):
            appendices = []
            for appendices_item_data in self.appendices:
                appendices_item = appendices_item_data.to_dict()
                appendices.append(appendices_item)

        author_comment: None | str | Unset
        if isinstance(self.author_comment, Unset):
            author_comment = UNSET
        else:
            author_comment = self.author_comment

        external_collaborators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_collaborators, Unset):
            external_collaborators = []
            for external_collaborators_item_data in self.external_collaborators:
                external_collaborators_item = external_collaborators_item_data.to_dict()
                external_collaborators.append(external_collaborators_item)

        campus: dict[str, Any] | None | Unset
        if isinstance(self.campus, Unset):
            campus = UNSET
        elif isinstance(self.campus, ClassificationRefType0):
            campus = self.campus.to_dict()
        else:
            campus = self.campus

        organization: dict[str, Any] | None | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, OrganizationRefType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        notification_recipients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_recipients, Unset):
            notification_recipients = []
            for notification_recipients_item_data in self.notification_recipients:
                notification_recipients_item = (
                    notification_recipients_item_data.to_dict()
                )
                notification_recipients.append(notification_recipients_item)

        sub_title: dict[str, Any] | None | Unset
        if isinstance(self.sub_title, Unset):
            sub_title = UNSET
        elif isinstance(self.sub_title, FormattedLocalizedStringType0):
            sub_title = self.sub_title.to_dict()
        else:
            sub_title = self.sub_title

        student_project_abstract: dict[str, Any] | None | Unset
        if isinstance(self.student_project_abstract, Unset):
            student_project_abstract = UNSET
        elif isinstance(self.student_project_abstract, FormattedLocalizedStringType0):
            student_project_abstract = self.student_project_abstract.to_dict()
        else:
            student_project_abstract = self.student_project_abstract

        number_of_pages: int | None | Unset
        if isinstance(self.number_of_pages, Unset):
            number_of_pages = UNSET
        else:
            number_of_pages = self.number_of_pages

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasSupervisors": has_supervisors,
                "educations": educations,
                "externalCollaboration": external_collaboration,
                "authors": authors,
                "title": title,
                "language": language,
                "publicationDate": publication_date,
                "confidential": confidential,
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
        if publishing_institution is not UNSET:
            field_dict["publishingInstitution"] = publishing_institution
        if supervisors is not UNSET:
            field_dict["supervisors"] = supervisors
        if publishing_place is not UNSET:
            field_dict["publishingPlace"] = publishing_place
        if location is not UNSET:
            field_dict["location"] = location
        if placement is not UNSET:
            field_dict["placement"] = placement
        if contact_info is not UNSET:
            field_dict["contactInfo"] = contact_info
        if room is not UNSET:
            field_dict["room"] = room
        if time is not UNSET:
            field_dict["time"] = time
        if examiner is not UNSET:
            field_dict["examiner"] = examiner
        if documents is not UNSET:
            field_dict["documents"] = documents
        if appendices is not UNSET:
            field_dict["appendices"] = appendices
        if author_comment is not UNSET:
            field_dict["authorComment"] = author_comment
        if external_collaborators is not UNSET:
            field_dict["externalCollaborators"] = external_collaborators
        if campus is not UNSET:
            field_dict["campus"] = campus
        if organization is not UNSET:
            field_dict["organization"] = organization
        if notification_recipients is not UNSET:
            field_dict["notificationRecipients"] = notification_recipients
        if sub_title is not UNSET:
            field_dict["subTitle"] = sub_title
        if student_project_abstract is not UNSET:
            field_dict["studentProjectAbstract"] = student_project_abstract
        if number_of_pages is not UNSET:
            field_dict["numberOfPages"] = number_of_pages
        if links is not UNSET:
            field_dict["links"] = links
        if images is not UNSET:
            field_dict["images"] = images
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0
        from ..models.education_association import EducationAssociation
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.student_project_appendix_document import (
            StudentProjectAppendixDocument,
        )
        from ..models.student_project_author import StudentProjectAuthor
        from ..models.student_project_document import StudentProjectDocument
        from ..models.student_project_external_collaborator import (
            StudentProjectExternalCollaborator,
        )
        from ..models.student_project_notification_recipient import (
            StudentProjectNotificationRecipient,
        )
        from ..models.student_project_supervisor import StudentProjectSupervisor
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)
        has_supervisors = d.pop("hasSupervisors")

        educations = []
        _educations = d.pop("educations")
        for educations_item_data in _educations:
            educations_item = EducationAssociation.from_dict(educations_item_data)

            educations.append(educations_item)

        external_collaboration = d.pop("externalCollaboration")

        authors = []
        _authors = d.pop("authors")
        for authors_item_data in _authors:
            authors_item = StudentProjectAuthor.from_dict(authors_item_data)

            authors.append(authors_item)

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

        def _parse_publication_date(data: object) -> CompoundDateType0 | None:
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

        publication_date = _parse_publication_date(d.pop("publicationDate"))

        confidential = d.pop("confidential")

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

        def _parse_publishing_institution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publishing_institution = _parse_publishing_institution(
            d.pop("publishingInstitution", UNSET)
        )

        _supervisors = d.pop("supervisors", UNSET)
        supervisors: list[StudentProjectSupervisor] | Unset = UNSET
        if _supervisors is not UNSET:
            supervisors = []
            for supervisors_item_data in _supervisors:
                supervisors_item = StudentProjectSupervisor.from_dict(
                    supervisors_item_data
                )

                supervisors.append(supervisors_item)

        def _parse_publishing_place(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publishing_place = _parse_publishing_place(d.pop("publishingPlace", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_placement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placement = _parse_placement(d.pop("placement", UNSET))

        def _parse_contact_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_info = _parse_contact_info(d.pop("contactInfo", UNSET))

        def _parse_room(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room = _parse_room(d.pop("room", UNSET))

        def _parse_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time = _parse_time(d.pop("time", UNSET))

        def _parse_examiner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        examiner = _parse_examiner(d.pop("examiner", UNSET))

        _documents = d.pop("documents", UNSET)
        documents: list[StudentProjectDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = StudentProjectDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        _appendices = d.pop("appendices", UNSET)
        appendices: list[StudentProjectAppendixDocument] | Unset = UNSET
        if _appendices is not UNSET:
            appendices = []
            for appendices_item_data in _appendices:
                appendices_item = StudentProjectAppendixDocument.from_dict(
                    appendices_item_data
                )

                appendices.append(appendices_item)

        def _parse_author_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_comment = _parse_author_comment(d.pop("authorComment", UNSET))

        _external_collaborators = d.pop("externalCollaborators", UNSET)
        external_collaborators: list[StudentProjectExternalCollaborator] | Unset = UNSET
        if _external_collaborators is not UNSET:
            external_collaborators = []
            for external_collaborators_item_data in _external_collaborators:
                external_collaborators_item = (
                    StudentProjectExternalCollaborator.from_dict(
                        external_collaborators_item_data
                    )
                )

                external_collaborators.append(external_collaborators_item)

        def _parse_campus(data: object) -> ClassificationRefType0 | None | Unset:
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

        campus = _parse_campus(d.pop("campus", UNSET))

        def _parse_organization(data: object) -> None | OrganizationRefType0 | Unset:
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

        organization = _parse_organization(d.pop("organization", UNSET))

        _notification_recipients = d.pop("notificationRecipients", UNSET)
        notification_recipients: list[StudentProjectNotificationRecipient] | Unset = (
            UNSET
        )
        if _notification_recipients is not UNSET:
            notification_recipients = []
            for notification_recipients_item_data in _notification_recipients:
                notification_recipients_item = (
                    StudentProjectNotificationRecipient.from_dict(
                        notification_recipients_item_data
                    )
                )

                notification_recipients.append(notification_recipients_item)

        def _parse_sub_title(
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

        sub_title = _parse_sub_title(d.pop("subTitle", UNSET))

        def _parse_student_project_abstract(
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

        student_project_abstract = _parse_student_project_abstract(
            d.pop("studentProjectAbstract", UNSET)
        )

        def _parse_number_of_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_pages = _parse_number_of_pages(d.pop("numberOfPages", UNSET))

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        _images = d.pop("images", UNSET)
        images: list[ImageFile] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = ImageFile.from_dict(images_item_data)

                images.append(images_item)

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

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

        system_name = d.pop("systemName", UNSET)

        student_project = cls(
            has_supervisors=has_supervisors,
            educations=educations,
            external_collaboration=external_collaboration,
            authors=authors,
            title=title,
            language=language,
            publication_date=publication_date,
            confidential=confidential,
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
            publishing_institution=publishing_institution,
            supervisors=supervisors,
            publishing_place=publishing_place,
            location=location,
            placement=placement,
            contact_info=contact_info,
            room=room,
            time=time,
            examiner=examiner,
            documents=documents,
            appendices=appendices,
            author_comment=author_comment,
            external_collaborators=external_collaborators,
            campus=campus,
            organization=organization,
            notification_recipients=notification_recipients,
            sub_title=sub_title,
            student_project_abstract=student_project_abstract,
            number_of_pages=number_of_pages,
            links=links,
            images=images,
            workflow=workflow,
            keyword_groups=keyword_groups,
            system_name=system_name,
        )

        student_project.additional_properties = d
        return student_project

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
