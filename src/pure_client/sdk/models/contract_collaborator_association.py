from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.external_person_ref_type_0 import ExternalPersonRefType0


T = TypeVar("T", bound="ContractCollaboratorAssociation")


@_attrs_define
class ContractCollaboratorAssociation:
    """A association between a contract and a collaborator

    Attributes:
        external_organization (ExternalOrganizationRefType0 | None): A reference to an organization external to the
            institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        type_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        contact_persons (list[ExternalPersonRefType0 | None] | Unset): A collection of contact persons
        lead_collaborator (bool | Unset):
    """

    external_organization: ExternalOrganizationRefType0 | None
    pure_id: int | Unset = UNSET
    type_: ClassificationRefType0 | None | Unset = UNSET
    contact_persons: list[ExternalPersonRefType0 | None] | Unset = UNSET
    lead_collaborator: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0

        external_organization: dict[str, Any] | None
        if isinstance(self.external_organization, ExternalOrganizationRefType0):
            external_organization = self.external_organization.to_dict()
        else:
            external_organization = self.external_organization

        pure_id = self.pure_id

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        contact_persons: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.contact_persons, Unset):
            contact_persons = []
            for contact_persons_item_data in self.contact_persons:
                contact_persons_item: dict[str, Any] | None
                if isinstance(contact_persons_item_data, ExternalPersonRefType0):
                    contact_persons_item = contact_persons_item_data.to_dict()
                else:
                    contact_persons_item = contact_persons_item_data
                contact_persons.append(contact_persons_item)

        lead_collaborator = self.lead_collaborator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalOrganization": external_organization,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if contact_persons is not UNSET:
            field_dict["contactPersons"] = contact_persons
        if lead_collaborator is not UNSET:
            field_dict["leadCollaborator"] = lead_collaborator

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0

        d = dict(src_dict)

        def _parse_external_organization(
            data: object,
        ) -> ExternalOrganizationRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_external_organization_ref_type_0 = (
                    ExternalOrganizationRefType0.from_dict(data)
                )

                return componentsschemas_external_organization_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalOrganizationRefType0 | None, data)

        external_organization = _parse_external_organization(
            d.pop("externalOrganization")
        )

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

        _contact_persons = d.pop("contactPersons", UNSET)
        contact_persons: list[ExternalPersonRefType0 | None] | Unset = UNSET
        if _contact_persons is not UNSET:
            contact_persons = []
            for contact_persons_item_data in _contact_persons:

                def _parse_contact_persons_item(
                    data: object,
                ) -> ExternalPersonRefType0 | None:
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

                contact_persons_item = _parse_contact_persons_item(
                    contact_persons_item_data
                )

                contact_persons.append(contact_persons_item)

        lead_collaborator = d.pop("leadCollaborator", UNSET)

        contract_collaborator_association = cls(
            external_organization=external_organization,
            pure_id=pure_id,
            type_=type_,
            contact_persons=contact_persons,
            lead_collaborator=lead_collaborator,
        )

        contract_collaborator_association.additional_properties = d
        return contract_collaborator_association

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
