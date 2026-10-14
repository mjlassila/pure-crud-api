from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.name import Name
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="InternalContributorAssociation")


@_attrs_define
class InternalContributorAssociation:
    """An internal contributor associated with the content.

    Attributes:
        type_discriminator (str):
        name (Name): A name describing a person, made up of given- and family name
        role (ClassificationRefType0 | None): A reference to a classification value
        person (None | PersonRefType0): A reference to a person internal to the institution
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        hidden (bool | Unset): If this contribution should be hidden, this is set to true, false otherwise. This is used
            for research output that have author collaborations. If they do, we hide the individual contributors.
        contribution_description (None | str | Unset): A string that details the contribution of the associated person.
        contribution_percentage (float | None | Unset): A real number between 0 and 1, describing the percentage of the
            contribution of the person.
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
        corresponding_author (bool | Unset): True if the contributor is the corresponding author, false otherwise.
        association_hidden (bool | Unset): True if the content should be hidden from the person's portal profile, false
            otherwise.
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organizational unit
            affiliations.
    """

    type_discriminator: str
    name: Name
    role: ClassificationRefType0 | None
    person: None | PersonRefType0
    pure_id: int | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    hidden: bool | Unset = UNSET
    contribution_description: None | str | Unset = UNSET
    contribution_percentage: float | None | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    corresponding_author: bool | Unset = UNSET
    association_hidden: bool | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        type_discriminator = self.type_discriminator

        name = self.name.to_dict()

        role: dict[str, Any] | None
        if isinstance(self.role, ClassificationRefType0):
            role = self.role.to_dict()
        else:
            role = self.role

        person: dict[str, Any] | None
        if isinstance(self.person, PersonRefType0):
            person = self.person.to_dict()
        else:
            person = self.person

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

        hidden = self.hidden

        contribution_description: None | str | Unset
        if isinstance(self.contribution_description, Unset):
            contribution_description = UNSET
        else:
            contribution_description = self.contribution_description

        contribution_percentage: float | None | Unset
        if isinstance(self.contribution_percentage, Unset):
            contribution_percentage = UNSET
        else:
            contribution_percentage = self.contribution_percentage

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, ClassificationRefType0):
            country = self.country.to_dict()
        else:
            country = self.country

        corresponding_author = self.corresponding_author

        association_hidden = self.association_hidden

        organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item: dict[str, Any] | None
                if isinstance(organizations_type_0_item_data, OrganizationRefType0):
                    organizations_type_0_item = organizations_type_0_item_data.to_dict()
                else:
                    organizations_type_0_item = organizations_type_0_item_data
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "name": name,
                "role": role,
                "person": person,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if contribution_description is not UNSET:
            field_dict["contributionDescription"] = contribution_description
        if contribution_percentage is not UNSET:
            field_dict["contributionPercentage"] = contribution_percentage
        if country is not UNSET:
            field_dict["country"] = country
        if corresponding_author is not UNSET:
            field_dict["correspondingAuthor"] = corresponding_author
        if association_hidden is not UNSET:
            field_dict["associationHidden"] = association_hidden
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.name import Name
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        name = Name.from_dict(d.pop("name"))

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

        hidden = d.pop("hidden", UNSET)

        def _parse_contribution_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contribution_description = _parse_contribution_description(
            d.pop("contributionDescription", UNSET)
        )

        def _parse_contribution_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        contribution_percentage = _parse_contribution_percentage(
            d.pop("contributionPercentage", UNSET)
        )

        def _parse_country(data: object) -> ClassificationRefType0 | None | Unset:
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

        country = _parse_country(d.pop("country", UNSET))

        corresponding_author = d.pop("correspondingAuthor", UNSET)

        association_hidden = d.pop("associationHidden", UNSET)

        def _parse_organizations(
            data: object,
        ) -> list[None | OrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:

                    def _parse_organizations_type_0_item(
                        data: object,
                    ) -> None | OrganizationRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_organization_ref_type_0 = (
                                OrganizationRefType0.from_dict(data)
                            )

                            return componentsschemas_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | OrganizationRefType0, data)

                    organizations_type_0_item = _parse_organizations_type_0_item(
                        organizations_type_0_item_data
                    )

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | OrganizationRefType0] | None | Unset, data)

        organizations = _parse_organizations(d.pop("organizations", UNSET))

        internal_contributor_association = cls(
            type_discriminator=type_discriminator,
            name=name,
            role=role,
            person=person,
            pure_id=pure_id,
            external_organizations=external_organizations,
            hidden=hidden,
            contribution_description=contribution_description,
            contribution_percentage=contribution_percentage,
            country=country,
            corresponding_author=corresponding_author,
            association_hidden=association_hidden,
            organizations=organizations,
        )

        internal_contributor_association.additional_properties = d
        return internal_contributor_association

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
