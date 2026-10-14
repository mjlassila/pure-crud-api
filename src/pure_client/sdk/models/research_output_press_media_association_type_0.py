from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.press_media_ref_type_0 import PressMediaRefType0


T = TypeVar("T", bound="ResearchOutputPressMediaAssociationType0")


@_attrs_define
class ResearchOutputPressMediaAssociationType0:
    """An association to a press media.

    Attributes:
        press_media (None | PressMediaRefType0): A reference to a press/media
    """

    press_media: None | PressMediaRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.press_media_ref_type_0 import PressMediaRefType0

        press_media: dict[str, Any] | None
        if isinstance(self.press_media, PressMediaRefType0):
            press_media = self.press_media.to_dict()
        else:
            press_media = self.press_media

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pressMedia": press_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.press_media_ref_type_0 import PressMediaRefType0

        d = dict(src_dict)

        def _parse_press_media(data: object) -> None | PressMediaRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_press_media_ref_type_0 = PressMediaRefType0.from_dict(
                    data
                )

                return componentsschemas_press_media_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PressMediaRefType0, data)

        press_media = _parse_press_media(d.pop("pressMedia"))

        research_output_press_media_association_type_0 = cls(
            press_media=press_media,
        )

        research_output_press_media_association_type_0.additional_properties = d
        return research_output_press_media_association_type_0

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
