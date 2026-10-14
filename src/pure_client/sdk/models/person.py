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
    from ..models.academic_qualification import AcademicQualification
    from ..models.address_type_0 import AddressType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.classified_localized_value import ClassifiedLocalizedValue
    from ..models.classified_name import ClassifiedName
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.document import Document
    from ..models.external_appointment import ExternalAppointment
    from ..models.honorary_staff_organization_association import (
        HonoraryStaffOrganizationAssociation,
    )
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.name import Name
    from ..models.person_classified_leave_of_absence import (
        PersonClassifiedLeaveOfAbsence,
    )
    from ..models.person_expertise_ref_type_0 import PersonExpertiseRefType0
    from ..models.professional_qualification import ProfessionalQualification
    from ..models.staff_organization_association import StaffOrganizationAssociation
    from ..models.student_organization_association import StudentOrganizationAssociation
    from ..models.user_ref_type_0 import UserRefType0
    from ..models.visibility import Visibility
    from ..models.visiting_scholar_organization_association import (
        VisitingScholarOrganizationAssociation,
    )
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Person")


@_attrs_define
class Person:
    """An academic professional, student, or other individual attached to the institution.

    Attributes:
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
        person_expertise (None | PersonExpertiseRefType0 | Unset): A reference to a person expertise
        start_date_as_researcher (datetime.date | None | Unset): Date that the person entered into the academic
            profession.
        affiliation_note (None | str | Unset): Notes regarding affiliations of the person.
        date_of_birth (datetime.date | None | Unset): The person's date of birth.
        employee_start_date (datetime.date | None | Unset): Date of the persons first day of the institution.
        employee_end_date (datetime.date | None | Unset): Date of the persons last day of the institution.
        external_positions (list[ExternalAppointment] | None | Unset): positions held by the person, that are external
            to the institution
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of Keyword associated with the person.
        leaves_of_absence (list[PersonClassifiedLeaveOfAbsence] | None | Unset): Leaves of absence had by the person.
        links (list[Link] | None | Unset): Links associated with the person.
        name (Name | Unset): A name describing a person, made up of given- and family name
        names (list[ClassifiedName] | None | Unset): Variant names of the person, Known aliases, ect.
        nationality (ClassificationRefType0 | None | Unset): A reference to a classification value
        orcid (None | str | Unset): orcid of the person.
        orcid_authenticated (bool | Unset): Authentication status of the orcid associated with the person.
        ciencia_id (None | str | Unset): Ciencia ID of the person.
        ciencia_id_authenticated (bool | Unset): Authentication status of the Ciencia ID associated with the person.
        honorary_staff_organization_associations (list[HonoraryStaffOrganizationAssociation] | None | Unset):
            Organizations that the person is associated with under the title of 'Honorary Staff'
        staff_organization_associations (list[StaffOrganizationAssociation] | None | Unset): Organizations that the
            person is associated with as 'Staff'
        student_organization_associations (list[StudentOrganizationAssociation] | None | Unset): Organizations that the
            person is associated with as a 'Student'
        visiting_scholar_organization_associations (list[VisitingScholarOrganizationAssociation] | None | Unset):
            Organizations that the person is associated with as a 'Visiting Scholar
        academic_qualifications (list[AcademicQualification] | None | Unset): Levels of academic qualifications that the
            person has achieved.
        profile_photos (list[ImageFile] | None | Unset): Profile photos in the form of Image files. The maximum file
            size is 1mb
        documents (list[Document] | None | Unset): Associated documents for the person
        private_address (AddressType0 | None | Unset): A physical address
        professional_qualifications (list[ProfessionalQualification] | None | Unset): The professional qualifications
            held by the person
        selected_for_profile_refinement_service (bool | Unset): If the person has been profiled.
        profile_information (list[ClassifiedFormattedLocalizedValue] | None | Unset): Information objects making up
            profiles made of the person
        retirement_date (datetime.date | None | Unset): Date of retirement for the person
        gender (ClassificationRefType0 | None | Unset): A reference to a classification value
        titles (list[ClassifiedLocalizedValue] | None | Unset): Titles held by the person
        visibility (Visibility | Unset): Visibility of an object
        willing_to_take_phd_students (bool | Unset): Boolean to define if the Person is willing to take on Phd Students.
        willing_to_take_phd_students_description (None | str | Unset): Field to describe or list phd projects that the
            person will participate in.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the person
        user (None | Unset | UserRefType0): A reference to an user
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        workflow (Workflow | Unset): Information about workflow
        main_research_area (ClassificationRefType0 | None | Unset): A reference to a classification value
        profiled (bool | Unset):
        system_name (str | Unset): The content system name
    """

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
    person_expertise: None | PersonExpertiseRefType0 | Unset = UNSET
    start_date_as_researcher: datetime.date | None | Unset = UNSET
    affiliation_note: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    employee_start_date: datetime.date | None | Unset = UNSET
    employee_end_date: datetime.date | None | Unset = UNSET
    external_positions: list[ExternalAppointment] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    leaves_of_absence: list[PersonClassifiedLeaveOfAbsence] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    name: Name | Unset = UNSET
    names: list[ClassifiedName] | None | Unset = UNSET
    nationality: ClassificationRefType0 | None | Unset = UNSET
    orcid: None | str | Unset = UNSET
    orcid_authenticated: bool | Unset = UNSET
    ciencia_id: None | str | Unset = UNSET
    ciencia_id_authenticated: bool | Unset = UNSET
    honorary_staff_organization_associations: (
        list[HonoraryStaffOrganizationAssociation] | None | Unset
    ) = UNSET
    staff_organization_associations: (
        list[StaffOrganizationAssociation] | None | Unset
    ) = UNSET
    student_organization_associations: (
        list[StudentOrganizationAssociation] | None | Unset
    ) = UNSET
    visiting_scholar_organization_associations: (
        list[VisitingScholarOrganizationAssociation] | None | Unset
    ) = UNSET
    academic_qualifications: list[AcademicQualification] | None | Unset = UNSET
    profile_photos: list[ImageFile] | None | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    private_address: AddressType0 | None | Unset = UNSET
    professional_qualifications: list[ProfessionalQualification] | None | Unset = UNSET
    selected_for_profile_refinement_service: bool | Unset = UNSET
    profile_information: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    retirement_date: datetime.date | None | Unset = UNSET
    gender: ClassificationRefType0 | None | Unset = UNSET
    titles: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    willing_to_take_phd_students: bool | Unset = UNSET
    willing_to_take_phd_students_description: None | str | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    user: None | Unset | UserRefType0 = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    main_research_area: ClassificationRefType0 | None | Unset = UNSET
    profiled: bool | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address_type_0 import AddressType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.person_expertise_ref_type_0 import PersonExpertiseRefType0
        from ..models.user_ref_type_0 import UserRefType0

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

        person_expertise: dict[str, Any] | None | Unset
        if isinstance(self.person_expertise, Unset):
            person_expertise = UNSET
        elif isinstance(self.person_expertise, PersonExpertiseRefType0):
            person_expertise = self.person_expertise.to_dict()
        else:
            person_expertise = self.person_expertise

        start_date_as_researcher: None | str | Unset
        if isinstance(self.start_date_as_researcher, Unset):
            start_date_as_researcher = UNSET
        elif isinstance(self.start_date_as_researcher, datetime.date):
            start_date_as_researcher = self.start_date_as_researcher.isoformat()
        else:
            start_date_as_researcher = self.start_date_as_researcher

        affiliation_note: None | str | Unset
        if isinstance(self.affiliation_note, Unset):
            affiliation_note = UNSET
        else:
            affiliation_note = self.affiliation_note

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        employee_start_date: None | str | Unset
        if isinstance(self.employee_start_date, Unset):
            employee_start_date = UNSET
        elif isinstance(self.employee_start_date, datetime.date):
            employee_start_date = self.employee_start_date.isoformat()
        else:
            employee_start_date = self.employee_start_date

        employee_end_date: None | str | Unset
        if isinstance(self.employee_end_date, Unset):
            employee_end_date = UNSET
        elif isinstance(self.employee_end_date, datetime.date):
            employee_end_date = self.employee_end_date.isoformat()
        else:
            employee_end_date = self.employee_end_date

        external_positions: list[dict[str, Any]] | None | Unset
        if isinstance(self.external_positions, Unset):
            external_positions = UNSET
        elif isinstance(self.external_positions, list):
            external_positions = []
            for external_positions_type_0_item_data in self.external_positions:
                external_positions_type_0_item = (
                    external_positions_type_0_item_data.to_dict()
                )
                external_positions.append(external_positions_type_0_item)

        else:
            external_positions = self.external_positions

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

        leaves_of_absence: list[dict[str, Any]] | None | Unset
        if isinstance(self.leaves_of_absence, Unset):
            leaves_of_absence = UNSET
        elif isinstance(self.leaves_of_absence, list):
            leaves_of_absence = []
            for leaves_of_absence_type_0_item_data in self.leaves_of_absence:
                leaves_of_absence_type_0_item = (
                    leaves_of_absence_type_0_item_data.to_dict()
                )
                leaves_of_absence.append(leaves_of_absence_type_0_item)

        else:
            leaves_of_absence = self.leaves_of_absence

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

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        names: list[dict[str, Any]] | None | Unset
        if isinstance(self.names, Unset):
            names = UNSET
        elif isinstance(self.names, list):
            names = []
            for names_type_0_item_data in self.names:
                names_type_0_item = names_type_0_item_data.to_dict()
                names.append(names_type_0_item)

        else:
            names = self.names

        nationality: dict[str, Any] | None | Unset
        if isinstance(self.nationality, Unset):
            nationality = UNSET
        elif isinstance(self.nationality, ClassificationRefType0):
            nationality = self.nationality.to_dict()
        else:
            nationality = self.nationality

        orcid: None | str | Unset
        if isinstance(self.orcid, Unset):
            orcid = UNSET
        else:
            orcid = self.orcid

        orcid_authenticated = self.orcid_authenticated

        ciencia_id: None | str | Unset
        if isinstance(self.ciencia_id, Unset):
            ciencia_id = UNSET
        else:
            ciencia_id = self.ciencia_id

        ciencia_id_authenticated = self.ciencia_id_authenticated

        honorary_staff_organization_associations: list[dict[str, Any]] | None | Unset
        if isinstance(self.honorary_staff_organization_associations, Unset):
            honorary_staff_organization_associations = UNSET
        elif isinstance(self.honorary_staff_organization_associations, list):
            honorary_staff_organization_associations = []
            for (
                honorary_staff_organization_associations_type_0_item_data
            ) in self.honorary_staff_organization_associations:
                honorary_staff_organization_associations_type_0_item = (
                    honorary_staff_organization_associations_type_0_item_data.to_dict()
                )
                honorary_staff_organization_associations.append(
                    honorary_staff_organization_associations_type_0_item
                )

        else:
            honorary_staff_organization_associations = (
                self.honorary_staff_organization_associations
            )

        staff_organization_associations: list[dict[str, Any]] | None | Unset
        if isinstance(self.staff_organization_associations, Unset):
            staff_organization_associations = UNSET
        elif isinstance(self.staff_organization_associations, list):
            staff_organization_associations = []
            for (
                staff_organization_associations_type_0_item_data
            ) in self.staff_organization_associations:
                staff_organization_associations_type_0_item = (
                    staff_organization_associations_type_0_item_data.to_dict()
                )
                staff_organization_associations.append(
                    staff_organization_associations_type_0_item
                )

        else:
            staff_organization_associations = self.staff_organization_associations

        student_organization_associations: list[dict[str, Any]] | None | Unset
        if isinstance(self.student_organization_associations, Unset):
            student_organization_associations = UNSET
        elif isinstance(self.student_organization_associations, list):
            student_organization_associations = []
            for (
                student_organization_associations_type_0_item_data
            ) in self.student_organization_associations:
                student_organization_associations_type_0_item = (
                    student_organization_associations_type_0_item_data.to_dict()
                )
                student_organization_associations.append(
                    student_organization_associations_type_0_item
                )

        else:
            student_organization_associations = self.student_organization_associations

        visiting_scholar_organization_associations: list[dict[str, Any]] | None | Unset
        if isinstance(self.visiting_scholar_organization_associations, Unset):
            visiting_scholar_organization_associations = UNSET
        elif isinstance(self.visiting_scholar_organization_associations, list):
            visiting_scholar_organization_associations = []
            for (
                visiting_scholar_organization_associations_type_0_item_data
            ) in self.visiting_scholar_organization_associations:
                visiting_scholar_organization_associations_type_0_item = visiting_scholar_organization_associations_type_0_item_data.to_dict()
                visiting_scholar_organization_associations.append(
                    visiting_scholar_organization_associations_type_0_item
                )

        else:
            visiting_scholar_organization_associations = (
                self.visiting_scholar_organization_associations
            )

        academic_qualifications: list[dict[str, Any]] | None | Unset
        if isinstance(self.academic_qualifications, Unset):
            academic_qualifications = UNSET
        elif isinstance(self.academic_qualifications, list):
            academic_qualifications = []
            for (
                academic_qualifications_type_0_item_data
            ) in self.academic_qualifications:
                academic_qualifications_type_0_item = (
                    academic_qualifications_type_0_item_data.to_dict()
                )
                academic_qualifications.append(academic_qualifications_type_0_item)

        else:
            academic_qualifications = self.academic_qualifications

        profile_photos: list[dict[str, Any]] | None | Unset
        if isinstance(self.profile_photos, Unset):
            profile_photos = UNSET
        elif isinstance(self.profile_photos, list):
            profile_photos = []
            for profile_photos_type_0_item_data in self.profile_photos:
                profile_photos_type_0_item = profile_photos_type_0_item_data.to_dict()
                profile_photos.append(profile_photos_type_0_item)

        else:
            profile_photos = self.profile_photos

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

        private_address: dict[str, Any] | None | Unset
        if isinstance(self.private_address, Unset):
            private_address = UNSET
        elif isinstance(self.private_address, AddressType0):
            private_address = self.private_address.to_dict()
        else:
            private_address = self.private_address

        professional_qualifications: list[dict[str, Any]] | None | Unset
        if isinstance(self.professional_qualifications, Unset):
            professional_qualifications = UNSET
        elif isinstance(self.professional_qualifications, list):
            professional_qualifications = []
            for (
                professional_qualifications_type_0_item_data
            ) in self.professional_qualifications:
                professional_qualifications_type_0_item = (
                    professional_qualifications_type_0_item_data.to_dict()
                )
                professional_qualifications.append(
                    professional_qualifications_type_0_item
                )

        else:
            professional_qualifications = self.professional_qualifications

        selected_for_profile_refinement_service = (
            self.selected_for_profile_refinement_service
        )

        profile_information: list[dict[str, Any]] | None | Unset
        if isinstance(self.profile_information, Unset):
            profile_information = UNSET
        elif isinstance(self.profile_information, list):
            profile_information = []
            for profile_information_type_0_item_data in self.profile_information:
                profile_information_type_0_item = (
                    profile_information_type_0_item_data.to_dict()
                )
                profile_information.append(profile_information_type_0_item)

        else:
            profile_information = self.profile_information

        retirement_date: None | str | Unset
        if isinstance(self.retirement_date, Unset):
            retirement_date = UNSET
        elif isinstance(self.retirement_date, datetime.date):
            retirement_date = self.retirement_date.isoformat()
        else:
            retirement_date = self.retirement_date

        gender: dict[str, Any] | None | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        elif isinstance(self.gender, ClassificationRefType0):
            gender = self.gender.to_dict()
        else:
            gender = self.gender

        titles: list[dict[str, Any]] | None | Unset
        if isinstance(self.titles, Unset):
            titles = UNSET
        elif isinstance(self.titles, list):
            titles = []
            for titles_type_0_item_data in self.titles:
                titles_type_0_item = titles_type_0_item_data.to_dict()
                titles.append(titles_type_0_item)

        else:
            titles = self.titles

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        willing_to_take_phd_students = self.willing_to_take_phd_students

        willing_to_take_phd_students_description: None | str | Unset
        if isinstance(self.willing_to_take_phd_students_description, Unset):
            willing_to_take_phd_students_description = UNSET
        else:
            willing_to_take_phd_students_description = (
                self.willing_to_take_phd_students_description
            )

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

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UserRefType0):
            user = self.user.to_dict()
        else:
            user = self.user

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

        main_research_area: dict[str, Any] | None | Unset
        if isinstance(self.main_research_area, Unset):
            main_research_area = UNSET
        elif isinstance(self.main_research_area, ClassificationRefType0):
            main_research_area = self.main_research_area.to_dict()
        else:
            main_research_area = self.main_research_area

        profiled = self.profiled

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if person_expertise is not UNSET:
            field_dict["personExpertise"] = person_expertise
        if start_date_as_researcher is not UNSET:
            field_dict["startDateAsResearcher"] = start_date_as_researcher
        if affiliation_note is not UNSET:
            field_dict["affiliationNote"] = affiliation_note
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if employee_start_date is not UNSET:
            field_dict["employeeStartDate"] = employee_start_date
        if employee_end_date is not UNSET:
            field_dict["employeeEndDate"] = employee_end_date
        if external_positions is not UNSET:
            field_dict["externalPositions"] = external_positions
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if leaves_of_absence is not UNSET:
            field_dict["leavesOfAbsence"] = leaves_of_absence
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if names is not UNSET:
            field_dict["names"] = names
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if orcid is not UNSET:
            field_dict["orcid"] = orcid
        if orcid_authenticated is not UNSET:
            field_dict["orcidAuthenticated"] = orcid_authenticated
        if ciencia_id is not UNSET:
            field_dict["cienciaId"] = ciencia_id
        if ciencia_id_authenticated is not UNSET:
            field_dict["cienciaIdAuthenticated"] = ciencia_id_authenticated
        if honorary_staff_organization_associations is not UNSET:
            field_dict["honoraryStaffOrganizationAssociations"] = (
                honorary_staff_organization_associations
            )
        if staff_organization_associations is not UNSET:
            field_dict["staffOrganizationAssociations"] = (
                staff_organization_associations
            )
        if student_organization_associations is not UNSET:
            field_dict["studentOrganizationAssociations"] = (
                student_organization_associations
            )
        if visiting_scholar_organization_associations is not UNSET:
            field_dict["visitingScholarOrganizationAssociations"] = (
                visiting_scholar_organization_associations
            )
        if academic_qualifications is not UNSET:
            field_dict["academicQualifications"] = academic_qualifications
        if profile_photos is not UNSET:
            field_dict["profilePhotos"] = profile_photos
        if documents is not UNSET:
            field_dict["documents"] = documents
        if private_address is not UNSET:
            field_dict["privateAddress"] = private_address
        if professional_qualifications is not UNSET:
            field_dict["professionalQualifications"] = professional_qualifications
        if selected_for_profile_refinement_service is not UNSET:
            field_dict["selectedForProfileRefinementService"] = (
                selected_for_profile_refinement_service
            )
        if profile_information is not UNSET:
            field_dict["profileInformation"] = profile_information
        if retirement_date is not UNSET:
            field_dict["retirementDate"] = retirement_date
        if gender is not UNSET:
            field_dict["gender"] = gender
        if titles is not UNSET:
            field_dict["titles"] = titles
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if willing_to_take_phd_students is not UNSET:
            field_dict["willingToTakePhdStudents"] = willing_to_take_phd_students
        if willing_to_take_phd_students_description is not UNSET:
            field_dict["willingToTakePhdStudentsDescription"] = (
                willing_to_take_phd_students_description
            )
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if user is not UNSET:
            field_dict["user"] = user
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if main_research_area is not UNSET:
            field_dict["mainResearchArea"] = main_research_area
        if profiled is not UNSET:
            field_dict["profiled"] = profiled
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.academic_qualification import AcademicQualification
        from ..models.address_type_0 import AddressType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.classified_localized_value import ClassifiedLocalizedValue
        from ..models.classified_name import ClassifiedName
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.document import Document
        from ..models.external_appointment import ExternalAppointment
        from ..models.honorary_staff_organization_association import (
            HonoraryStaffOrganizationAssociation,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.name import Name
        from ..models.person_classified_leave_of_absence import (
            PersonClassifiedLeaveOfAbsence,
        )
        from ..models.person_expertise_ref_type_0 import PersonExpertiseRefType0
        from ..models.professional_qualification import ProfessionalQualification
        from ..models.staff_organization_association import StaffOrganizationAssociation
        from ..models.student_organization_association import (
            StudentOrganizationAssociation,
        )
        from ..models.user_ref_type_0 import UserRefType0
        from ..models.visibility import Visibility
        from ..models.visiting_scholar_organization_association import (
            VisitingScholarOrganizationAssociation,
        )
        from ..models.workflow import Workflow

        d = dict(src_dict)
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

        def _parse_person_expertise(
            data: object,
        ) -> None | PersonExpertiseRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_expertise_ref_type_0 = (
                    PersonExpertiseRefType0.from_dict(data)
                )

                return componentsschemas_person_expertise_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonExpertiseRefType0 | Unset, data)

        person_expertise = _parse_person_expertise(d.pop("personExpertise", UNSET))

        def _parse_start_date_as_researcher(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_as_researcher_type_0 = isoparse(data).date()

                return start_date_as_researcher_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date_as_researcher = _parse_start_date_as_researcher(
            d.pop("startDateAsResearcher", UNSET)
        )

        def _parse_affiliation_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        affiliation_note = _parse_affiliation_note(d.pop("affiliationNote", UNSET))

        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = isoparse(data).date()

                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("dateOfBirth", UNSET))

        def _parse_employee_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                employee_start_date_type_0 = isoparse(data).date()

                return employee_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        employee_start_date = _parse_employee_start_date(
            d.pop("employeeStartDate", UNSET)
        )

        def _parse_employee_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                employee_end_date_type_0 = isoparse(data).date()

                return employee_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        employee_end_date = _parse_employee_end_date(d.pop("employeeEndDate", UNSET))

        def _parse_external_positions(
            data: object,
        ) -> list[ExternalAppointment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_positions_type_0 = []
                _external_positions_type_0 = data
                for external_positions_type_0_item_data in _external_positions_type_0:
                    external_positions_type_0_item = ExternalAppointment.from_dict(
                        external_positions_type_0_item_data
                    )

                    external_positions_type_0.append(external_positions_type_0_item)

                return external_positions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalAppointment] | None | Unset, data)

        external_positions = _parse_external_positions(
            d.pop("externalPositions", UNSET)
        )

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

        def _parse_leaves_of_absence(
            data: object,
        ) -> list[PersonClassifiedLeaveOfAbsence] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                leaves_of_absence_type_0 = []
                _leaves_of_absence_type_0 = data
                for leaves_of_absence_type_0_item_data in _leaves_of_absence_type_0:
                    leaves_of_absence_type_0_item = (
                        PersonClassifiedLeaveOfAbsence.from_dict(
                            leaves_of_absence_type_0_item_data
                        )
                    )

                    leaves_of_absence_type_0.append(leaves_of_absence_type_0_item)

                return leaves_of_absence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PersonClassifiedLeaveOfAbsence] | None | Unset, data)

        leaves_of_absence = _parse_leaves_of_absence(d.pop("leavesOfAbsence", UNSET))

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

        _name = d.pop("name", UNSET)
        name: Name | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = Name.from_dict(_name)

        def _parse_names(data: object) -> list[ClassifiedName] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                names_type_0 = []
                _names_type_0 = data
                for names_type_0_item_data in _names_type_0:
                    names_type_0_item = ClassifiedName.from_dict(names_type_0_item_data)

                    names_type_0.append(names_type_0_item)

                return names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedName] | None | Unset, data)

        names = _parse_names(d.pop("names", UNSET))

        def _parse_nationality(data: object) -> ClassificationRefType0 | None | Unset:
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

        nationality = _parse_nationality(d.pop("nationality", UNSET))

        def _parse_orcid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        orcid = _parse_orcid(d.pop("orcid", UNSET))

        orcid_authenticated = d.pop("orcidAuthenticated", UNSET)

        def _parse_ciencia_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ciencia_id = _parse_ciencia_id(d.pop("cienciaId", UNSET))

        ciencia_id_authenticated = d.pop("cienciaIdAuthenticated", UNSET)

        def _parse_honorary_staff_organization_associations(
            data: object,
        ) -> list[HonoraryStaffOrganizationAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                honorary_staff_organization_associations_type_0 = []
                _honorary_staff_organization_associations_type_0 = data
                for (
                    honorary_staff_organization_associations_type_0_item_data
                ) in _honorary_staff_organization_associations_type_0:
                    honorary_staff_organization_associations_type_0_item = (
                        HonoraryStaffOrganizationAssociation.from_dict(
                            honorary_staff_organization_associations_type_0_item_data
                        )
                    )

                    honorary_staff_organization_associations_type_0.append(
                        honorary_staff_organization_associations_type_0_item
                    )

                return honorary_staff_organization_associations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HonoraryStaffOrganizationAssociation] | None | Unset, data)

        honorary_staff_organization_associations = (
            _parse_honorary_staff_organization_associations(
                d.pop("honoraryStaffOrganizationAssociations", UNSET)
            )
        )

        def _parse_staff_organization_associations(
            data: object,
        ) -> list[StaffOrganizationAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                staff_organization_associations_type_0 = []
                _staff_organization_associations_type_0 = data
                for (
                    staff_organization_associations_type_0_item_data
                ) in _staff_organization_associations_type_0:
                    staff_organization_associations_type_0_item = (
                        StaffOrganizationAssociation.from_dict(
                            staff_organization_associations_type_0_item_data
                        )
                    )

                    staff_organization_associations_type_0.append(
                        staff_organization_associations_type_0_item
                    )

                return staff_organization_associations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StaffOrganizationAssociation] | None | Unset, data)

        staff_organization_associations = _parse_staff_organization_associations(
            d.pop("staffOrganizationAssociations", UNSET)
        )

        def _parse_student_organization_associations(
            data: object,
        ) -> list[StudentOrganizationAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                student_organization_associations_type_0 = []
                _student_organization_associations_type_0 = data
                for (
                    student_organization_associations_type_0_item_data
                ) in _student_organization_associations_type_0:
                    student_organization_associations_type_0_item = (
                        StudentOrganizationAssociation.from_dict(
                            student_organization_associations_type_0_item_data
                        )
                    )

                    student_organization_associations_type_0.append(
                        student_organization_associations_type_0_item
                    )

                return student_organization_associations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StudentOrganizationAssociation] | None | Unset, data)

        student_organization_associations = _parse_student_organization_associations(
            d.pop("studentOrganizationAssociations", UNSET)
        )

        def _parse_visiting_scholar_organization_associations(
            data: object,
        ) -> list[VisitingScholarOrganizationAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                visiting_scholar_organization_associations_type_0 = []
                _visiting_scholar_organization_associations_type_0 = data
                for (
                    visiting_scholar_organization_associations_type_0_item_data
                ) in _visiting_scholar_organization_associations_type_0:
                    visiting_scholar_organization_associations_type_0_item = (
                        VisitingScholarOrganizationAssociation.from_dict(
                            visiting_scholar_organization_associations_type_0_item_data
                        )
                    )

                    visiting_scholar_organization_associations_type_0.append(
                        visiting_scholar_organization_associations_type_0_item
                    )

                return visiting_scholar_organization_associations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[VisitingScholarOrganizationAssociation] | None | Unset, data
            )

        visiting_scholar_organization_associations = (
            _parse_visiting_scholar_organization_associations(
                d.pop("visitingScholarOrganizationAssociations", UNSET)
            )
        )

        def _parse_academic_qualifications(
            data: object,
        ) -> list[AcademicQualification] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                academic_qualifications_type_0 = []
                _academic_qualifications_type_0 = data
                for (
                    academic_qualifications_type_0_item_data
                ) in _academic_qualifications_type_0:
                    academic_qualifications_type_0_item = (
                        AcademicQualification.from_dict(
                            academic_qualifications_type_0_item_data
                        )
                    )

                    academic_qualifications_type_0.append(
                        academic_qualifications_type_0_item
                    )

                return academic_qualifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AcademicQualification] | None | Unset, data)

        academic_qualifications = _parse_academic_qualifications(
            d.pop("academicQualifications", UNSET)
        )

        def _parse_profile_photos(data: object) -> list[ImageFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                profile_photos_type_0 = []
                _profile_photos_type_0 = data
                for profile_photos_type_0_item_data in _profile_photos_type_0:
                    profile_photos_type_0_item = ImageFile.from_dict(
                        profile_photos_type_0_item_data
                    )

                    profile_photos_type_0.append(profile_photos_type_0_item)

                return profile_photos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageFile] | None | Unset, data)

        profile_photos = _parse_profile_photos(d.pop("profilePhotos", UNSET))

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

        def _parse_private_address(data: object) -> AddressType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_address_type_0 = AddressType0.from_dict(data)

                return componentsschemas_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddressType0 | None | Unset, data)

        private_address = _parse_private_address(d.pop("privateAddress", UNSET))

        def _parse_professional_qualifications(
            data: object,
        ) -> list[ProfessionalQualification] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                professional_qualifications_type_0 = []
                _professional_qualifications_type_0 = data
                for (
                    professional_qualifications_type_0_item_data
                ) in _professional_qualifications_type_0:
                    professional_qualifications_type_0_item = (
                        ProfessionalQualification.from_dict(
                            professional_qualifications_type_0_item_data
                        )
                    )

                    professional_qualifications_type_0.append(
                        professional_qualifications_type_0_item
                    )

                return professional_qualifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProfessionalQualification] | None | Unset, data)

        professional_qualifications = _parse_professional_qualifications(
            d.pop("professionalQualifications", UNSET)
        )

        selected_for_profile_refinement_service = d.pop(
            "selectedForProfileRefinementService", UNSET
        )

        def _parse_profile_information(
            data: object,
        ) -> list[ClassifiedFormattedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                profile_information_type_0 = []
                _profile_information_type_0 = data
                for profile_information_type_0_item_data in _profile_information_type_0:
                    profile_information_type_0_item = (
                        ClassifiedFormattedLocalizedValue.from_dict(
                            profile_information_type_0_item_data
                        )
                    )

                    profile_information_type_0.append(profile_information_type_0_item)

                return profile_information_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedFormattedLocalizedValue] | None | Unset, data)

        profile_information = _parse_profile_information(
            d.pop("profileInformation", UNSET)
        )

        def _parse_retirement_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirement_date_type_0 = isoparse(data).date()

                return retirement_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        retirement_date = _parse_retirement_date(d.pop("retirementDate", UNSET))

        def _parse_gender(data: object) -> ClassificationRefType0 | None | Unset:
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

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_titles(
            data: object,
        ) -> list[ClassifiedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                titles_type_0 = []
                _titles_type_0 = data
                for titles_type_0_item_data in _titles_type_0:
                    titles_type_0_item = ClassifiedLocalizedValue.from_dict(
                        titles_type_0_item_data
                    )

                    titles_type_0.append(titles_type_0_item)

                return titles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedLocalizedValue] | None | Unset, data)

        titles = _parse_titles(d.pop("titles", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        willing_to_take_phd_students = d.pop("willingToTakePhdStudents", UNSET)

        def _parse_willing_to_take_phd_students_description(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        willing_to_take_phd_students_description = (
            _parse_willing_to_take_phd_students_description(
                d.pop("willingToTakePhdStudentsDescription", UNSET)
            )
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

        def _parse_user(data: object) -> None | Unset | UserRefType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                return componentsschemas_user_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRefType0, data)

        user = _parse_user(d.pop("user", UNSET))

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

        def _parse_main_research_area(
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

        main_research_area = _parse_main_research_area(d.pop("mainResearchArea", UNSET))

        profiled = d.pop("profiled", UNSET)

        system_name = d.pop("systemName", UNSET)

        person = cls(
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
            person_expertise=person_expertise,
            start_date_as_researcher=start_date_as_researcher,
            affiliation_note=affiliation_note,
            date_of_birth=date_of_birth,
            employee_start_date=employee_start_date,
            employee_end_date=employee_end_date,
            external_positions=external_positions,
            keyword_groups=keyword_groups,
            leaves_of_absence=leaves_of_absence,
            links=links,
            name=name,
            names=names,
            nationality=nationality,
            orcid=orcid,
            orcid_authenticated=orcid_authenticated,
            ciencia_id=ciencia_id,
            ciencia_id_authenticated=ciencia_id_authenticated,
            honorary_staff_organization_associations=honorary_staff_organization_associations,
            staff_organization_associations=staff_organization_associations,
            student_organization_associations=student_organization_associations,
            visiting_scholar_organization_associations=visiting_scholar_organization_associations,
            academic_qualifications=academic_qualifications,
            profile_photos=profile_photos,
            documents=documents,
            private_address=private_address,
            professional_qualifications=professional_qualifications,
            selected_for_profile_refinement_service=selected_for_profile_refinement_service,
            profile_information=profile_information,
            retirement_date=retirement_date,
            gender=gender,
            titles=titles,
            visibility=visibility,
            willing_to_take_phd_students=willing_to_take_phd_students,
            willing_to_take_phd_students_description=willing_to_take_phd_students_description,
            identifiers=identifiers,
            user=user,
            custom_defined_fields=custom_defined_fields,
            workflow=workflow,
            main_research_area=main_research_area,
            profiled=profiled,
            system_name=system_name,
        )

        person.additional_properties = d
        return person

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
