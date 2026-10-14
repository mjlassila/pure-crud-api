from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.project_ref_type_0 import ProjectRefType0


T = TypeVar("T", bound="ProjectAssociation")


@_attrs_define
class ProjectAssociation:
    """An association to a project.

    Attributes:
        project (None | ProjectRefType0): A reference to project
        relation_type (ClassificationRefType0 | None | Unset): A reference to a classification value
    """

    project: None | ProjectRefType0
    relation_type: ClassificationRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.project_ref_type_0 import ProjectRefType0

        project: dict[str, Any] | None
        if isinstance(self.project, ProjectRefType0):
            project = self.project.to_dict()
        else:
            project = self.project

        relation_type: dict[str, Any] | None | Unset
        if isinstance(self.relation_type, Unset):
            relation_type = UNSET
        elif isinstance(self.relation_type, ClassificationRefType0):
            relation_type = self.relation_type.to_dict()
        else:
            relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
            }
        )
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
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

        def _parse_relation_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        relation_type = _parse_relation_type(d.pop("relationType", UNSET))

        project_association = cls(
            project=project,
            relation_type=relation_type,
        )

        project_association.additional_properties = d
        return project_association

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
