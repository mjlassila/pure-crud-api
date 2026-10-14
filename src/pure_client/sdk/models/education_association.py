from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.education_ref_type_0 import EducationRefType0
    from ..models.semester_ref_type_0 import SemesterRefType0
    from ..models.specialization_ref_type_0 import SpecializationRefType0


T = TypeVar("T", bound="EducationAssociation")


@_attrs_define
class EducationAssociation:
    """An association to an education

    Attributes:
        education_ref (EducationRefType0 | None): A reference to Education
        semester_ref (None | SemesterRefType0): A reference to semester
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        specialization_ref (None | SpecializationRefType0 | Unset): A reference to a specialization
    """

    education_ref: EducationRefType0 | None
    semester_ref: None | SemesterRefType0
    pure_id: int | Unset = UNSET
    specialization_ref: None | SpecializationRefType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.education_ref_type_0 import EducationRefType0
        from ..models.semester_ref_type_0 import SemesterRefType0
        from ..models.specialization_ref_type_0 import SpecializationRefType0

        education_ref: dict[str, Any] | None
        if isinstance(self.education_ref, EducationRefType0):
            education_ref = self.education_ref.to_dict()
        else:
            education_ref = self.education_ref

        semester_ref: dict[str, Any] | None
        if isinstance(self.semester_ref, SemesterRefType0):
            semester_ref = self.semester_ref.to_dict()
        else:
            semester_ref = self.semester_ref

        pure_id = self.pure_id

        specialization_ref: dict[str, Any] | None | Unset
        if isinstance(self.specialization_ref, Unset):
            specialization_ref = UNSET
        elif isinstance(self.specialization_ref, SpecializationRefType0):
            specialization_ref = self.specialization_ref.to_dict()
        else:
            specialization_ref = self.specialization_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "educationRef": education_ref,
                "semesterRef": semester_ref,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if specialization_ref is not UNSET:
            field_dict["specializationRef"] = specialization_ref

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.education_ref_type_0 import EducationRefType0
        from ..models.semester_ref_type_0 import SemesterRefType0
        from ..models.specialization_ref_type_0 import SpecializationRefType0

        d = dict(src_dict)

        def _parse_education_ref(data: object) -> EducationRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_education_ref_type_0 = EducationRefType0.from_dict(
                    data
                )

                return componentsschemas_education_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EducationRefType0 | None, data)

        education_ref = _parse_education_ref(d.pop("educationRef"))

        def _parse_semester_ref(data: object) -> None | SemesterRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_semester_ref_type_0 = SemesterRefType0.from_dict(data)

                return componentsschemas_semester_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SemesterRefType0, data)

        semester_ref = _parse_semester_ref(d.pop("semesterRef"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_specialization_ref(
            data: object,
        ) -> None | SpecializationRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_specialization_ref_type_0 = (
                    SpecializationRefType0.from_dict(data)
                )

                return componentsschemas_specialization_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpecializationRefType0 | Unset, data)

        specialization_ref = _parse_specialization_ref(
            d.pop("specializationRef", UNSET)
        )

        education_association = cls(
            education_ref=education_ref,
            semester_ref=semester_ref,
            pure_id=pure_id,
            specialization_ref=specialization_ref,
        )

        education_association.additional_properties = d
        return education_association

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
