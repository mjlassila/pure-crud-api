from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_financial_funding_collaborator_association import (
        AwardFinancialFundingCollaboratorAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.currency_amount import CurrencyAmount
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.system_currency_amount import SystemCurrencyAmount
    from ..models.visibility import Visibility


T = TypeVar("T", bound="AwardFinancialFundingAssociation")


@_attrs_define
class AwardFinancialFundingAssociation:
    """A financial funding is used when money is provided by the funder. It holds information about amounts and splits with
    collaborators.

        Attributes:
            type_discriminator (str):
            awarded_amount (SystemCurrencyAmount): A monetary value in the Pure installation's system currency as defined by
                the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
            pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
            cost_code (None | str | Unset): The cost code of the funding.
            funder (ExternalOrganizationRefType0 | None | Unset): A reference to an organization external to the institution
            internal_funder (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
            classifications (list[ClassificationRefType0 | None] | None | Unset): Related classifications of the funding.
            funding_project_scheme (None | str | Unset): The funding project scheme of the funding, also known as research
                program.
            visibility (Visibility | Unset): Visibility of an object
            awarded_amount_in_awarded_currency (CurrencyAmount | Unset): A monetary value in the specified currency as
                defined by the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-
                dictionary
            funding_collaborators (list[AwardFinancialFundingCollaboratorAssociation] | None | Unset): The collaborators of
                the funding. It's currently only possible to associate a single internal collaborator. There external
                collaborators must follow the collaborators associated with the award.
    """

    type_discriminator: str
    awarded_amount: SystemCurrencyAmount
    pure_id: int | Unset = UNSET
    cost_code: None | str | Unset = UNSET
    funder: ExternalOrganizationRefType0 | None | Unset = UNSET
    internal_funder: None | OrganizationRefType0 | Unset = UNSET
    classifications: list[ClassificationRefType0 | None] | None | Unset = UNSET
    funding_project_scheme: None | str | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    awarded_amount_in_awarded_currency: CurrencyAmount | Unset = UNSET
    funding_collaborators: (
        list[AwardFinancialFundingCollaboratorAssociation] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0

        type_discriminator = self.type_discriminator

        awarded_amount = self.awarded_amount.to_dict()

        pure_id = self.pure_id

        cost_code: None | str | Unset
        if isinstance(self.cost_code, Unset):
            cost_code = UNSET
        else:
            cost_code = self.cost_code

        funder: dict[str, Any] | None | Unset
        if isinstance(self.funder, Unset):
            funder = UNSET
        elif isinstance(self.funder, ExternalOrganizationRefType0):
            funder = self.funder.to_dict()
        else:
            funder = self.funder

        internal_funder: dict[str, Any] | None | Unset
        if isinstance(self.internal_funder, Unset):
            internal_funder = UNSET
        elif isinstance(self.internal_funder, OrganizationRefType0):
            internal_funder = self.internal_funder.to_dict()
        else:
            internal_funder = self.internal_funder

        classifications: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.classifications, Unset):
            classifications = UNSET
        elif isinstance(self.classifications, list):
            classifications = []
            for classifications_type_0_item_data in self.classifications:
                classifications_type_0_item: dict[str, Any] | None
                if isinstance(classifications_type_0_item_data, ClassificationRefType0):
                    classifications_type_0_item = (
                        classifications_type_0_item_data.to_dict()
                    )
                else:
                    classifications_type_0_item = classifications_type_0_item_data
                classifications.append(classifications_type_0_item)

        else:
            classifications = self.classifications

        funding_project_scheme: None | str | Unset
        if isinstance(self.funding_project_scheme, Unset):
            funding_project_scheme = UNSET
        else:
            funding_project_scheme = self.funding_project_scheme

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        awarded_amount_in_awarded_currency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.awarded_amount_in_awarded_currency, Unset):
            awarded_amount_in_awarded_currency = (
                self.awarded_amount_in_awarded_currency.to_dict()
            )

        funding_collaborators: list[dict[str, Any]] | None | Unset
        if isinstance(self.funding_collaborators, Unset):
            funding_collaborators = UNSET
        elif isinstance(self.funding_collaborators, list):
            funding_collaborators = []
            for funding_collaborators_type_0_item_data in self.funding_collaborators:
                funding_collaborators_type_0_item = (
                    funding_collaborators_type_0_item_data.to_dict()
                )
                funding_collaborators.append(funding_collaborators_type_0_item)

        else:
            funding_collaborators = self.funding_collaborators

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "awardedAmount": awarded_amount,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if cost_code is not UNSET:
            field_dict["costCode"] = cost_code
        if funder is not UNSET:
            field_dict["funder"] = funder
        if internal_funder is not UNSET:
            field_dict["internalFunder"] = internal_funder
        if classifications is not UNSET:
            field_dict["classifications"] = classifications
        if funding_project_scheme is not UNSET:
            field_dict["fundingProjectScheme"] = funding_project_scheme
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if awarded_amount_in_awarded_currency is not UNSET:
            field_dict["awardedAmountInAwardedCurrency"] = (
                awarded_amount_in_awarded_currency
            )
        if funding_collaborators is not UNSET:
            field_dict["fundingCollaborators"] = funding_collaborators

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.award_financial_funding_collaborator_association import (
            AwardFinancialFundingCollaboratorAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.currency_amount import CurrencyAmount
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.system_currency_amount import SystemCurrencyAmount
        from ..models.visibility import Visibility

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        awarded_amount = SystemCurrencyAmount.from_dict(d.pop("awardedAmount"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_cost_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_code = _parse_cost_code(d.pop("costCode", UNSET))

        def _parse_funder(data: object) -> ExternalOrganizationRefType0 | None | Unset:
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

        funder = _parse_funder(d.pop("funder", UNSET))

        def _parse_internal_funder(data: object) -> None | OrganizationRefType0 | Unset:
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

        internal_funder = _parse_internal_funder(d.pop("internalFunder", UNSET))

        def _parse_classifications(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                classifications_type_0 = []
                _classifications_type_0 = data
                for classifications_type_0_item_data in _classifications_type_0:

                    def _parse_classifications_type_0_item(
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

                    classifications_type_0_item = _parse_classifications_type_0_item(
                        classifications_type_0_item_data
                    )

                    classifications_type_0.append(classifications_type_0_item)

                return classifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        classifications = _parse_classifications(d.pop("classifications", UNSET))

        def _parse_funding_project_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funding_project_scheme = _parse_funding_project_scheme(
            d.pop("fundingProjectScheme", UNSET)
        )

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        _awarded_amount_in_awarded_currency = d.pop(
            "awardedAmountInAwardedCurrency", UNSET
        )
        awarded_amount_in_awarded_currency: CurrencyAmount | Unset
        if isinstance(_awarded_amount_in_awarded_currency, Unset):
            awarded_amount_in_awarded_currency = UNSET
        else:
            awarded_amount_in_awarded_currency = CurrencyAmount.from_dict(
                _awarded_amount_in_awarded_currency
            )

        def _parse_funding_collaborators(
            data: object,
        ) -> list[AwardFinancialFundingCollaboratorAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_collaborators_type_0 = []
                _funding_collaborators_type_0 = data
                for (
                    funding_collaborators_type_0_item_data
                ) in _funding_collaborators_type_0:
                    funding_collaborators_type_0_item = (
                        AwardFinancialFundingCollaboratorAssociation.from_dict(
                            funding_collaborators_type_0_item_data
                        )
                    )

                    funding_collaborators_type_0.append(
                        funding_collaborators_type_0_item
                    )

                return funding_collaborators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AwardFinancialFundingCollaboratorAssociation] | None | Unset, data
            )

        funding_collaborators = _parse_funding_collaborators(
            d.pop("fundingCollaborators", UNSET)
        )

        award_financial_funding_association = cls(
            type_discriminator=type_discriminator,
            awarded_amount=awarded_amount,
            pure_id=pure_id,
            cost_code=cost_code,
            funder=funder,
            internal_funder=internal_funder,
            classifications=classifications,
            funding_project_scheme=funding_project_scheme,
            visibility=visibility,
            awarded_amount_in_awarded_currency=awarded_amount_in_awarded_currency,
            funding_collaborators=funding_collaborators,
        )

        award_financial_funding_association.additional_properties = d
        return award_financial_funding_association

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
