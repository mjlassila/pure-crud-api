from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ISSNRef")


@_attrs_define
class ISSNRef:
    """A reference to a journal ISSN

    Attributes:
        pure_id (int): Pure database ID of the ISSN. This is found by retrieving the Journal and going through the ISSNs
            collection.
        issn (str | Unset): The actual ISSN value
    """

    pure_id: int
    issn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pure_id = self.pure_id

        issn = self.issn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pureId": pure_id,
            }
        )
        if issn is not UNSET:
            field_dict["issn"] = issn

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pure_id = d.pop("pureId")

        issn = d.pop("issn", UNSET)

        issn_ref = cls(
            pure_id=pure_id,
            issn=issn,
        )

        issn_ref.additional_properties = d
        return issn_ref

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
