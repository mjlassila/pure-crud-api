from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FundingOpportunityContactEmail")


@_attrs_define
class FundingOpportunityContactEmail:
    """Funding Opportunity Contact Email

    Attributes:
        email (str): The email of the contact
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        description (str | Unset):
    """

    email: str
    pure_id: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        pure_id = self.pure_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        pure_id = d.pop("pureId", UNSET)

        description = d.pop("description", UNSET)

        funding_opportunity_contact_email = cls(
            email=email,
            pure_id=pure_id,
            description=description,
        )

        funding_opportunity_contact_email.additional_properties = d
        return funding_opportunity_contact_email

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
