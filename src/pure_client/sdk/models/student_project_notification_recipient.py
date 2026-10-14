from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StudentProjectNotificationRecipient")


@_attrs_define
class StudentProjectNotificationRecipient:
    """A number of email addresses that will be notified once this student project enters the validated workflow step

    Attributes:
        email_address (str): The email address for the notification recipient
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
    """

    email_address: str
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailAddress": email_address,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email_address = d.pop("emailAddress")

        pure_id = d.pop("pureId", UNSET)

        student_project_notification_recipient = cls(
            email_address=email_address,
            pure_id=pure_id,
        )

        student_project_notification_recipient.additional_properties = d
        return student_project_notification_recipient

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
