from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gender_type_0_key import GenderType0Key
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="GenderType0")


@_attrs_define
class GenderType0:
    """A list of possible genders

    Attributes:
        key (GenderType0Key | Unset):
        value (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
    """

    key: GenderType0Key | Unset = UNSET
    value: LocalizedStringType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_string_type_0 import LocalizedStringType0

        key: str | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

        value: dict[str, Any] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, LocalizedStringType0):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: GenderType0Key | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = GenderType0Key(_key)

        def _parse_value(data: object) -> LocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_localized_string_type_0 = (
                    LocalizedStringType0.from_dict(data)
                )

                return componentsschemas_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedStringType0 | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        gender_type_0 = cls(
            key=key,
            value=value,
        )

        gender_type_0.additional_properties = d
        return gender_type_0

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
