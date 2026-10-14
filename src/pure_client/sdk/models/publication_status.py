from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.compound_date_type_0 import CompoundDateType0


T = TypeVar("T", bound="PublicationStatus")


@_attrs_define
class PublicationStatus:
    """A representation of a point in time when the status of a publication changed, e.g. the submission date or
    publication date of the publication.

        Attributes:
            pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
            current (bool | Unset): True when this status element is the current, false otherwise.
            publication_status (ClassificationRefType0 | None | Unset): A reference to a classification value
            publication_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and month or
                a full date
    """

    pure_id: int | Unset = UNSET
    current: bool | Unset = UNSET
    publication_status: ClassificationRefType0 | None | Unset = UNSET
    publication_date: CompoundDateType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0

        pure_id = self.pure_id

        current = self.current

        publication_status: dict[str, Any] | None | Unset
        if isinstance(self.publication_status, Unset):
            publication_status = UNSET
        elif isinstance(self.publication_status, ClassificationRefType0):
            publication_status = self.publication_status.to_dict()
        else:
            publication_status = self.publication_status

        publication_date: dict[str, Any] | None | Unset
        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        elif isinstance(self.publication_date, CompoundDateType0):
            publication_date = self.publication_date.to_dict()
        else:
            publication_date = self.publication_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if current is not UNSET:
            field_dict["current"] = current
        if publication_status is not UNSET:
            field_dict["publicationStatus"] = publication_status
        if publication_date is not UNSET:
            field_dict["publicationDate"] = publication_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_type_0 import CompoundDateType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        current = d.pop("current", UNSET)

        def _parse_publication_status(
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

        publication_status = _parse_publication_status(
            d.pop("publicationStatus", UNSET)
        )

        def _parse_publication_date(data: object) -> CompoundDateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compound_date_type_0 = CompoundDateType0.from_dict(
                    data
                )

                return componentsschemas_compound_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompoundDateType0 | None | Unset, data)

        publication_date = _parse_publication_date(d.pop("publicationDate", UNSET))

        publication_status = cls(
            pure_id=pure_id,
            current=current,
            publication_status=publication_status,
            publication_date=publication_date,
        )

        publication_status.additional_properties = d
        return publication_status

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
