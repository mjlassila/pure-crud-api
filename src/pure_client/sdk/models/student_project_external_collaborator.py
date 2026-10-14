from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.name import Name


T = TypeVar("T", bound="StudentProjectExternalCollaborator")


@_attrs_define
class StudentProjectExternalCollaborator:
    """An external collaborator of a student project

    Attributes:
        external_organization (ExternalOrganizationRefType0 | None): A reference to an organization external to the
            institution
        external_collaborator_role (ClassificationRefType0 | None): A reference to a classification value
        name (Name): A name describing a person, made up of given- and family name
        email (str): The email of the external collaborator
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        title (None | str | Unset): The title of the external collaborator
    """

    external_organization: ExternalOrganizationRefType0 | None
    external_collaborator_role: ClassificationRefType0 | None
    name: Name
    email: str
    pure_id: int | Unset = UNSET
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )

        external_organization: dict[str, Any] | None
        if isinstance(self.external_organization, ExternalOrganizationRefType0):
            external_organization = self.external_organization.to_dict()
        else:
            external_organization = self.external_organization

        external_collaborator_role: dict[str, Any] | None
        if isinstance(self.external_collaborator_role, ClassificationRefType0):
            external_collaborator_role = self.external_collaborator_role.to_dict()
        else:
            external_collaborator_role = self.external_collaborator_role

        name = self.name.to_dict()

        email = self.email

        pure_id = self.pure_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalOrganization": external_organization,
                "externalCollaboratorRole": external_collaborator_role,
                "name": name,
                "email": email,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.name import Name

        d = dict(src_dict)

        def _parse_external_organization(
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

        external_organization = _parse_external_organization(
            d.pop("externalOrganization")
        )

        def _parse_external_collaborator_role(
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

        external_collaborator_role = _parse_external_collaborator_role(
            d.pop("externalCollaboratorRole")
        )

        name = Name.from_dict(d.pop("name"))

        email = d.pop("email")

        pure_id = d.pop("pureId", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        student_project_external_collaborator = cls(
            external_organization=external_organization,
            external_collaborator_role=external_collaborator_role,
            name=name,
            email=email,
            pure_id=pure_id,
            title=title,
        )

        student_project_external_collaborator.additional_properties = d
        return student_project_external_collaborator

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
