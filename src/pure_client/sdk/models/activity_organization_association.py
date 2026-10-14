from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_ref_type_0 import OrganizationRefType0


T = TypeVar("T", bound="ActivityOrganizationAssociation")


@_attrs_define
class ActivityOrganizationAssociation:
    """An association with an organization.

    Attributes:
        type_discriminator (str):
        organization (None | OrganizationRefType0): A reference to an organization in the institution
    """

    type_discriminator: str
    organization: None | OrganizationRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_ref_type_0 import OrganizationRefType0

        type_discriminator = self.type_discriminator

        organization: dict[str, Any] | None
        if isinstance(self.organization, OrganizationRefType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "organization": organization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.organization_ref_type_0 import OrganizationRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_organization(data: object) -> None | OrganizationRefType0:
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

        organization = _parse_organization(d.pop("organization"))

        activity_organization_association = cls(
            type_discriminator=type_discriminator,
            organization=organization,
        )

        activity_organization_association.additional_properties = d
        return activity_organization_association

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
