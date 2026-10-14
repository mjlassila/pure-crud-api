from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="DataSetGeoLocation")


@_attrs_define
class DataSetGeoLocation:
    """A data set geo-location.

    Attributes:
        point (None | str | Unset): Location expressed as a point
        polygon (None | str | Unset): Location expressed as a polygon
        calculated_point (str | Unset): Used to determine whether or not we may update the point. An end-user has not
            entered a point manually if the value of the calculated point is the same as point
        geographical_coverage (LocalizedStringType0 | None | Unset): A set of string values, one for each submission
            locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
    """

    point: None | str | Unset = UNSET
    polygon: None | str | Unset = UNSET
    calculated_point: str | Unset = UNSET
    geographical_coverage: LocalizedStringType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_string_type_0 import LocalizedStringType0

        point: None | str | Unset
        if isinstance(self.point, Unset):
            point = UNSET
        else:
            point = self.point

        polygon: None | str | Unset
        if isinstance(self.polygon, Unset):
            polygon = UNSET
        else:
            polygon = self.polygon

        calculated_point = self.calculated_point

        geographical_coverage: dict[str, Any] | None | Unset
        if isinstance(self.geographical_coverage, Unset):
            geographical_coverage = UNSET
        elif isinstance(self.geographical_coverage, LocalizedStringType0):
            geographical_coverage = self.geographical_coverage.to_dict()
        else:
            geographical_coverage = self.geographical_coverage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if point is not UNSET:
            field_dict["point"] = point
        if polygon is not UNSET:
            field_dict["polygon"] = polygon
        if calculated_point is not UNSET:
            field_dict["calculatedPoint"] = calculated_point
        if geographical_coverage is not UNSET:
            field_dict["geographicalCoverage"] = geographical_coverage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)

        def _parse_point(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        point = _parse_point(d.pop("point", UNSET))

        def _parse_polygon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polygon = _parse_polygon(d.pop("polygon", UNSET))

        calculated_point = d.pop("calculatedPoint", UNSET)

        def _parse_geographical_coverage(
            data: object,
        ) -> LocalizedStringType0 | None | Unset:
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

        geographical_coverage = _parse_geographical_coverage(
            d.pop("geographicalCoverage", UNSET)
        )

        data_set_geo_location = cls(
            point=point,
            polygon=polygon,
            calculated_point=calculated_point,
            geographical_coverage=geographical_coverage,
        )

        data_set_geo_location.additional_properties = d
        return data_set_geo_location

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
