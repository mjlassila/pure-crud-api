from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="ClassificationRefList")


@_attrs_define
class ClassificationRefList:
    """List of classification references

    Attributes:
        classifications (list[ClassificationRefType0 | None] | Unset):
    """

    classifications: list[ClassificationRefType0 | None] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        classifications: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.classifications, Unset):
            classifications = []
            for classifications_item_data in self.classifications:
                classifications_item: dict[str, Any] | None
                if isinstance(classifications_item_data, ClassificationRefType0):
                    classifications_item = classifications_item_data.to_dict()
                else:
                    classifications_item = classifications_item_data
                classifications.append(classifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classifications is not UNSET:
            field_dict["classifications"] = classifications

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)
        _classifications = d.pop("classifications", UNSET)
        classifications: list[ClassificationRefType0 | None] | Unset = UNSET
        if _classifications is not UNSET:
            classifications = []
            for classifications_item_data in _classifications:

                def _parse_classifications_item(
                    data: object,
                ) -> ClassificationRefType0 | None:
                    if data is None:
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
                    return cast(ClassificationRefType0 | None, data)

                classifications_item = _parse_classifications_item(
                    classifications_item_data
                )

                classifications.append(classifications_item)

        classification_ref_list = cls(
            classifications=classifications,
        )

        classification_ref_list.additional_properties = d
        return classification_ref_list

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
