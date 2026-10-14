from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_entry import AccountEntry
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.system_currency_amount import SystemCurrencyAmount
    from ..models.yearly_budget import YearlyBudget


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """An account of a budget.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        budget (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency as defined by
            the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        classification (ClassificationRefType0 | None | Unset): A reference to a classification value
        cost_center (ClassificationRefType0 | None | Unset): A reference to a classification value
        entries (list[AccountEntry] | None | Unset): Associated account entries of the account.
        funder_contribution (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency
            as defined by the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-
            dictionary
        recovery_percentage (float | None | Unset): The recovery percentage of the budget.
        specification (None | str | Unset): The specification of the budget.
        yearly_budgets (list[YearlyBudget] | None | Unset): Yearly budgets of the account.
    """

    pure_id: int | Unset = UNSET
    budget: SystemCurrencyAmount | Unset = UNSET
    classification: ClassificationRefType0 | None | Unset = UNSET
    cost_center: ClassificationRefType0 | None | Unset = UNSET
    entries: list[AccountEntry] | None | Unset = UNSET
    funder_contribution: SystemCurrencyAmount | Unset = UNSET
    recovery_percentage: float | None | Unset = UNSET
    specification: None | str | Unset = UNSET
    yearly_budgets: list[YearlyBudget] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        pure_id = self.pure_id

        budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        classification: dict[str, Any] | None | Unset
        if isinstance(self.classification, Unset):
            classification = UNSET
        elif isinstance(self.classification, ClassificationRefType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        cost_center: dict[str, Any] | None | Unset
        if isinstance(self.cost_center, Unset):
            cost_center = UNSET
        elif isinstance(self.cost_center, ClassificationRefType0):
            cost_center = self.cost_center.to_dict()
        else:
            cost_center = self.cost_center

        entries: list[dict[str, Any]] | None | Unset
        if isinstance(self.entries, Unset):
            entries = UNSET
        elif isinstance(self.entries, list):
            entries = []
            for entries_type_0_item_data in self.entries:
                entries_type_0_item = entries_type_0_item_data.to_dict()
                entries.append(entries_type_0_item)

        else:
            entries = self.entries

        funder_contribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funder_contribution, Unset):
            funder_contribution = self.funder_contribution.to_dict()

        recovery_percentage: float | None | Unset
        if isinstance(self.recovery_percentage, Unset):
            recovery_percentage = UNSET
        else:
            recovery_percentage = self.recovery_percentage

        specification: None | str | Unset
        if isinstance(self.specification, Unset):
            specification = UNSET
        else:
            specification = self.specification

        yearly_budgets: list[dict[str, Any]] | None | Unset
        if isinstance(self.yearly_budgets, Unset):
            yearly_budgets = UNSET
        elif isinstance(self.yearly_budgets, list):
            yearly_budgets = []
            for yearly_budgets_type_0_item_data in self.yearly_budgets:
                yearly_budgets_type_0_item = yearly_budgets_type_0_item_data.to_dict()
                yearly_budgets.append(yearly_budgets_type_0_item)

        else:
            yearly_budgets = self.yearly_budgets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if budget is not UNSET:
            field_dict["budget"] = budget
        if classification is not UNSET:
            field_dict["classification"] = classification
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if entries is not UNSET:
            field_dict["entries"] = entries
        if funder_contribution is not UNSET:
            field_dict["funderContribution"] = funder_contribution
        if recovery_percentage is not UNSET:
            field_dict["recoveryPercentage"] = recovery_percentage
        if specification is not UNSET:
            field_dict["specification"] = specification
        if yearly_budgets is not UNSET:
            field_dict["yearlyBudgets"] = yearly_budgets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.account_entry import AccountEntry
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.system_currency_amount import SystemCurrencyAmount
        from ..models.yearly_budget import YearlyBudget

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        _budget = d.pop("budget", UNSET)
        budget: SystemCurrencyAmount | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = SystemCurrencyAmount.from_dict(_budget)

        def _parse_classification(
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

        classification = _parse_classification(d.pop("classification", UNSET))

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

        def _parse_entries(data: object) -> list[AccountEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entries_type_0 = []
                _entries_type_0 = data
                for entries_type_0_item_data in _entries_type_0:
                    entries_type_0_item = AccountEntry.from_dict(
                        entries_type_0_item_data
                    )

                    entries_type_0.append(entries_type_0_item)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccountEntry] | None | Unset, data)

        entries = _parse_entries(d.pop("entries", UNSET))

        _funder_contribution = d.pop("funderContribution", UNSET)
        funder_contribution: SystemCurrencyAmount | Unset
        if isinstance(_funder_contribution, Unset):
            funder_contribution = UNSET
        else:
            funder_contribution = SystemCurrencyAmount.from_dict(_funder_contribution)

        def _parse_recovery_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        recovery_percentage = _parse_recovery_percentage(
            d.pop("recoveryPercentage", UNSET)
        )

        def _parse_specification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        specification = _parse_specification(d.pop("specification", UNSET))

        def _parse_yearly_budgets(data: object) -> list[YearlyBudget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                yearly_budgets_type_0 = []
                _yearly_budgets_type_0 = data
                for yearly_budgets_type_0_item_data in _yearly_budgets_type_0:
                    yearly_budgets_type_0_item = YearlyBudget.from_dict(
                        yearly_budgets_type_0_item_data
                    )

                    yearly_budgets_type_0.append(yearly_budgets_type_0_item)

                return yearly_budgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[YearlyBudget] | None | Unset, data)

        yearly_budgets = _parse_yearly_budgets(d.pop("yearlyBudgets", UNSET))

        account = cls(
            pure_id=pure_id,
            budget=budget,
            classification=classification,
            cost_center=cost_center,
            entries=entries,
            funder_contribution=funder_contribution,
            recovery_percentage=recovery_percentage,
            specification=specification,
            yearly_budgets=yearly_budgets,
        )

        account.additional_properties = d
        return account

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
