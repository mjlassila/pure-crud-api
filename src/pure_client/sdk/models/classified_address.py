from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.geo_location_type_0 import GeoLocationType0


T = TypeVar("T", bound="ClassifiedAddress")


@_attrs_define
class ClassifiedAddress:
    """A physical address

    Attributes:
        address_type (ClassificationRefType0 | None): A reference to a classification value
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        address_lines (None | str | Unset): Address for personal residence
        street (None | str | Unset): The name of the street
        building (None | str | Unset): The name of the building
        postalcode (None | str | Unset): The postal code of the city
        city (None | str | Unset): The name of the city
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
        subdivision (ClassificationRefType0 | None | Unset): A reference to a classification value
        geo_location (GeoLocationType0 | None | Unset): Geographical location
    """

    address_type: ClassificationRefType0 | None
    pure_id: int | Unset = UNSET
    address_lines: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    building: None | str | Unset = UNSET
    postalcode: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    subdivision: ClassificationRefType0 | None | Unset = UNSET
    geo_location: GeoLocationType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.geo_location_type_0 import GeoLocationType0

        address_type: dict[str, Any] | None
        if isinstance(self.address_type, ClassificationRefType0):
            address_type = self.address_type.to_dict()
        else:
            address_type = self.address_type

        pure_id = self.pure_id

        address_lines: None | str | Unset
        if isinstance(self.address_lines, Unset):
            address_lines = UNSET
        else:
            address_lines = self.address_lines

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        building: None | str | Unset
        if isinstance(self.building, Unset):
            building = UNSET
        else:
            building = self.building

        postalcode: None | str | Unset
        if isinstance(self.postalcode, Unset):
            postalcode = UNSET
        else:
            postalcode = self.postalcode

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, ClassificationRefType0):
            country = self.country.to_dict()
        else:
            country = self.country

        subdivision: dict[str, Any] | None | Unset
        if isinstance(self.subdivision, Unset):
            subdivision = UNSET
        elif isinstance(self.subdivision, ClassificationRefType0):
            subdivision = self.subdivision.to_dict()
        else:
            subdivision = self.subdivision

        geo_location: dict[str, Any] | None | Unset
        if isinstance(self.geo_location, Unset):
            geo_location = UNSET
        elif isinstance(self.geo_location, GeoLocationType0):
            geo_location = self.geo_location.to_dict()
        else:
            geo_location = self.geo_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addressType": address_type,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if address_lines is not UNSET:
            field_dict["addressLines"] = address_lines
        if street is not UNSET:
            field_dict["street"] = street
        if building is not UNSET:
            field_dict["building"] = building
        if postalcode is not UNSET:
            field_dict["postalcode"] = postalcode
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if subdivision is not UNSET:
            field_dict["subdivision"] = subdivision
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.geo_location_type_0 import GeoLocationType0

        d = dict(src_dict)

        def _parse_address_type(data: object) -> ClassificationRefType0 | None:
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

        address_type = _parse_address_type(d.pop("addressType"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_address_lines(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_lines = _parse_address_lines(d.pop("addressLines", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_building(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building = _parse_building(d.pop("building", UNSET))

        def _parse_postalcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postalcode = _parse_postalcode(d.pop("postalcode", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> ClassificationRefType0 | None | Unset:
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

        country = _parse_country(d.pop("country", UNSET))

        def _parse_subdivision(data: object) -> ClassificationRefType0 | None | Unset:
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

        subdivision = _parse_subdivision(d.pop("subdivision", UNSET))

        def _parse_geo_location(data: object) -> GeoLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_geo_location_type_0 = GeoLocationType0.from_dict(data)

                return componentsschemas_geo_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GeoLocationType0 | None | Unset, data)

        geo_location = _parse_geo_location(d.pop("geoLocation", UNSET))

        classified_address = cls(
            address_type=address_type,
            pure_id=pure_id,
            address_lines=address_lines,
            street=street,
            building=building,
            postalcode=postalcode,
            city=city,
            country=country,
            subdivision=subdivision,
            geo_location=geo_location,
        )

        classified_address.additional_properties = d
        return classified_address

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
