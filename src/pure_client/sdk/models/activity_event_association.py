from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_ref_type_0 import EventRefType0


T = TypeVar("T", bound="ActivityEventAssociation")


@_attrs_define
class ActivityEventAssociation:
    """An association with an event.

    Attributes:
        type_discriminator (str):
        event (EventRefType0 | None): A reference to an event
    """

    type_discriminator: str
    event: EventRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_ref_type_0 import EventRefType0

        type_discriminator = self.type_discriminator

        event: dict[str, Any] | None
        if isinstance(self.event, EventRefType0):
            event = self.event.to_dict()
        else:
            event = self.event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "event": event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.event_ref_type_0 import EventRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_event(data: object) -> EventRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_event_ref_type_0 = EventRefType0.from_dict(data)

                return componentsschemas_event_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventRefType0 | None, data)

        event = _parse_event(d.pop("event"))

        activity_event_association = cls(
            type_discriminator=type_discriminator,
            event=event,
        )

        activity_event_association.additional_properties = d
        return activity_event_association

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
