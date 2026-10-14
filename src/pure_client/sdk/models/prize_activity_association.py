from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.activity_ref_type_0 import ActivityRefType0


T = TypeVar("T", bound="PrizeActivityAssociation")


@_attrs_define
class PrizeActivityAssociation:
    """An association to an activity.

    Attributes:
        activity (ActivityRefType0 | None): A reference to an activity
    """

    activity: ActivityRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0

        activity: dict[str, Any] | None
        if isinstance(self.activity, ActivityRefType0):
            activity = self.activity.to_dict()
        else:
            activity = self.activity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity": activity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.activity_ref_type_0 import ActivityRefType0

        d = dict(src_dict)

        def _parse_activity(data: object) -> ActivityRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_activity_ref_type_0 = ActivityRefType0.from_dict(data)

                return componentsschemas_activity_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityRefType0 | None, data)

        activity = _parse_activity(d.pop("activity"))

        prize_activity_association = cls(
            activity=activity,
        )

        prize_activity_association.additional_properties = d
        return prize_activity_association

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
