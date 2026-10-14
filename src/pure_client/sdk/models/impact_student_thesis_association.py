from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.student_thesis_ref_type_0 import StudentThesisRefType0


T = TypeVar("T", bound="ImpactStudentThesisAssociation")


@_attrs_define
class ImpactStudentThesisAssociation:
    """An association to a student thesis

    Attributes:
        student_thesis (None | StudentThesisRefType0): A reference to student thesis
    """

    student_thesis: None | StudentThesisRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0

        student_thesis: dict[str, Any] | None
        if isinstance(self.student_thesis, StudentThesisRefType0):
            student_thesis = self.student_thesis.to_dict()
        else:
            student_thesis = self.student_thesis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "studentThesis": student_thesis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0

        d = dict(src_dict)

        def _parse_student_thesis(data: object) -> None | StudentThesisRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_student_thesis_ref_type_0 = (
                    StudentThesisRefType0.from_dict(data)
                )

                return componentsschemas_student_thesis_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StudentThesisRefType0, data)

        student_thesis = _parse_student_thesis(d.pop("studentThesis"))

        impact_student_thesis_association = cls(
            student_thesis=student_thesis,
        )

        impact_student_thesis_association.additional_properties = d
        return impact_student_thesis_association

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
