from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classification_scheme_ref_type_0 import ClassificationSchemeRefType0
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="ClassificationSchemeRelation")


@_attrs_define
class ClassificationSchemeRelation:
    """Association between classification schemes

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        classification (ClassificationRefType0 | None | Unset): A reference to a classification value
        title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        classification_scheme (ClassificationSchemeRefType0 | None | Unset): A reference to a classification scheme
    """

    pure_id: int | Unset = UNSET
    classification: ClassificationRefType0 | None | Unset = UNSET
    title: LocalizedStringType0 | None | Unset = UNSET
    classification_scheme: ClassificationSchemeRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classification_scheme_ref_type_0 import (
            ClassificationSchemeRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        pure_id = self.pure_id

        classification: dict[str, Any] | None | Unset
        if isinstance(self.classification, Unset):
            classification = UNSET
        elif isinstance(self.classification, ClassificationRefType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        classification_scheme: dict[str, Any] | None | Unset
        if isinstance(self.classification_scheme, Unset):
            classification_scheme = UNSET
        elif isinstance(self.classification_scheme, ClassificationSchemeRefType0):
            classification_scheme = self.classification_scheme.to_dict()
        else:
            classification_scheme = self.classification_scheme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if classification is not UNSET:
            field_dict["classification"] = classification
        if title is not UNSET:
            field_dict["title"] = title
        if classification_scheme is not UNSET:
            field_dict["classificationScheme"] = classification_scheme

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classification_scheme_ref_type_0 import (
            ClassificationSchemeRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_classification(
            data: object,
        ) -> ClassificationRefType0 | None | Unset:
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

        classification = _parse_classification(d.pop("classification", UNSET))

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

        classification_scheme_relation = cls(
            pure_id=pure_id,
            classification=classification,
            title=title,
            classification_scheme=classification_scheme,
        )

        classification_scheme_relation.additional_properties = d
        return classification_scheme_relation

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
