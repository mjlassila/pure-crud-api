from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.system_currency_amount import SystemCurrencyAmount


T = TypeVar("T", bound="ApplicationExternalFinancialFundingCollaboratorAssociation")


@_attrs_define
class ApplicationExternalFinancialFundingCollaboratorAssociation:
    """An external collaborator for a financial funding.

    Attributes:
        type_discriminator (str):
        collaborator (ExternalOrganizationRefType0 | None): A reference to an organization external to the institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        institutional_part (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency
            as defined by the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-
            dictionary
    """

    type_discriminator: str
    collaborator: ExternalOrganizationRefType0 | None
    pure_id: int | Unset = UNSET
    institutional_part: SystemCurrencyAmount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )

        type_discriminator = self.type_discriminator

        collaborator: dict[str, Any] | None
        if isinstance(self.collaborator, ExternalOrganizationRefType0):
            collaborator = self.collaborator.to_dict()
        else:
            collaborator = self.collaborator

        pure_id = self.pure_id

        institutional_part: dict[str, Any] | Unset = UNSET
        if not isinstance(self.institutional_part, Unset):
            institutional_part = self.institutional_part.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "collaborator": collaborator,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if institutional_part is not UNSET:
            field_dict["institutionalPart"] = institutional_part

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.system_currency_amount import SystemCurrencyAmount

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_collaborator(data: object) -> ExternalOrganizationRefType0 | None:
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

        collaborator = _parse_collaborator(d.pop("collaborator"))

        pure_id = d.pop("pureId", UNSET)

        _institutional_part = d.pop("institutionalPart", UNSET)
        institutional_part: SystemCurrencyAmount | Unset
        if isinstance(_institutional_part, Unset):
            institutional_part = UNSET
        else:
            institutional_part = SystemCurrencyAmount.from_dict(_institutional_part)

        application_external_financial_funding_collaborator_association = cls(
            type_discriminator=type_discriminator,
            collaborator=collaborator,
            pure_id=pure_id,
            institutional_part=institutional_part,
        )

        application_external_financial_funding_collaborator_association.additional_properties = d
        return application_external_financial_funding_collaborator_association

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
