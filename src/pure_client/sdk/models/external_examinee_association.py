from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_person_ref_type_0 import ExternalPersonRefType0


T = TypeVar("T", bound="ExternalExamineeAssociation")


@_attrs_define
class ExternalExamineeAssociation:
    """An external examinee association.

    Attributes:
        type_discriminator (str):
        external_person (ExternalPersonRefType0 | None): A reference to a person external to the institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
    """

    type_discriminator: str
    external_person: ExternalPersonRefType0 | None
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0

        type_discriminator = self.type_discriminator

        external_person: dict[str, Any] | None
        if isinstance(self.external_person, ExternalPersonRefType0):
            external_person = self.external_person.to_dict()
        else:
            external_person = self.external_person

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "externalPerson": external_person,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_external_person(data: object) -> ExternalPersonRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_external_person_ref_type_0 = (
                    ExternalPersonRefType0.from_dict(data)
                )

                return componentsschemas_external_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalPersonRefType0 | None, data)

        external_person = _parse_external_person(d.pop("externalPerson"))

        pure_id = d.pop("pureId", UNSET)

        external_examinee_association = cls(
            type_discriminator=type_discriminator,
            external_person=external_person,
            pure_id=pure_id,
        )

        external_examinee_association.additional_properties = d
        return external_examinee_association

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
