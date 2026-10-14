from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compound_date_type_0 import CompoundDateType0


T = TypeVar("T", bound="CompoundDateRange")


@_attrs_define
class CompoundDateRange:
    """A date range of that can be defined by only year, year and month or a full date

    Attributes:
        start_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and month or a full
            date
        end_date (CompoundDateType0 | None | Unset): A date that can be defined by only year, year and month or a full
            date
    """

    start_date: CompoundDateType0 | None | Unset = UNSET
    end_date: CompoundDateType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.compound_date_type_0 import CompoundDateType0

        start_date: dict[str, Any] | None | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, CompoundDateType0):
            start_date = self.start_date.to_dict()
        else:
            start_date = self.start_date

        end_date: dict[str, Any] | None | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, CompoundDateType0):
            end_date = self.end_date.to_dict()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compound_date_type_0 import CompoundDateType0

        d = dict(src_dict)

        def _parse_start_date(data: object) -> CompoundDateType0 | None | Unset:
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

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> CompoundDateType0 | None | Unset:
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

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        compound_date_range = cls(
            start_date=start_date,
            end_date=end_date,
        )

        compound_date_range.additional_properties = d
        return compound_date_range

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
