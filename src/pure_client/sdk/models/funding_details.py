from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )


T = TypeVar("T", bound="FundingDetails")


@_attrs_define
class FundingDetails:
    """Details about funding.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        funding_organizations (list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset): The internal or
            external funding organizations
        funding_organization_acronym (None | str | Unset): The acronym of the funding organization
        funding_numbers (list[str] | None | Unset): Funding numbers/IDs
    """

    pure_id: int | Unset = UNSET
    funding_organizations: (
        list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset
    ) = UNSET
    funding_organization_acronym: None | str | Unset = UNSET
    funding_numbers: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

        pure_id = self.pure_id

        funding_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.funding_organizations, Unset):
            funding_organizations = UNSET
        elif isinstance(self.funding_organizations, list):
            funding_organizations = []
            for funding_organizations_type_0_item_data in self.funding_organizations:
                funding_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    funding_organizations_type_0_item_data,
                    OrganizationOrExternalOrganizationRefType0,
                ):
                    funding_organizations_type_0_item = (
                        funding_organizations_type_0_item_data.to_dict()
                    )
                else:
                    funding_organizations_type_0_item = (
                        funding_organizations_type_0_item_data
                    )
                funding_organizations.append(funding_organizations_type_0_item)

        else:
            funding_organizations = self.funding_organizations

        funding_organization_acronym: None | str | Unset
        if isinstance(self.funding_organization_acronym, Unset):
            funding_organization_acronym = UNSET
        else:
            funding_organization_acronym = self.funding_organization_acronym

        funding_numbers: list[str] | None | Unset
        if isinstance(self.funding_numbers, Unset):
            funding_numbers = UNSET
        elif isinstance(self.funding_numbers, list):
            funding_numbers = self.funding_numbers

        else:
            funding_numbers = self.funding_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if funding_organizations is not UNSET:
            field_dict["fundingOrganizations"] = funding_organizations
        if funding_organization_acronym is not UNSET:
            field_dict["fundingOrganizationAcronym"] = funding_organization_acronym
        if funding_numbers is not UNSET:
            field_dict["fundingNumbers"] = funding_numbers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_funding_organizations(
            data: object,
        ) -> list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_organizations_type_0 = []
                _funding_organizations_type_0 = data
                for (
                    funding_organizations_type_0_item_data
                ) in _funding_organizations_type_0:

                    def _parse_funding_organizations_type_0_item(
                        data: object,
                    ) -> None | OrganizationOrExternalOrganizationRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_organization_or_external_organization_ref_type_0 = OrganizationOrExternalOrganizationRefType0.from_dict(
                                data
                            )

                            return componentsschemas_organization_or_external_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | OrganizationOrExternalOrganizationRefType0, data
                        )

                    funding_organizations_type_0_item = (
                        _parse_funding_organizations_type_0_item(
                            funding_organizations_type_0_item_data
                        )
                    )

                    funding_organizations_type_0.append(
                        funding_organizations_type_0_item
                    )

                return funding_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset,
                data,
            )

        funding_organizations = _parse_funding_organizations(
            d.pop("fundingOrganizations", UNSET)
        )

        def _parse_funding_organization_acronym(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funding_organization_acronym = _parse_funding_organization_acronym(
            d.pop("fundingOrganizationAcronym", UNSET)
        )

        def _parse_funding_numbers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_numbers_type_0 = cast(list[str], data)

                return funding_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        funding_numbers = _parse_funding_numbers(d.pop("fundingNumbers", UNSET))

        funding_details = cls(
            pure_id=pure_id,
            funding_organizations=funding_organizations,
            funding_organization_acronym=funding_organization_acronym,
            funding_numbers=funding_numbers,
        )

        funding_details.additional_properties = d
        return funding_details

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
