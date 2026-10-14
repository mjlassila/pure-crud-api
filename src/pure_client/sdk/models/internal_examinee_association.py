from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="InternalExamineeAssociation")


@_attrs_define
class InternalExamineeAssociation:
    """An internal examinee association.

    Attributes:
        type_discriminator (str):
        person (None | PersonRefType0): A reference to a person internal to the institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
    """

    type_discriminator: str
    person: None | PersonRefType0
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.person_ref_type_0 import PersonRefType0

        type_discriminator = self.type_discriminator

        person: dict[str, Any] | None
        if isinstance(self.person, PersonRefType0):
            person = self.person.to_dict()
        else:
            person = self.person

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "person": person,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

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

        pure_id = d.pop("pureId", UNSET)

        internal_examinee_association = cls(
            type_discriminator=type_discriminator,
            person=person,
            pure_id=pure_id,
        )

        internal_examinee_association.additional_properties = d
        return internal_examinee_association

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
