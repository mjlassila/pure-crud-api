from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompoundDateType0")


@_attrs_define
class CompoundDateType0:
    """A date that can be defined by only year, year and month or a full date

    Attributes:
        year (int):
        month (int | None | Unset):
        day (int | None | Unset):
    """

    year: int
    month: int | None | Unset = UNSET
    day: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        month: int | None | Unset
        if isinstance(self.month, Unset):
            month = UNSET
        else:
            month = self.month

        day: int | None | Unset
        if isinstance(self.day, Unset):
            day = UNSET
        else:
            day = self.day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
            }
        )
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        year = d.pop("year")

        def _parse_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        month = _parse_month(d.pop("month", UNSET))

        def _parse_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day = _parse_day(d.pop("day", UNSET))

        compound_date_type_0 = cls(
            year=year,
            month=month,
            day=day,
        )

        compound_date_type_0.additional_properties = d
        return compound_date_type_0

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
