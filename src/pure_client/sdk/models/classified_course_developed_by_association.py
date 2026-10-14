from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name import Name
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="ClassifiedCourseDevelopedByAssociation")


@_attrs_define
class ClassifiedCourseDevelopedByAssociation:
    """A person who developed a given course.

    Attributes:
        organizations (list[None | OrganizationRefType0]): A collection of organization associations
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        person (None | PersonRefType0 | Unset): A reference to a person internal to the institution
        name (Name | Unset): A name describing a person, made up of given- and family name
        association_hidden (bool | Unset): True if the content should be hidden from the person's portal profile, false
            otherwise.
    """

    organizations: list[None | OrganizationRefType0]
    pure_id: int | Unset = UNSET
    person: None | PersonRefType0 | Unset = UNSET
    name: Name | Unset = UNSET
    association_hidden: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item: dict[str, Any] | None
            if isinstance(organizations_item_data, OrganizationRefType0):
                organizations_item = organizations_item_data.to_dict()
            else:
                organizations_item = organizations_item_data
            organizations.append(organizations_item)

        pure_id = self.pure_id

        person: dict[str, Any] | None | Unset
        if isinstance(self.person, Unset):
            person = UNSET
        elif isinstance(self.person, PersonRefType0):
            person = self.person.to_dict()
        else:
            person = self.person

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        association_hidden = self.association_hidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizations": organizations,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if person is not UNSET:
            field_dict["person"] = person
        if name is not UNSET:
            field_dict["name"] = name
        if association_hidden is not UNSET:
            field_dict["associationHidden"] = association_hidden

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.name import Name
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)
        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:

            def _parse_organizations_item(data: object) -> None | OrganizationRefType0:
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

            organizations_item = _parse_organizations_item(organizations_item_data)

            organizations.append(organizations_item)

        pure_id = d.pop("pureId", UNSET)

        def _parse_person(data: object) -> None | PersonRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_ref_type_0 = PersonRefType0.from_dict(data)

                return componentsschemas_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonRefType0 | Unset, data)

        person = _parse_person(d.pop("person", UNSET))

        _name = d.pop("name", UNSET)
        name: Name | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = Name.from_dict(_name)

        association_hidden = d.pop("associationHidden", UNSET)

        classified_course_developed_by_association = cls(
            organizations=organizations,
            pure_id=pure_id,
            person=person,
            name=name,
            association_hidden=association_hidden,
        )

        classified_course_developed_by_association.additional_properties = d
        return classified_course_developed_by_association

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
