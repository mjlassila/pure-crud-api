from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.visibility import Visibility


T = TypeVar("T", bound="ApplicationFundingBudgetAssociation")


@_attrs_define
class ApplicationFundingBudgetAssociation:
    """A budget for a financial funding of an application.

    Attributes:
        visibility (Visibility): Visibility of an object
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        accounts (list[Account] | None | Unset): Associated accounts of the budget.
        cost_center (ClassificationRefType0 | None | Unset): A reference to a classification value
        cost_code (None | str | Unset): The cost code of the budget.
        organization (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
    """

    visibility: Visibility
    pure_id: int | Unset = UNSET
    accounts: list[Account] | None | Unset = UNSET
    cost_center: ClassificationRefType0 | None | Unset = UNSET
    cost_code: None | str | Unset = UNSET
    organization: None | OrganizationRefType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.organization_ref_type_0 import OrganizationRefType0

        visibility = self.visibility.to_dict()

        pure_id = self.pure_id

        accounts: list[dict[str, Any]] | None | Unset
        if isinstance(self.accounts, Unset):
            accounts = UNSET
        elif isinstance(self.accounts, list):
            accounts = []
            for accounts_type_0_item_data in self.accounts:
                accounts_type_0_item = accounts_type_0_item_data.to_dict()
                accounts.append(accounts_type_0_item)

        else:
            accounts = self.accounts

        cost_center: dict[str, Any] | None | Unset
        if isinstance(self.cost_center, Unset):
            cost_center = UNSET
        elif isinstance(self.cost_center, ClassificationRefType0):
            cost_center = self.cost_center.to_dict()
        else:
            cost_center = self.cost_center

        cost_code: None | str | Unset
        if isinstance(self.cost_code, Unset):
            cost_code = UNSET
        else:
            cost_code = self.cost_code

        organization: dict[str, Any] | None | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, OrganizationRefType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if cost_code is not UNSET:
            field_dict["costCode"] = cost_code
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.account import Account
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.visibility import Visibility

        d = dict(src_dict)
        visibility = Visibility.from_dict(d.pop("visibility"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_accounts(data: object) -> list[Account] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accounts_type_0 = []
                _accounts_type_0 = data
                for accounts_type_0_item_data in _accounts_type_0:
                    accounts_type_0_item = Account.from_dict(accounts_type_0_item_data)

                    accounts_type_0.append(accounts_type_0_item)

                return accounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Account] | None | Unset, data)

        accounts = _parse_accounts(d.pop("accounts", UNSET))

        def _parse_cost_center(data: object) -> ClassificationRefType0 | None | Unset:
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

        cost_center = _parse_cost_center(d.pop("costCenter", UNSET))

        def _parse_cost_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_code = _parse_cost_code(d.pop("costCode", UNSET))

        def _parse_organization(data: object) -> None | OrganizationRefType0 | Unset:
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

        organization = _parse_organization(d.pop("organization", UNSET))

        application_funding_budget_association = cls(
            visibility=visibility,
            pure_id=pure_id,
            accounts=accounts,
            cost_center=cost_center,
            cost_code=cost_code,
            organization=organization,
        )

        application_funding_budget_association.additional_properties = d
        return application_funding_budget_association

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
