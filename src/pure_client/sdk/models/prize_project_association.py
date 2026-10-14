from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_ref_type_0 import ProjectRefType0


T = TypeVar("T", bound="PrizeProjectAssociation")


@_attrs_define
class PrizeProjectAssociation:
    """An association to a project.

    Attributes:
        project (None | ProjectRefType0): A reference to project
    """

    project: None | ProjectRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.project_ref_type_0 import ProjectRefType0

        project: dict[str, Any] | None
        if isinstance(self.project, ProjectRefType0):
            project = self.project.to_dict()
        else:
            project = self.project

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.project_ref_type_0 import ProjectRefType0

        d = dict(src_dict)

        def _parse_project(data: object) -> None | ProjectRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_project_ref_type_0 = ProjectRefType0.from_dict(data)

                return componentsschemas_project_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProjectRefType0, data)

        project = _parse_project(d.pop("project"))

        prize_project_association = cls(
            project=project,
        )

        prize_project_association.additional_properties = d
        return prize_project_association

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
