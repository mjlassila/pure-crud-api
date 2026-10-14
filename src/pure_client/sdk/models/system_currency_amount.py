from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemCurrencyAmount")


@_attrs_define
class SystemCurrencyAmount:
    """A monetary value in the Pure installation's system currency as defined by the W3C's Payment Request standard:
    https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary

        Attributes:
            value (str): A valid decimal monetary value as defined by the W3C's Payment Request standard:
                https://www.w3.org/TR/payment-request/#dom-paymentcurrencyamount-value
            currency (str | Unset): An ISO-4217 3-letter alphabetic code representing the Pure installation's system
                currency as defined by the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#dom-
                paymentcurrencyamount-currency
    """

    value: str
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value")

        currency = d.pop("currency", UNSET)

        system_currency_amount = cls(
            value=value,
            currency=currency,
        )

        system_currency_amount.additional_properties = d
        return system_currency_amount

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
