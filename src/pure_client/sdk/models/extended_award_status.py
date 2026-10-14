from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendedAwardStatus")


@_attrs_define
class ExtendedAwardStatus:
    """Indicates that an award is extended.

    Attributes:
        type_discriminator (str):
        extended_end_date (datetime.date): The date the award is extended to
        date_of_extension (datetime.date | None | Unset): The date the award was extended
    """

    type_discriminator: str
    extended_end_date: datetime.date
    date_of_extension: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_discriminator = self.type_discriminator

        extended_end_date = self.extended_end_date.isoformat()

        date_of_extension: None | str | Unset
        if isinstance(self.date_of_extension, Unset):
            date_of_extension = UNSET
        elif isinstance(self.date_of_extension, datetime.date):
            date_of_extension = self.date_of_extension.isoformat()
        else:
            date_of_extension = self.date_of_extension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "extendedEndDate": extended_end_date,
            }
        )
        if date_of_extension is not UNSET:
            field_dict["dateOfExtension"] = date_of_extension

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        extended_end_date = isoparse(d.pop("extendedEndDate")).date()

        def _parse_date_of_extension(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_extension_type_0 = isoparse(data).date()

                return date_of_extension_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_extension = _parse_date_of_extension(d.pop("dateOfExtension", UNSET))

        extended_award_status = cls(
            type_discriminator=type_discriminator,
            extended_end_date=extended_end_date,
            date_of_extension=date_of_extension,
        )

        extended_award_status.additional_properties = d
        return extended_award_status

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
