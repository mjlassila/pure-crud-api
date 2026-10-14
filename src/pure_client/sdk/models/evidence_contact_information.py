from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvidenceContactInformation")


@_attrs_define
class EvidenceContactInformation:
    """EvidenceContactInformation

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        contact_name (str | Unset):
        contact_details (str | Unset):
        corroborate_text (str | Unset):
        consent_obtained (bool | Unset):
    """

    pure_id: int | Unset = UNSET
    contact_name: str | Unset = UNSET
    contact_details: str | Unset = UNSET
    corroborate_text: str | Unset = UNSET
    consent_obtained: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pure_id = self.pure_id

        contact_name = self.contact_name

        contact_details = self.contact_details

        corroborate_text = self.corroborate_text

        consent_obtained = self.consent_obtained

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_details is not UNSET:
            field_dict["contactDetails"] = contact_details
        if corroborate_text is not UNSET:
            field_dict["corroborateText"] = corroborate_text
        if consent_obtained is not UNSET:
            field_dict["consentObtained"] = consent_obtained

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        contact_name = d.pop("contactName", UNSET)

        contact_details = d.pop("contactDetails", UNSET)

        corroborate_text = d.pop("corroborateText", UNSET)

        consent_obtained = d.pop("consentObtained", UNSET)

        evidence_contact_information = cls(
            pure_id=pure_id,
            contact_name=contact_name,
            contact_details=contact_details,
            corroborate_text=corroborate_text,
            consent_obtained=consent_obtained,
        )

        evidence_contact_information.additional_properties = d
        return evidence_contact_information

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
