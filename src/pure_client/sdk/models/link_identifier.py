from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkIdentifier")


@_attrs_define
class LinkIdentifier:
    """A link identifier

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        link_identifier (None | str | Unset): The link identifier
    """

    pure_id: int | Unset = UNSET
    link_identifier: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pure_id = self.pure_id

        link_identifier: None | str | Unset
        if isinstance(self.link_identifier, Unset):
            link_identifier = UNSET
        else:
            link_identifier = self.link_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if link_identifier is not UNSET:
            field_dict["linkIdentifier"] = link_identifier

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_link_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link_identifier = _parse_link_identifier(d.pop("linkIdentifier", UNSET))

        link_identifier = cls(
            pure_id=pure_id,
            link_identifier=link_identifier,
        )

        link_identifier.additional_properties = d
        return link_identifier

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
