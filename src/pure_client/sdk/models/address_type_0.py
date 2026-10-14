from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="AddressType0")


@_attrs_define
class AddressType0:
    """A physical address

    Attributes:
        road (None | str | Unset): Name of road and house number, eg. 'Pennsylvania Avenue' or '123 Main St.'
        room (None | str | Unset): Room number or name if available, eg. '1.23' or 'Office of Creative Services'
        building (None | str | Unset): Building Name if available, eg. 'Couper Administration Building'
        postal_code (None | str | Unset): Postal code
        city (None | str | Unset): City or town, eg. 'Binghamton'
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    road: None | str | Unset = UNSET
    room: None | str | Unset = UNSET
    building: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        road: None | str | Unset
        if isinstance(self.road, Unset):
            road = UNSET
        else:
            road = self.road

        room: None | str | Unset
        if isinstance(self.room, Unset):
            room = UNSET
        else:
            room = self.room

        building: None | str | Unset
        if isinstance(self.building, Unset):
            building = UNSET
        else:
            building = self.building

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if road is not UNSET:
            field_dict["road"] = road
        if room is not UNSET:
            field_dict["room"] = room
        if building is not UNSET:
            field_dict["building"] = building
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)

        def _parse_road(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        road = _parse_road(d.pop("road", UNSET))

        def _parse_room(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room = _parse_room(d.pop("room", UNSET))

        def _parse_building(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building = _parse_building(d.pop("building", UNSET))

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

        address_type_0 = cls(
            road=road,
            room=room,
            building=building,
            postal_code=postal_code,
            city=city,
            country=country,
        )

        address_type_0.additional_properties = d
        return address_type_0

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
