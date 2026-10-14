from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name import Name


T = TypeVar("T", bound="StudentProjectAuthor")


@_attrs_define
class StudentProjectAuthor:
    """The collection of authors of the student project

    Attributes:
        name (Name): A name describing a person, made up of given- and family name
        email (str): The email of the author
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        student_id (None | str | Unset): The student id of the author
    """

    name: Name
    email: str
    pure_id: int | Unset = UNSET
    student_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.to_dict()

        email = self.email

        pure_id = self.pure_id

        student_id: None | str | Unset
        if isinstance(self.student_id, Unset):
            student_id = UNSET
        else:
            student_id = self.student_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if student_id is not UNSET:
            field_dict["studentID"] = student_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.name import Name

        d = dict(src_dict)
        name = Name.from_dict(d.pop("name"))

        email = d.pop("email")

        pure_id = d.pop("pureId", UNSET)

        def _parse_student_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_id = _parse_student_id(d.pop("studentID", UNSET))

        student_project_author = cls(
            name=name,
            email=email,
            pure_id=pure_id,
            student_id=student_id,
        )

        student_project_author.additional_properties = d
        return student_project_author

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
