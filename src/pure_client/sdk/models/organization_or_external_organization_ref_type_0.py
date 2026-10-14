from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.organization_ref_type_0 import OrganizationRefType0


T = TypeVar("T", bound="OrganizationOrExternalOrganizationRefType0")


@_attrs_define
class OrganizationOrExternalOrganizationRefType0:
    """A reference to an organization in the institution or an external organization

    Attributes:
        organization_ref (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
        external_organization_ref (ExternalOrganizationRefType0 | None | Unset): A reference to an organization external
            to the institution
    """

    organization_ref: None | OrganizationRefType0 | Unset = UNSET
    external_organization_ref: ExternalOrganizationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        organization_ref: dict[str, Any] | None | Unset
        if isinstance(self.organization_ref, Unset):
            organization_ref = UNSET
        elif isinstance(self.organization_ref, OrganizationRefType0):
            organization_ref = self.organization_ref.to_dict()
        else:
            organization_ref = self.organization_ref

        external_organization_ref: dict[str, Any] | None | Unset
        if isinstance(self.external_organization_ref, Unset):
            external_organization_ref = UNSET
        elif isinstance(self.external_organization_ref, ExternalOrganizationRefType0):
            external_organization_ref = self.external_organization_ref.to_dict()
        else:
            external_organization_ref = self.external_organization_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_ref is not UNSET:
            field_dict["organizationRef"] = organization_ref
        if external_organization_ref is not UNSET:
            field_dict["externalOrganizationRef"] = external_organization_ref

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        d = dict(src_dict)

        def _parse_organization_ref(
            data: object,
        ) -> None | OrganizationRefType0 | Unset:
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

        organization_ref = _parse_organization_ref(d.pop("organizationRef", UNSET))

        def _parse_external_organization_ref(
            data: object,
        ) -> ExternalOrganizationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(ExternalOrganizationRefType0 | None | Unset, data)

        external_organization_ref = _parse_external_organization_ref(
            d.pop("externalOrganizationRef", UNSET)
        )

        organization_or_external_organization_ref_type_0 = cls(
            organization_ref=organization_ref,
            external_organization_ref=external_organization_ref,
        )

        organization_or_external_organization_ref_type_0.additional_properties = d
        return organization_or_external_organization_ref_type_0

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
