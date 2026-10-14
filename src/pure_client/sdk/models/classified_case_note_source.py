from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="ClassifiedCaseNoteSource")


@_attrs_define
class ClassifiedCaseNoteSource:
    """Identification value of the case note in the source system.

    Attributes:
        classification (ClassificationRefType0 | None): A reference to a classification value
        value (str): The identifier of the case note in the source system.
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
    """

    classification: ClassificationRefType0 | None
    value: str
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        classification: dict[str, Any] | None
        if isinstance(self.classification, ClassificationRefType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        value = self.value

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "classification": classification,
                "value": value,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)

        def _parse_classification(data: object) -> ClassificationRefType0 | None:
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

        classification = _parse_classification(d.pop("classification"))

        value = d.pop("value")

        pure_id = d.pop("pureId", UNSET)

        classified_case_note_source = cls(
            classification=classification,
            value=value,
            pure_id=pure_id,
        )

        classified_case_note_source.additional_properties = d
        return classified_case_note_source

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
