from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_ref_type_0 import AwardRefType0
    from ..models.system_currency_amount import SystemCurrencyAmount


T = TypeVar("T", bound="ContractAwardAssociation")


@_attrs_define
class ContractAwardAssociation:
    """An association with an award

    Attributes:
        award (AwardRefType0 | None): A reference to an award
        value (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency as defined by
            the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        note (None | str | Unset): Association note
    """

    award: AwardRefType0 | None
    value: SystemCurrencyAmount | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.award_ref_type_0 import AwardRefType0

        award: dict[str, Any] | None
        if isinstance(self.award, AwardRefType0):
            award = self.award.to_dict()
        else:
            award = self.award

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "award": award,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.system_currency_amount import SystemCurrencyAmount

        d = dict(src_dict)

        def _parse_award(data: object) -> AwardRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_award_ref_type_0 = AwardRefType0.from_dict(data)

                return componentsschemas_award_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwardRefType0 | None, data)

        award = _parse_award(d.pop("award"))

        _value = d.pop("value", UNSET)
        value: SystemCurrencyAmount | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = SystemCurrencyAmount.from_dict(_value)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        contract_award_association = cls(
            award=award,
            value=value,
            note=note,
        )

        contract_award_association.additional_properties = d
        return contract_award_association

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
