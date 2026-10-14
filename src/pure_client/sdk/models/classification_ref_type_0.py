from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_localized_string_type_0 import SystemLocalizedStringType0


T = TypeVar("T", bound="ClassificationRefType0")


@_attrs_define
class ClassificationRefType0:
    """A reference to a classification value

    Attributes:
        uri (str): Classification URI of the referred classification
        term (None | SystemLocalizedStringType0 | Unset): A set of localized string values each for a specific UI
            locale. Example: {'en_GB': 'Some text'}.
    """

    uri: str
    term: None | SystemLocalizedStringType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        uri = self.uri

        term: dict[str, Any] | None | Unset
        if isinstance(self.term, Unset):
            term = UNSET
        elif isinstance(self.term, SystemLocalizedStringType0):
            term = self.term.to_dict()
        else:
            term = self.term

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
            }
        )
        if term is not UNSET:
            field_dict["term"] = term

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        d = dict(src_dict)
        uri = d.pop("uri")

        def _parse_term(data: object) -> None | SystemLocalizedStringType0 | Unset:
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

        term = _parse_term(d.pop("term", UNSET))

        classification_ref_type_0 = cls(
            uri=uri,
            term=term,
        )

        classification_ref_type_0.additional_properties = d
        return classification_ref_type_0

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
