from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_ref_type_0 import AwardRefType0
    from ..models.participant_time_spent import ParticipantTimeSpent
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="ParticipantTimeTrackingAssociation")


@_attrs_define
class ParticipantTimeTrackingAssociation:
    """Project participant time-tracking association, which holds allocated and spent time.

    Attributes:
        award (AwardRefType0 | None): A reference to an award
        person (None | PersonRefType0): A reference to a person internal to the institution
        allocated_time (int | None | Unset): The allocated time for an award for the participant.
        total_time_spent (int | Unset): The total time spent for an award for the participant.
        time_spent (list[ParticipantTimeSpent] | Unset): The time spent for an award for the participant.
    """

    award: AwardRefType0 | None
    person: None | PersonRefType0
    allocated_time: int | None | Unset = UNSET
    total_time_spent: int | Unset = UNSET
    time_spent: list[ParticipantTimeSpent] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        award: dict[str, Any] | None
        if isinstance(self.award, AwardRefType0):
            award = self.award.to_dict()
        else:
            award = self.award

        person: dict[str, Any] | None
        if isinstance(self.person, PersonRefType0):
            person = self.person.to_dict()
        else:
            person = self.person

        allocated_time: int | None | Unset
        if isinstance(self.allocated_time, Unset):
            allocated_time = UNSET
        else:
            allocated_time = self.allocated_time

        total_time_spent = self.total_time_spent

        time_spent: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.time_spent, Unset):
            time_spent = []
            for time_spent_item_data in self.time_spent:
                time_spent_item = time_spent_item_data.to_dict()
                time_spent.append(time_spent_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "award": award,
                "person": person,
            }
        )
        if allocated_time is not UNSET:
            field_dict["allocatedTime"] = allocated_time
        if total_time_spent is not UNSET:
            field_dict["totalTimeSpent"] = total_time_spent
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.participant_time_spent import ParticipantTimeSpent
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)

        def _parse_award(data: object) -> AwardRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_award_ref_type_0 = AwardRefType0.from_dict(data)

                return componentsschemas_award_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwardRefType0 | None, data)

        award = _parse_award(d.pop("award"))

        def _parse_person(data: object) -> None | PersonRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_ref_type_0 = PersonRefType0.from_dict(data)

                return componentsschemas_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonRefType0, data)

        person = _parse_person(d.pop("person"))

        def _parse_allocated_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        allocated_time = _parse_allocated_time(d.pop("allocatedTime", UNSET))

        total_time_spent = d.pop("totalTimeSpent", UNSET)

        _time_spent = d.pop("timeSpent", UNSET)
        time_spent: list[ParticipantTimeSpent] | Unset = UNSET
        if _time_spent is not UNSET:
            time_spent = []
            for time_spent_item_data in _time_spent:
                time_spent_item = ParticipantTimeSpent.from_dict(time_spent_item_data)

                time_spent.append(time_spent_item)

        participant_time_tracking_association = cls(
            award=award,
            person=person,
            allocated_time=allocated_time,
            total_time_spent=total_time_spent,
            time_spent=time_spent,
        )

        participant_time_tracking_association.additional_properties = d
        return participant_time_tracking_association

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
