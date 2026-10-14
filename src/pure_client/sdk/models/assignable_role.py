from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="AssignableRole")


@_attrs_define
class AssignableRole:
    """An assignable role

    Attributes:
        assignable_role_name (str): The name of the assignable role
        target_system_name (None | str | Unset): The name of the target system
        title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
    """

    assignable_role_name: str
    target_system_name: None | str | Unset = UNSET
    title: LocalizedStringType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_string_type_0 import LocalizedStringType0

        assignable_role_name = self.assignable_role_name

        target_system_name: None | str | Unset
        if isinstance(self.target_system_name, Unset):
            target_system_name = UNSET
        else:
            target_system_name = self.target_system_name

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignableRoleName": assignable_role_name,
            }
        )
        if target_system_name is not UNSET:
            field_dict["targetSystemName"] = target_system_name
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        assignable_role_name = d.pop("assignableRoleName")

        def _parse_target_system_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_system_name = _parse_target_system_name(d.pop("targetSystemName", UNSET))

        def _parse_title(data: object) -> LocalizedStringType0 | None | Unset:
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

        title = _parse_title(d.pop("title", UNSET))

        assignable_role = cls(
            assignable_role_name=assignable_role_name,
            target_system_name=target_system_name,
            title=title,
        )

        assignable_role.additional_properties = d
        return assignable_role

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
