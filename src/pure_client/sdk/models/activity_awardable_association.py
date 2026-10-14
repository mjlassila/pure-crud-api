from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_ref_type_0 import ActivityRefType0
    from ..models.award_ref_type_0 import AwardRefType0


T = TypeVar("T", bound="ActivityAwardableAssociation")


@_attrs_define
class ActivityAwardableAssociation:
    """A relation to an activity, optionally in the context of the Award that made it possible.

    Attributes:
        activity (ActivityRefType0 | None): A reference to an activity
        award (AwardRefType0 | None | Unset): A reference to an award
    """

    activity: ActivityRefType0 | None
    award: AwardRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.award_ref_type_0 import AwardRefType0

        activity: dict[str, Any] | None
        if isinstance(self.activity, ActivityRefType0):
            activity = self.activity.to_dict()
        else:
            activity = self.activity

        award: dict[str, Any] | None | Unset
        if isinstance(self.award, Unset):
            award = UNSET
        elif isinstance(self.award, AwardRefType0):
            award = self.award.to_dict()
        else:
            award = self.award

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity": activity,
            }
        )
        if award is not UNSET:
            field_dict["award"] = award

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.award_ref_type_0 import AwardRefType0

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

        def _parse_award(data: object) -> AwardRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_award_ref_type_0 = AwardRefType0.from_dict(data)

                return componentsschemas_award_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwardRefType0 | None | Unset, data)

        award = _parse_award(d.pop("award", UNSET))

        activity_awardable_association = cls(
            activity=activity,
            award=award,
        )

        activity_awardable_association.additional_properties = d
        return activity_awardable_association

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
