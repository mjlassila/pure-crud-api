from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier import Identifier
    from ..models.user_ref_type_0 import UserRefType0


T = TypeVar("T", bound="FundingOpportunityContactPerson")


@_attrs_define
class FundingOpportunityContactPerson:
    """Funding Opportunity Contact Person

    Attributes:
        user (None | UserRefType0): A reference to an user
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
    """

    user: None | UserRefType0
    pure_id: int | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref_type_0 import UserRefType0

        user: dict[str, Any] | None
        if isinstance(self.user, UserRefType0):
            user = self.user.to_dict()
        else:
            user = self.user

        pure_id = self.pure_id

        identifiers: list[dict[str, Any]] | None | Unset
        if isinstance(self.identifiers, Unset):
            identifiers = UNSET
        elif isinstance(self.identifiers, list):
            identifiers = []
            for identifiers_type_0_item_data in self.identifiers:
                identifiers_type_0_item = identifiers_type_0_item_data.to_dict()
                identifiers.append(identifiers_type_0_item)

        else:
            identifiers = self.identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.identifier import Identifier
        from ..models.user_ref_type_0 import UserRefType0

        d = dict(src_dict)

        def _parse_user(data: object) -> None | UserRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                return componentsschemas_user_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserRefType0, data)

        user = _parse_user(d.pop("user"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_identifiers(data: object) -> list[Identifier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                identifiers_type_0 = []
                _identifiers_type_0 = data
                for identifiers_type_0_item_data in _identifiers_type_0:
                    identifiers_type_0_item = Identifier.from_dict(
                        identifiers_type_0_item_data
                    )

                    identifiers_type_0.append(identifiers_type_0_item)

                return identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Identifier] | None | Unset, data)

        identifiers = _parse_identifiers(d.pop("identifiers", UNSET))

        funding_opportunity_contact_person = cls(
            user=user,
            pure_id=pure_id,
            identifiers=identifiers,
        )

        funding_opportunity_contact_person.additional_properties = d
        return funding_opportunity_contact_person

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
