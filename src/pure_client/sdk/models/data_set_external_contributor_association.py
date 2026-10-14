from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.date_range import DateRange
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.external_person_ref_type_0 import ExternalPersonRefType0
    from ..models.name import Name


T = TypeVar("T", bound="DataSetExternalContributorAssociation")


@_attrs_define
class DataSetExternalContributorAssociation:
    """An external contributor associated with the content.

    Attributes:
        type_discriminator (str):
        role (ClassificationRefType0 | None): A reference to a classification value
        external_person (ExternalPersonRefType0 | None): A reference to a person external to the institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        name (Name | Unset): A name describing a person, made up of given- and family name
        period (DateRange | Unset): A date range
        hidden (bool | Unset): If this contribution should be hidden, this is set to true, false otherwise. This is used
            for dataset that have author collaborations. If they do, we hide the individual contributors.
        association_hidden (bool | Unset): True if the content should be hidden from the person's portal profile, false
            otherwise.
    """

    type_discriminator: str
    role: ClassificationRefType0 | None
    external_person: ExternalPersonRefType0 | None
    pure_id: int | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    name: Name | Unset = UNSET
    period: DateRange | Unset = UNSET
    hidden: bool | Unset = UNSET
    association_hidden: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0

        type_discriminator = self.type_discriminator

        role: dict[str, Any] | None
        if isinstance(self.role, ClassificationRefType0):
            role = self.role.to_dict()
        else:
            role = self.role

        external_person: dict[str, Any] | None
        if isinstance(self.external_person, ExternalPersonRefType0):
            external_person = self.external_person.to_dict()
        else:
            external_person = self.external_person

        pure_id = self.pure_id

        external_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.external_organizations, Unset):
            external_organizations = UNSET
        elif isinstance(self.external_organizations, list):
            external_organizations = []
            for external_organizations_type_0_item_data in self.external_organizations:
                external_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    external_organizations_type_0_item_data,
                    ExternalOrganizationRefType0,
                ):
                    external_organizations_type_0_item = (
                        external_organizations_type_0_item_data.to_dict()
                    )
                else:
                    external_organizations_type_0_item = (
                        external_organizations_type_0_item_data
                    )
                external_organizations.append(external_organizations_type_0_item)

        else:
            external_organizations = self.external_organizations

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        hidden = self.hidden

        association_hidden = self.association_hidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "role": role,
                "externalPerson": external_person,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if name is not UNSET:
            field_dict["name"] = name
        if period is not UNSET:
            field_dict["period"] = period
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if association_hidden is not UNSET:
            field_dict["associationHidden"] = association_hidden

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0
        from ..models.name import Name

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_role(data: object) -> ClassificationRefType0 | None:
            if data is None:
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
            return cast(ClassificationRefType0 | None, data)

        role = _parse_role(d.pop("role"))

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

        def _parse_external_organizations(
            data: object,
        ) -> list[ExternalOrganizationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_organizations_type_0 = []
                _external_organizations_type_0 = data
                for (
                    external_organizations_type_0_item_data
                ) in _external_organizations_type_0:

                    def _parse_external_organizations_type_0_item(
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

                    external_organizations_type_0_item = (
                        _parse_external_organizations_type_0_item(
                            external_organizations_type_0_item_data
                        )
                    )

                    external_organizations_type_0.append(
                        external_organizations_type_0_item
                    )

                return external_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalOrganizationRefType0 | None] | None | Unset, data)

        external_organizations = _parse_external_organizations(
            d.pop("externalOrganizations", UNSET)
        )

        _name = d.pop("name", UNSET)
        name: Name | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = Name.from_dict(_name)

        _period = d.pop("period", UNSET)
        period: DateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = DateRange.from_dict(_period)

        hidden = d.pop("hidden", UNSET)

        association_hidden = d.pop("associationHidden", UNSET)

        data_set_external_contributor_association = cls(
            type_discriminator=type_discriminator,
            role=role,
            external_person=external_person,
            pure_id=pure_id,
            external_organizations=external_organizations,
            name=name,
            period=period,
            hidden=hidden,
            association_hidden=association_hidden,
        )

        data_set_external_contributor_association.additional_properties = d
        return data_set_external_contributor_association

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
