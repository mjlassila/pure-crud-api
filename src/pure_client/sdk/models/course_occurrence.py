from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_classified_course_lecturer_association import (
        AbstractClassifiedCourseLecturerAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.identifier import Identifier
    from ..models.organization_ref_type_0 import OrganizationRefType0


T = TypeVar("T", bound="CourseOccurrence")


@_attrs_define
class CourseOccurrence:
    """An occurrence of a given course.

    Attributes:
        semester (ClassificationRefType0 | None): A reference to a classification value
        year (int): What year the course occurred
        course_lecturers (list[AbstractClassifiedCourseLecturerAssociation]): A collection of persons who have lectured
            in the course
        organizations (list[None | OrganizationRefType0]): A collection of organization associations
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        student_learners_count (int | None | Unset): A count of student learners attending the course
        grade (None | str | Unset): The specific grade awarded by the course, such as a 'Master of Science' degree
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations
        identifiers (list[Identifier] | None | Unset): Identifiers related to the course occurrence
    """

    semester: ClassificationRefType0 | None
    year: int
    course_lecturers: list[AbstractClassifiedCourseLecturerAssociation]
    organizations: list[None | OrganizationRefType0]
    pure_id: int | Unset = UNSET
    student_learners_count: int | None | Unset = UNSET
    grade: None | str | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    identifiers: list[Identifier] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        semester: dict[str, Any] | None
        if isinstance(self.semester, ClassificationRefType0):
            semester = self.semester.to_dict()
        else:
            semester = self.semester

        year = self.year

        course_lecturers = []
        for course_lecturers_item_data in self.course_lecturers:
            course_lecturers_item = course_lecturers_item_data.to_dict()
            course_lecturers.append(course_lecturers_item)

        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item: dict[str, Any] | None
            if isinstance(organizations_item_data, OrganizationRefType0):
                organizations_item = organizations_item_data.to_dict()
            else:
                organizations_item = organizations_item_data
            organizations.append(organizations_item)

        pure_id = self.pure_id

        student_learners_count: int | None | Unset
        if isinstance(self.student_learners_count, Unset):
            student_learners_count = UNSET
        else:
            student_learners_count = self.student_learners_count

        grade: None | str | Unset
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "semester": semester,
                "year": year,
                "courseLecturers": course_lecturers,
                "organizations": organizations,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if student_learners_count is not UNSET:
            field_dict["studentLearnersCount"] = student_learners_count
        if grade is not UNSET:
            field_dict["grade"] = grade
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_classified_course_lecturer_association import (
            AbstractClassifiedCourseLecturerAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.identifier import Identifier
        from ..models.organization_ref_type_0 import OrganizationRefType0

        d = dict(src_dict)

        def _parse_semester(data: object) -> ClassificationRefType0 | None:
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

        semester = _parse_semester(d.pop("semester"))

        year = d.pop("year")

        course_lecturers = []
        _course_lecturers = d.pop("courseLecturers")
        for course_lecturers_item_data in _course_lecturers:
            course_lecturers_item = (
                AbstractClassifiedCourseLecturerAssociation.from_dict(
                    course_lecturers_item_data
                )
            )

            course_lecturers.append(course_lecturers_item)

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

        pure_id = d.pop("pureId", UNSET)

        def _parse_student_learners_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        student_learners_count = _parse_student_learners_count(
            d.pop("studentLearnersCount", UNSET)
        )

        def _parse_grade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grade = _parse_grade(d.pop("grade", UNSET))

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

        course_occurrence = cls(
            semester=semester,
            year=year,
            course_lecturers=course_lecturers,
            organizations=organizations,
            pure_id=pure_id,
            student_learners_count=student_learners_count,
            grade=grade,
            external_organizations=external_organizations,
            identifiers=identifiers,
        )

        course_occurrence.additional_properties = d
        return course_occurrence

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
