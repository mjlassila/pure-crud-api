from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_currency_amount import SystemCurrencyAmount
    from ..models.year_month_type_0 import YearMonthType0


T = TypeVar("T", bound="AccountEntry")


@_attrs_define
class AccountEntry:
    """An account entry of an account.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        amount (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency as defined by
            the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        year_month (None | Unset | YearMonthType0): A date that can be defined by only year and month
        commitment (bool | Unset): Is the entry only a commitment?
    """

    pure_id: int | Unset = UNSET
    amount: SystemCurrencyAmount | Unset = UNSET
    year_month: None | Unset | YearMonthType0 = UNSET
    commitment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.year_month_type_0 import YearMonthType0

        pure_id = self.pure_id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        year_month: dict[str, Any] | None | Unset
        if isinstance(self.year_month, Unset):
            year_month = UNSET
        elif isinstance(self.year_month, YearMonthType0):
            year_month = self.year_month.to_dict()
        else:
            year_month = self.year_month

        commitment = self.commitment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if year_month is not UNSET:
            field_dict["yearMonth"] = year_month
        if commitment is not UNSET:
            field_dict["commitment"] = commitment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_currency_amount import SystemCurrencyAmount
        from ..models.year_month_type_0 import YearMonthType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        _amount = d.pop("amount", UNSET)
        amount: SystemCurrencyAmount | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = SystemCurrencyAmount.from_dict(_amount)

        def _parse_year_month(data: object) -> None | Unset | YearMonthType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_year_month_type_0 = YearMonthType0.from_dict(data)

                return componentsschemas_year_month_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | YearMonthType0, data)

        year_month = _parse_year_month(d.pop("yearMonth", UNSET))

        commitment = d.pop("commitment", UNSET)

        account_entry = cls(
            pure_id=pure_id,
            amount=amount,
            year_month=year_month,
            commitment=commitment,
        )

        account_entry.additional_properties = d
        return account_entry

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
