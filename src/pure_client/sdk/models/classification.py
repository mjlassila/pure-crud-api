from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_relation import ClassificationRelation
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.system_localized_string_type_0 import SystemLocalizedStringType0


T = TypeVar("T", bound="Classification")


@_attrs_define
class Classification:
    """A way to annotate another object with a type/role/etc.

    Attributes:
        uri (str): URI used to uniquely identify this object
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        term (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting. Invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        disabled (bool | Unset):
        description (None | SystemLocalizedStringType0 | Unset): A set of localized string values each for a specific UI
            locale. Example: {'en_GB': 'Some text'}.
        classification_relations (list[ClassificationRelation] | Unset):
    """

    uri: str
    pure_id: int | Unset = UNSET
    term: FormattedLocalizedStringType0 | None | Unset = UNSET
    disabled: bool | Unset = UNSET
    description: None | SystemLocalizedStringType0 | Unset = UNSET
    classification_relations: list[ClassificationRelation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        uri = self.uri

        pure_id = self.pure_id

        term: dict[str, Any] | None | Unset
        if isinstance(self.term, Unset):
            term = UNSET
        elif isinstance(self.term, FormattedLocalizedStringType0):
            term = self.term.to_dict()
        else:
            term = self.term

        disabled = self.disabled

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, SystemLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        classification_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.classification_relations, Unset):
            classification_relations = []
            for classification_relations_item_data in self.classification_relations:
                classification_relations_item = (
                    classification_relations_item_data.to_dict()
                )
                classification_relations.append(classification_relations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if term is not UNSET:
            field_dict["term"] = term
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if description is not UNSET:
            field_dict["description"] = description
        if classification_relations is not UNSET:
            field_dict["classificationRelations"] = classification_relations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_relation import ClassificationRelation
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.system_localized_string_type_0 import SystemLocalizedStringType0

        d = dict(src_dict)
        uri = d.pop("uri")

        pure_id = d.pop("pureId", UNSET)

        def _parse_term(data: object) -> FormattedLocalizedStringType0 | None | Unset:
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

        term = _parse_term(d.pop("term", UNSET))

        disabled = d.pop("disabled", UNSET)

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

        _classification_relations = d.pop("classificationRelations", UNSET)
        classification_relations: list[ClassificationRelation] | Unset = UNSET
        if _classification_relations is not UNSET:
            classification_relations = []
            for classification_relations_item_data in _classification_relations:
                classification_relations_item = ClassificationRelation.from_dict(
                    classification_relations_item_data
                )

                classification_relations.append(classification_relations_item)

        classification = cls(
            uri=uri,
            pure_id=pure_id,
            term=term,
            disabled=disabled,
            description=description,
            classification_relations=classification_relations,
        )

        classification.additional_properties = d
        return classification

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
