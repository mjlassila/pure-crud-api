from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """A hyperlink describing a location on the web.

    Attributes:
        url (str): The URL (Uniform Resource Locator) of the link
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        alias (None | str | Unset): A user-friendly text to show instead of the URL
        description (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        link_type (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    url: str
    pure_id: int | Unset = UNSET
    alias: None | str | Unset = UNSET
    description: LocalizedStringType0 | None | Unset = UNSET
    link_type: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0

        url = self.url

        pure_id = self.pure_id

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, LocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        link_type: dict[str, Any] | None | Unset
        if isinstance(self.link_type, Unset):
            link_type = UNSET
        elif isinstance(self.link_type, ClassificationRefType0):
            link_type = self.link_type.to_dict()
        else:
            link_type = self.link_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if link_type is not UNSET:
            field_dict["linkType"] = link_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        url = d.pop("url")

        pure_id = d.pop("pureId", UNSET)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_description(data: object) -> LocalizedStringType0 | None | Unset:
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

        description = _parse_description(d.pop("description", UNSET))

        def _parse_link_type(data: object) -> ClassificationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_classification_ref_type_0 = (
                    ClassificationRefType0.from_dict(data)
                )

                return componentsschemas_classification_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClassificationRefType0 | None | Unset, data)

        link_type = _parse_link_type(d.pop("linkType", UNSET))

        link = cls(
            url=url,
            pure_id=pure_id,
            alias=alias,
            description=description,
            link_type=link_type,
        )

        link.additional_properties = d
        return link

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
