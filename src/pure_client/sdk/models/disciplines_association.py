from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_ref_type_0 import ContentRefType0
    from ..models.disciplines_discipline_assignment import (
        DisciplinesDisciplineAssignment,
    )


T = TypeVar("T", bound="DisciplinesAssociation")


@_attrs_define
class DisciplinesAssociation:
    """An association between a content and a number of discipline assignments

    Attributes:
        discipline_assignments (list[DisciplinesDisciplineAssignment]): A collection of assigned disciplines
        content (ContentRefType0 | None | Unset):
        discipline_scheme (str | Unset): The discipline scheme these disciplines are assigned from
    """

    discipline_assignments: list[DisciplinesDisciplineAssignment]
    content: ContentRefType0 | None | Unset = UNSET
    discipline_scheme: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_ref_type_0 import ContentRefType0

        discipline_assignments = []
        for discipline_assignments_item_data in self.discipline_assignments:
            discipline_assignments_item = discipline_assignments_item_data.to_dict()
            discipline_assignments.append(discipline_assignments_item)

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, ContentRefType0):
            content = self.content.to_dict()
        else:
            content = self.content

        discipline_scheme = self.discipline_scheme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disciplineAssignments": discipline_assignments,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if discipline_scheme is not UNSET:
            field_dict["disciplineScheme"] = discipline_scheme

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.content_ref_type_0 import ContentRefType0
        from ..models.disciplines_discipline_assignment import (
            DisciplinesDisciplineAssignment,
        )

        d = dict(src_dict)
        discipline_assignments = []
        _discipline_assignments = d.pop("disciplineAssignments")
        for discipline_assignments_item_data in _discipline_assignments:
            discipline_assignments_item = DisciplinesDisciplineAssignment.from_dict(
                discipline_assignments_item_data
            )

            discipline_assignments.append(discipline_assignments_item)

        def _parse_content(data: object) -> ContentRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_ref_type_0 = ContentRefType0.from_dict(data)

                return componentsschemas_content_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContentRefType0 | None | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        discipline_scheme = d.pop("disciplineScheme", UNSET)

        disciplines_association = cls(
            discipline_assignments=discipline_assignments,
            content=content,
            discipline_scheme=discipline_scheme,
        )

        disciplines_association.additional_properties = d
        return disciplines_association

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
