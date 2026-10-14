from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.geo_location_type_0 import GeoLocationType0


T = TypeVar("T", bound="CERIFAddressType0")


@_attrs_define
class CERIFAddressType0:
    """A physical address

    Attributes:
        address1 (None | str | Unset): Address line 1
        address2 (None | str | Unset): Address line 2
        address3 (None | str | Unset): Address line 3
        address4 (None | str | Unset): Address line 4
        address5 (None | str | Unset): Address line 5
        postal_code (None | str | Unset): Postal code of city
        city (None | str | Unset): City
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
        subdivision (ClassificationRefType0 | None | Unset): A reference to a classification value
        state (None | str | Unset): State. Mutually exclusive with state
        geo_location (GeoLocationType0 | None | Unset): Geographical location
    """

    address1: None | str | Unset = UNSET
    address2: None | str | Unset = UNSET
    address3: None | str | Unset = UNSET
    address4: None | str | Unset = UNSET
    address5: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    subdivision: ClassificationRefType0 | None | Unset = UNSET
    state: None | str | Unset = UNSET
    geo_location: GeoLocationType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.geo_location_type_0 import GeoLocationType0

        address1: None | str | Unset
        if isinstance(self.address1, Unset):
            address1 = UNSET
        else:
            address1 = self.address1

        address2: None | str | Unset
        if isinstance(self.address2, Unset):
            address2 = UNSET
        else:
            address2 = self.address2

        address3: None | str | Unset
        if isinstance(self.address3, Unset):
            address3 = UNSET
        else:
            address3 = self.address3

        address4: None | str | Unset
        if isinstance(self.address4, Unset):
            address4 = UNSET
        else:
            address4 = self.address4

        address5: None | str | Unset
        if isinstance(self.address5, Unset):
            address5 = UNSET
        else:
            address5 = self.address5

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

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

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        geo_location: dict[str, Any] | None | Unset
        if isinstance(self.geo_location, Unset):
            geo_location = UNSET
        elif isinstance(self.geo_location, GeoLocationType0):
            geo_location = self.geo_location.to_dict()
        else:
            geo_location = self.geo_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if address3 is not UNSET:
            field_dict["address3"] = address3
        if address4 is not UNSET:
            field_dict["address4"] = address4
        if address5 is not UNSET:
            field_dict["address5"] = address5
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if subdivision is not UNSET:
            field_dict["subdivision"] = subdivision
        if state is not UNSET:
            field_dict["state"] = state
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.geo_location_type_0 import GeoLocationType0

        d = dict(src_dict)

        def _parse_address1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address1 = _parse_address1(d.pop("address1", UNSET))

        def _parse_address2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2 = _parse_address2(d.pop("address2", UNSET))

        def _parse_address3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address3 = _parse_address3(d.pop("address3", UNSET))

        def _parse_address4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address4 = _parse_address4(d.pop("address4", UNSET))

        def _parse_address5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address5 = _parse_address5(d.pop("address5", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postalCode", UNSET))

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

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

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

        cerif_address_type_0 = cls(
            address1=address1,
            address2=address2,
            address3=address3,
            address4=address4,
            address5=address5,
            postal_code=postal_code,
            city=city,
            country=country,
            subdivision=subdivision,
            state=state,
            geo_location=geo_location,
        )

        cerif_address_type_0.additional_properties = d
        return cerif_address_type_0

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
