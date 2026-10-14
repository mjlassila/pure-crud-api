from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDefinedFieldDateType0")


@_attrs_define
class CustomDefinedFieldDateType0:
    """Map of CustomDefinedField values, where the key is the field identifier

    Example:
        { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}

    Attributes:
        type_discriminator (str):
        value (datetime.date | None | Unset): The date value for the custom field
    """

    type_discriminator: str
    value: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_discriminator = self.type_discriminator

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_value(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_0 = isoparse(data).date()

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        custom_defined_field_date_type_0 = cls(
            type_discriminator=type_discriminator,
            value=value,
        )

        custom_defined_field_date_type_0.additional_properties = d
        return custom_defined_field_date_type_0

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
