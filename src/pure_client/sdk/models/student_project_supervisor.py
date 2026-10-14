from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.external_person_ref_type_0 import ExternalPersonRefType0
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="StudentProjectSupervisor")


@_attrs_define
class StudentProjectSupervisor:
    """A supervisor for a student project

    Attributes:
        person (None | PersonRefType0): A reference to a person internal to the institution
        external_person (ExternalPersonRefType0 | None): A reference to a person external to the institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        supervisor_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        email (None | str | Unset): The supervisor email
    """

    person: None | PersonRefType0
    external_person: ExternalPersonRefType0 | None
    pure_id: int | Unset = UNSET
    supervisor_type: ClassificationRefType0 | None | Unset = UNSET
    email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        person: dict[str, Any] | None
        if isinstance(self.person, PersonRefType0):
            person = self.person.to_dict()
        else:
            person = self.person

        external_person: dict[str, Any] | None
        if isinstance(self.external_person, ExternalPersonRefType0):
            external_person = self.external_person.to_dict()
        else:
            external_person = self.external_person

        pure_id = self.pure_id

        supervisor_type: dict[str, Any] | None | Unset
        if isinstance(self.supervisor_type, Unset):
            supervisor_type = UNSET
        elif isinstance(self.supervisor_type, ClassificationRefType0):
            supervisor_type = self.supervisor_type.to_dict()
        else:
            supervisor_type = self.supervisor_type

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "person": person,
                "externalPerson": external_person,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if supervisor_type is not UNSET:
            field_dict["supervisorType"] = supervisor_type
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)

        def _parse_person(data: object) -> None | PersonRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_ref_type_0 = PersonRefType0.from_dict(data)

                return componentsschemas_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonRefType0, data)

        person = _parse_person(d.pop("person"))

        def _parse_external_person(data: object) -> ExternalPersonRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_external_person_ref_type_0 = (
                    ExternalPersonRefType0.from_dict(data)
                )

                return componentsschemas_external_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalPersonRefType0 | None, data)

        external_person = _parse_external_person(d.pop("externalPerson"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_supervisor_type(
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

        supervisor_type = _parse_supervisor_type(d.pop("supervisorType", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        student_project_supervisor = cls(
            person=person,
            external_person=external_person,
            pure_id=pure_id,
            supervisor_type=supervisor_type,
            email=email,
        )

        student_project_supervisor.additional_properties = d
        return student_project_supervisor

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
