from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_scheme_ref_type_0 import ClassificationSchemeRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="AllowedKeywordGroupConfiguration")


@_attrs_define
class AllowedKeywordGroupConfiguration:
    """A specification of the allowed behavior of a specified keyword group

    Attributes:
        target_system_name (str): The content system name this configuration applies to
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        keyword_group_type (str | Unset): The OpenAPI schema type of this keyword configuration
        name (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        description (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        classification_scheme (ClassificationSchemeRefType0 | None | Unset): A reference to a classification scheme
        allow_userdefined_keywords (bool | Unset): Defines if user defined keywords are allowed
        limit_to_leaf_selection (bool | Unset):
        logical_name (str | Unset):
        relation_type (None | str | Unset): The schema name of the type (with the ability to associate keywords) on
            which the keyword group configuration is related to, e.g. StaffOrganizationAssociation. It can also be set to
            null (default value), which means the keyword group configuration is related to the main type (the target system
            name) and not a relation of the main type.
    """

    target_system_name: str
    pure_id: int | Unset = UNSET
    keyword_group_type: str | Unset = UNSET
    name: LocalizedStringType0 | None | Unset = UNSET
    description: FormattedLocalizedStringType0 | None | Unset = UNSET
    classification_scheme: ClassificationSchemeRefType0 | None | Unset = UNSET
    allow_userdefined_keywords: bool | Unset = UNSET
    limit_to_leaf_selection: bool | Unset = UNSET
    logical_name: str | Unset = UNSET
    relation_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_scheme_ref_type_0 import (
            ClassificationSchemeRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        target_system_name = self.target_system_name

        pure_id = self.pure_id

        keyword_group_type = self.keyword_group_type

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, LocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, FormattedLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        classification_scheme: dict[str, Any] | None | Unset
        if isinstance(self.classification_scheme, Unset):
            classification_scheme = UNSET
        elif isinstance(self.classification_scheme, ClassificationSchemeRefType0):
            classification_scheme = self.classification_scheme.to_dict()
        else:
            classification_scheme = self.classification_scheme

        allow_userdefined_keywords = self.allow_userdefined_keywords

        limit_to_leaf_selection = self.limit_to_leaf_selection

        logical_name = self.logical_name

        relation_type: None | str | Unset
        if isinstance(self.relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetSystemName": target_system_name,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if keyword_group_type is not UNSET:
            field_dict["keywordGroupType"] = keyword_group_type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if classification_scheme is not UNSET:
            field_dict["classificationScheme"] = classification_scheme
        if allow_userdefined_keywords is not UNSET:
            field_dict["allowUserdefinedKeywords"] = allow_userdefined_keywords
        if limit_to_leaf_selection is not UNSET:
            field_dict["limitToLeafSelection"] = limit_to_leaf_selection
        if logical_name is not UNSET:
            field_dict["logicalName"] = logical_name
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_scheme_ref_type_0 import (
            ClassificationSchemeRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        target_system_name = d.pop("targetSystemName")

        pure_id = d.pop("pureId", UNSET)

        keyword_group_type = d.pop("keywordGroupType", UNSET)

        def _parse_name(data: object) -> LocalizedStringType0 | None | Unset:
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

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(
            data: object,
        ) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_classification_scheme(
            data: object,
        ) -> ClassificationSchemeRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_classification_scheme_ref_type_0 = (
                    ClassificationSchemeRefType0.from_dict(data)
                )

                return componentsschemas_classification_scheme_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClassificationSchemeRefType0 | None | Unset, data)

        classification_scheme = _parse_classification_scheme(
            d.pop("classificationScheme", UNSET)
        )

        allow_userdefined_keywords = d.pop("allowUserdefinedKeywords", UNSET)

        limit_to_leaf_selection = d.pop("limitToLeafSelection", UNSET)

        logical_name = d.pop("logicalName", UNSET)

        def _parse_relation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation_type = _parse_relation_type(d.pop("relationType", UNSET))

        allowed_keyword_group_configuration = cls(
            target_system_name=target_system_name,
            pure_id=pure_id,
            keyword_group_type=keyword_group_type,
            name=name,
            description=description,
            classification_scheme=classification_scheme,
            allow_userdefined_keywords=allow_userdefined_keywords,
            limit_to_leaf_selection=limit_to_leaf_selection,
            logical_name=logical_name,
            relation_type=relation_type,
        )

        allowed_keyword_group_configuration.additional_properties = d
        return allowed_keyword_group_configuration

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
