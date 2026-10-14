from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount
    from ..models.system_currency_amount import SystemCurrencyAmount


T = TypeVar("T", bound="ArticleProcessingCharge")


@_attrs_define
class ArticleProcessingCharge:
    """Holds information on the article processing charge

    Attributes:
        paid (bool | Unset): This value is true if the processing charge has been paid, false if not and null/not
            presentif unknown or not noted on content.
        amount_in_currency (CurrencyAmount | Unset): A monetary value in the specified currency as defined by the W3C's
            Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        amount (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency as defined by
            the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
    """

    paid: bool | Unset = UNSET
    amount_in_currency: CurrencyAmount | Unset = UNSET
    amount: SystemCurrencyAmount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid = self.paid

        amount_in_currency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount_in_currency, Unset):
            amount_in_currency = self.amount_in_currency.to_dict()

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paid is not UNSET:
            field_dict["paid"] = paid
        if amount_in_currency is not UNSET:
            field_dict["amountInCurrency"] = amount_in_currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.currency_amount import CurrencyAmount
        from ..models.system_currency_amount import SystemCurrencyAmount

        d = dict(src_dict)
        paid = d.pop("paid", UNSET)

        _amount_in_currency = d.pop("amountInCurrency", UNSET)
        amount_in_currency: CurrencyAmount | Unset
        if isinstance(_amount_in_currency, Unset):
            amount_in_currency = UNSET
        else:
            amount_in_currency = CurrencyAmount.from_dict(_amount_in_currency)

        _amount = d.pop("amount", UNSET)
        amount: SystemCurrencyAmount | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = SystemCurrencyAmount.from_dict(_amount)

        article_processing_charge = cls(
            paid=paid,
            amount_in_currency=amount_in_currency,
            amount=amount,
        )

        article_processing_charge.additional_properties = d
        return article_processing_charge

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
