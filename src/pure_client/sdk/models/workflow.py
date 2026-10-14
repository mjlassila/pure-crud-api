from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_localized_string_type_0 import SystemLocalizedStringType0


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """Information about workflow

    Attributes:
        step (str): Current workflow step
        description (None | SystemLocalizedStringType0 | Unset): A set of localized string values each for a specific UI
            locale. Example: {'en_GB': 'Some text'}.
    """

    step: str
    description: None | SystemLocalizedStringType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        step = self.step

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, SystemLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        d = dict(src_dict)
        step = d.pop("step")

        def _parse_description(
            data: object,
        ) -> None | SystemLocalizedStringType0 | Unset:
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

        description = _parse_description(d.pop("description", UNSET))

        workflow = cls(
            step=step,
            description=description,
        )

        workflow.additional_properties = d
        return workflow

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
