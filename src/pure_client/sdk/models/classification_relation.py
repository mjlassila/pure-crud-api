from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="ClassificationRelation")


@_attrs_define
class ClassificationRelation:
    """Relation between classifications

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        related_to (ClassificationRefType0 | None | Unset): A reference to a classification value
        relation_type (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    pure_id: int | Unset = UNSET
    related_to: ClassificationRefType0 | None | Unset = UNSET
    relation_type: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        pure_id = self.pure_id

        related_to: dict[str, Any] | None | Unset
        if isinstance(self.related_to, Unset):
            related_to = UNSET
        elif isinstance(self.related_to, ClassificationRefType0):
            related_to = self.related_to.to_dict()
        else:
            related_to = self.related_to

        relation_type: dict[str, Any] | None | Unset
        if isinstance(self.relation_type, Unset):
            relation_type = UNSET
        elif isinstance(self.relation_type, ClassificationRefType0):
            relation_type = self.relation_type.to_dict()
        else:
            relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_related_to(data: object) -> ClassificationRefType0 | None | Unset:
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

        related_to = _parse_related_to(d.pop("relatedTo", UNSET))

        def _parse_relation_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        relation_type = _parse_relation_type(d.pop("relationType", UNSET))

        classification_relation = cls(
            pure_id=pure_id,
            related_to=related_to,
            relation_type=relation_type,
        )

        classification_relation.additional_properties = d
        return classification_relation

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
