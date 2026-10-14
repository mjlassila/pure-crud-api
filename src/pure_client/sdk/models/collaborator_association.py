from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="CollaboratorAssociation")


@_attrs_define
class CollaboratorAssociation:
    """A collaborator associated with the content.

    Attributes:
        type_discriminator (str):
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        type_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        lead_collaborator (bool | None | Unset): Whether this collaborator is lead collaborator or not.
    """

    type_discriminator: str
    pure_id: int | Unset = UNSET
    type_: ClassificationRefType0 | None | Unset = UNSET
    lead_collaborator: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        type_discriminator = self.type_discriminator

        pure_id = self.pure_id

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        lead_collaborator: bool | None | Unset
        if isinstance(self.lead_collaborator, Unset):
            lead_collaborator = UNSET
        else:
            lead_collaborator = self.lead_collaborator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if lead_collaborator is not UNSET:
            field_dict["leadCollaborator"] = lead_collaborator

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        pure_id = d.pop("pureId", UNSET)

        def _parse_type_(data: object) -> ClassificationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_classification_ref_type_0 = (
                    ClassificationRefType0.from_dict(data)
                )

                return componentsschemas_classification_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClassificationRefType0 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_lead_collaborator(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        lead_collaborator = _parse_lead_collaborator(d.pop("leadCollaborator", UNSET))

        collaborator_association = cls(
            type_discriminator=type_discriminator,
            pure_id=pure_id,
            type_=type_,
            lead_collaborator=lead_collaborator,
        )

        collaborator_association.additional_properties = d
        return collaborator_association

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
