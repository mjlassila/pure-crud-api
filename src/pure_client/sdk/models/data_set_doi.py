from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.date_range import DateRange


T = TypeVar("T", bound="DataSetDoi")


@_attrs_define
class DataSetDoi:
    """A DOI.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        doi (None | str | Unset): DOI.
        access_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        embargo_period (DateRange | Unset): A date range
        license_type (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    pure_id: int | Unset = UNSET
    doi: None | str | Unset = UNSET
    access_type: ClassificationRefType0 | None | Unset = UNSET
    embargo_period: DateRange | Unset = UNSET
    license_type: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        pure_id = self.pure_id

        doi: None | str | Unset
        if isinstance(self.doi, Unset):
            doi = UNSET
        else:
            doi = self.doi

        access_type: dict[str, Any] | None | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        elif isinstance(self.access_type, ClassificationRefType0):
            access_type = self.access_type.to_dict()
        else:
            access_type = self.access_type

        embargo_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embargo_period, Unset):
            embargo_period = self.embargo_period.to_dict()

        license_type: dict[str, Any] | None | Unset
        if isinstance(self.license_type, Unset):
            license_type = UNSET
        elif isinstance(self.license_type, ClassificationRefType0):
            license_type = self.license_type.to_dict()
        else:
            license_type = self.license_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if doi is not UNSET:
            field_dict["doi"] = doi
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if embargo_period is not UNSET:
            field_dict["embargoPeriod"] = embargo_period
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        def _parse_doi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        doi = _parse_doi(d.pop("doi", UNSET))

        def _parse_access_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        access_type = _parse_access_type(d.pop("accessType", UNSET))

        _embargo_period = d.pop("embargoPeriod", UNSET)
        embargo_period: DateRange | Unset
        if isinstance(_embargo_period, Unset):
            embargo_period = UNSET
        else:
            embargo_period = DateRange.from_dict(_embargo_period)

        def _parse_license_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        license_type = _parse_license_type(d.pop("licenseType", UNSET))

        data_set_doi = cls(
            pure_id=pure_id,
            doi=doi,
            access_type=access_type,
            embargo_period=embargo_period,
            license_type=license_type,
        )

        data_set_doi.additional_properties = d
        return data_set_doi

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
