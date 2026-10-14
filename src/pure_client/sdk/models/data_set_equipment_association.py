from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.equipment_ref_type_0 import EquipmentRefType0


T = TypeVar("T", bound="DataSetEquipmentAssociation")


@_attrs_define
class DataSetEquipmentAssociation:
    """An association to an equipment.

    Attributes:
        equipment (EquipmentRefType0 | None): A reference to a piece of equipment
    """

    equipment: EquipmentRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.equipment_ref_type_0 import EquipmentRefType0

        equipment: dict[str, Any] | None
        if isinstance(self.equipment, EquipmentRefType0):
            equipment = self.equipment.to_dict()
        else:
            equipment = self.equipment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "equipment": equipment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.equipment_ref_type_0 import EquipmentRefType0

        d = dict(src_dict)

        def _parse_equipment(data: object) -> EquipmentRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_equipment_ref_type_0 = EquipmentRefType0.from_dict(
                    data
                )

                return componentsschemas_equipment_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EquipmentRefType0 | None, data)

        equipment = _parse_equipment(d.pop("equipment"))

        data_set_equipment_association = cls(
            equipment=equipment,
        )

        data_set_equipment_association.additional_properties = d
        return data_set_equipment_association

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
