from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignable_role_ref import AssignableRoleRef
    from ..models.content_ref_type_0 import ContentRefType0


T = TypeVar("T", bound="LocalRoleAssignment")


@_attrs_define
class LocalRoleAssignment:
    """The complete picture of where a local role is to be assigned

    Attributes:
        role_definition (AssignableRoleRef): A reference to an assignable role that can be either local or global
        assignments (list[ContentRefType0 | None] | None | Unset): Where the local role is (to be) assigned
    """

    role_definition: AssignableRoleRef
    assignments: list[ContentRefType0 | None] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_ref_type_0 import ContentRefType0

        role_definition = self.role_definition.to_dict()

        assignments: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, list):
            assignments = []
            for assignments_type_0_item_data in self.assignments:
                assignments_type_0_item: dict[str, Any] | None
                if isinstance(assignments_type_0_item_data, ContentRefType0):
                    assignments_type_0_item = assignments_type_0_item_data.to_dict()
                else:
                    assignments_type_0_item = assignments_type_0_item_data
                assignments.append(assignments_type_0_item)

        else:
            assignments = self.assignments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roleDefinition": role_definition,
            }
        )
        if assignments is not UNSET:
            field_dict["assignments"] = assignments

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assignable_role_ref import AssignableRoleRef
        from ..models.content_ref_type_0 import ContentRefType0

        d = dict(src_dict)
        role_definition = AssignableRoleRef.from_dict(d.pop("roleDefinition"))

        def _parse_assignments(
            data: object,
        ) -> list[ContentRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignments_type_0 = []
                _assignments_type_0 = data
                for assignments_type_0_item_data in _assignments_type_0:

                    def _parse_assignments_type_0_item(
                        data: object,
                    ) -> ContentRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_content_ref_type_0 = (
                                ContentRefType0.from_dict(data)
                            )

                            return componentsschemas_content_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ContentRefType0 | None, data)

                    assignments_type_0_item = _parse_assignments_type_0_item(
                        assignments_type_0_item_data
                    )

                    assignments_type_0.append(assignments_type_0_item)

                return assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContentRefType0 | None] | None | Unset, data)

        assignments = _parse_assignments(d.pop("assignments", UNSET))

        local_role_assignment = cls(
            role_definition=role_definition,
            assignments=assignments,
        )

        local_role_assignment.additional_properties = d
        return local_role_assignment

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
