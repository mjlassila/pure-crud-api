from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.global_role_assignment import GlobalRoleAssignment
    from ..models.local_role_assignment import LocalRoleAssignment


T = TypeVar("T", bound="UserRoles")


@_attrs_define
class UserRoles:
    """The complete picture of a users roles

    Attributes:
        version (str): Used to guard against conflicting updates. The property should never be modified explicitly by a
            client
        global_role_assignments (list[GlobalRoleAssignment]): Current/requested global role assignments
        local_role_assignments (list[LocalRoleAssignment]): Current/requested local role assignments
    """

    version: str
    global_role_assignments: list[GlobalRoleAssignment]
    local_role_assignments: list[LocalRoleAssignment]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        global_role_assignments = []
        for global_role_assignments_item_data in self.global_role_assignments:
            global_role_assignments_item = global_role_assignments_item_data.to_dict()
            global_role_assignments.append(global_role_assignments_item)

        local_role_assignments = []
        for local_role_assignments_item_data in self.local_role_assignments:
            local_role_assignments_item = local_role_assignments_item_data.to_dict()
            local_role_assignments.append(local_role_assignments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "globalRoleAssignments": global_role_assignments,
                "localRoleAssignments": local_role_assignments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.global_role_assignment import GlobalRoleAssignment
        from ..models.local_role_assignment import LocalRoleAssignment

        d = dict(src_dict)
        version = d.pop("version")

        global_role_assignments = []
        _global_role_assignments = d.pop("globalRoleAssignments")
        for global_role_assignments_item_data in _global_role_assignments:
            global_role_assignments_item = GlobalRoleAssignment.from_dict(
                global_role_assignments_item_data
            )

            global_role_assignments.append(global_role_assignments_item)

        local_role_assignments = []
        _local_role_assignments = d.pop("localRoleAssignments")
        for local_role_assignments_item_data in _local_role_assignments:
            local_role_assignments_item = LocalRoleAssignment.from_dict(
                local_role_assignments_item_data
            )

            local_role_assignments.append(local_role_assignments_item)

        user_roles = cls(
            version=version,
            global_role_assignments=global_role_assignments,
            local_role_assignments=local_role_assignments,
        )

        user_roles.additional_properties = d
        return user_roles

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
