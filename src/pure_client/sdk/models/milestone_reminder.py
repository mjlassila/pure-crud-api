from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.milestone_reminder_time_unit import MilestoneReminderTimeUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="MilestoneReminder")


@_attrs_define
class MilestoneReminder:
    """A milestone reminder.

    Attributes:
        value (int): Number of units in reminder period.
        time_unit (MilestoneReminderTimeUnit): The time unit of the reminder.
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
    """

    value: int
    time_unit: MilestoneReminderTimeUnit
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        time_unit = self.time_unit.value

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "timeUnit": time_unit,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value")

        time_unit = MilestoneReminderTimeUnit(d.pop("timeUnit"))

        pure_id = d.pop("pureId", UNSET)

        milestone_reminder = cls(
            value=value,
            time_unit=time_unit,
            pure_id=pure_id,
        )

        milestone_reminder.additional_properties = d
        return milestone_reminder

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
