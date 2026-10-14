from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_localized_string_type_0 import SystemLocalizedStringType0


T = TypeVar("T", bound="ValidationError")


@_attrs_define
class ValidationError:
    """Validation error

    Attributes:
        path (str | Unset):
        code (str | Unset):
        title (None | SystemLocalizedStringType0 | Unset): A set of localized string values each for a specific UI
            locale. Example: {'en_GB': 'Some text'}.
    """

    path: str | Unset = UNSET
    code: str | Unset = UNSET
    title: None | SystemLocalizedStringType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        path = self.path

        code = self.code

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, SystemLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        code = d.pop("code", UNSET)

        def _parse_title(data: object) -> None | SystemLocalizedStringType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_system_localized_string_type_0 = (
                    SystemLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_system_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemLocalizedStringType0 | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        validation_error = cls(
            path=path,
            code=code,
            title=title,
        )

        validation_error.additional_properties = d
        return validation_error

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
