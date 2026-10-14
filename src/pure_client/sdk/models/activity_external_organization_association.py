from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0


T = TypeVar("T", bound="ActivityExternalOrganizationAssociation")


@_attrs_define
class ActivityExternalOrganizationAssociation:
    """An association with an external organization.

    Attributes:
        type_discriminator (str):
        external_organization (ExternalOrganizationRefType0 | None): A reference to an organization external to the
            institution
    """

    type_discriminator: str
    external_organization: ExternalOrganizationRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )

        type_discriminator = self.type_discriminator

        external_organization: dict[str, Any] | None
        if isinstance(self.external_organization, ExternalOrganizationRefType0):
            external_organization = self.external_organization.to_dict()
        else:
            external_organization = self.external_organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "externalOrganization": external_organization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

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

        activity_external_organization_association = cls(
            type_discriminator=type_discriminator,
            external_organization=external_organization,
        )

        activity_external_organization_association.additional_properties = d
        return activity_external_organization_association

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
