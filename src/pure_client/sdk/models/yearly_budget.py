from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_currency_amount import SystemCurrencyAmount


T = TypeVar("T", bound="YearlyBudget")


@_attrs_define
class YearlyBudget:
    """A yearly budget of an account.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        budget (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency as defined by
            the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        year (int | None | Unset): The year of the yearly budget.
    """

    pure_id: int | Unset = UNSET
    budget: SystemCurrencyAmount | Unset = UNSET
    year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pure_id = self.pure_id

        budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if budget is not UNSET:
            field_dict["budget"] = budget
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_currency_amount import SystemCurrencyAmount

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        _budget = d.pop("budget", UNSET)
        budget: SystemCurrencyAmount | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = SystemCurrencyAmount.from_dict(_budget)

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        yearly_budget = cls(
            pure_id=pure_id,
            budget=budget,
            year=year,
        )

        yearly_budget.additional_properties = d
        return yearly_budget

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
