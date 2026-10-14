from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CurrencyAmount")


@_attrs_define
class CurrencyAmount:
    """A monetary value in the specified currency as defined by the W3C's Payment Request standard:
    https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary

        Attributes:
            currency (str): An ISO-4217 3-letter alphabetic code as defined by the W3C's Payment Request standard:
                https://www.w3.org/TR/payment-request/#dom-paymentcurrencyamount-currency
            value (str): A valid decimal monetary value as defined by the W3C's Payment Request standard:
                https://www.w3.org/TR/payment-request/#dom-paymentcurrencyamount-value
    """

    currency: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        currency = d.pop("currency")

        value = d.pop("value")

        currency_amount = cls(
            currency=currency,
            value=value,
        )

        currency_amount.additional_properties = d
        return currency_amount

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
