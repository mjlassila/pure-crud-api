from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.formatted_string import FormattedString


T = TypeVar("T", bound="PublicationSeries")


@_attrs_define
class PublicationSeries:
    """A publication series.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        name (FormattedString | Unset): A string containing HTML formatted text
        publisher_name (None | str | Unset): The publisher of the publication series.
        print_issn (None | str | Unset): The print ISSN of the publication series.
        electronic_issn (None | str | Unset): The electronic ISSN of the publication series.
        no (None | str | Unset): The number of the publication series.
        volume (None | str | Unset): The volume of the publication series.
    """

    pure_id: int | Unset = UNSET
    name: FormattedString | Unset = UNSET
    publisher_name: None | str | Unset = UNSET
    print_issn: None | str | Unset = UNSET
    electronic_issn: None | str | Unset = UNSET
    no: None | str | Unset = UNSET
    volume: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pure_id = self.pure_id

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        publisher_name: None | str | Unset
        if isinstance(self.publisher_name, Unset):
            publisher_name = UNSET
        else:
            publisher_name = self.publisher_name

        print_issn: None | str | Unset
        if isinstance(self.print_issn, Unset):
            print_issn = UNSET
        else:
            print_issn = self.print_issn

        electronic_issn: None | str | Unset
        if isinstance(self.electronic_issn, Unset):
            electronic_issn = UNSET
        else:
            electronic_issn = self.electronic_issn

        no: None | str | Unset
        if isinstance(self.no, Unset):
            no = UNSET
        else:
            no = self.no

        volume: None | str | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if name is not UNSET:
            field_dict["name"] = name
        if publisher_name is not UNSET:
            field_dict["publisherName"] = publisher_name
        if print_issn is not UNSET:
            field_dict["printIssn"] = print_issn
        if electronic_issn is not UNSET:
            field_dict["electronicIssn"] = electronic_issn
        if no is not UNSET:
            field_dict["no"] = no
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.formatted_string import FormattedString

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        _name = d.pop("name", UNSET)
        name: FormattedString | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = FormattedString.from_dict(_name)

        def _parse_publisher_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher_name = _parse_publisher_name(d.pop("publisherName", UNSET))

        def _parse_print_issn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        print_issn = _parse_print_issn(d.pop("printIssn", UNSET))

        def _parse_electronic_issn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        electronic_issn = _parse_electronic_issn(d.pop("electronicIssn", UNSET))

        def _parse_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no = _parse_no(d.pop("no", UNSET))

        def _parse_volume(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        publication_series = cls(
            pure_id=pure_id,
            name=name,
            publisher_name=publisher_name,
            print_issn=print_issn,
            electronic_issn=electronic_issn,
            no=no,
            volume=volume,
        )

        publication_series.additional_properties = d
        return publication_series

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
