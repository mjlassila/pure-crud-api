from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ParticipantTimeSpent")


@_attrs_define
class ParticipantTimeSpent:
    """Used to track how much time was spend on a given date.

    Attributes:
        date (datetime.date): The date the time was spent.
        time_spent (int): The amount of time spent.
    """

    date: datetime.date
    time_spent: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        time_spent = self.time_spent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "timeSpent": time_spent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        time_spent = d.pop("timeSpent")

        participant_time_spent = cls(
            date=date,
            time_spent=time_spent,
        )

        participant_time_spent.additional_properties = d
        return participant_time_spent

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
