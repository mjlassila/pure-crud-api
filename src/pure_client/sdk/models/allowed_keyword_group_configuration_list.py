from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_keyword_group_configuration import (
        AllowedKeywordGroupConfiguration,
    )


T = TypeVar("T", bound="AllowedKeywordGroupConfigurationList")


@_attrs_define
class AllowedKeywordGroupConfigurationList:
    """List of allowed keyword group configurations

    Attributes:
        configurations (list[AllowedKeywordGroupConfiguration] | Unset):
    """

    configurations: list[AllowedKeywordGroupConfiguration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = []
            for configurations_item_data in self.configurations:
                configurations_item = configurations_item_data.to_dict()
                configurations.append(configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configurations is not UNSET:
            field_dict["configurations"] = configurations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.allowed_keyword_group_configuration import (
            AllowedKeywordGroupConfiguration,
        )

        d = dict(src_dict)
        _configurations = d.pop("configurations", UNSET)
        configurations: list[AllowedKeywordGroupConfiguration] | Unset = UNSET
        if _configurations is not UNSET:
            configurations = []
            for configurations_item_data in _configurations:
                configurations_item = AllowedKeywordGroupConfiguration.from_dict(
                    configurations_item_data
                )

                configurations.append(configurations_item)

        allowed_keyword_group_configuration_list = cls(
            configurations=configurations,
        )

        allowed_keyword_group_configuration_list.additional_properties = d
        return allowed_keyword_group_configuration_list

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
