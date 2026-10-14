from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="DataSetPhysicalData")


@_attrs_define
class DataSetPhysicalData:
    """A description of physical data.

    Attributes:
        title (str): Title.
        storage_location (str): Storage location.
        media (str): Media.
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        access_description (None | str | Unset): Access description.
        type_ (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    title: str
    storage_location: str
    media: str
    pure_id: int | Unset = UNSET
    access_description: None | str | Unset = UNSET
    type_: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        title = self.title

        storage_location = self.storage_location

        media = self.media

        pure_id = self.pure_id

        access_description: None | str | Unset
        if isinstance(self.access_description, Unset):
            access_description = UNSET
        else:
            access_description = self.access_description

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "storageLocation": storage_location,
                "media": media,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if access_description is not UNSET:
            field_dict["accessDescription"] = access_description
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)
        title = d.pop("title")

        storage_location = d.pop("storageLocation")

        media = d.pop("media")

        pure_id = d.pop("pureId", UNSET)

        def _parse_access_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_description = _parse_access_description(
            d.pop("accessDescription", UNSET)
        )

        def _parse_type_(data: object) -> ClassificationRefType0 | None | Unset:
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

        type_ = _parse_type_(d.pop("type", UNSET))

        data_set_physical_data = cls(
            title=title,
            storage_location=storage_location,
            media=media,
            pure_id=pure_id,
            access_description=access_description,
            type_=type_,
        )

        data_set_physical_data.additional_properties = d
        return data_set_physical_data

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
