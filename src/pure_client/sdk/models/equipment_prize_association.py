from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prize_ref_type_0 import PrizeRefType0


T = TypeVar("T", bound="EquipmentPrizeAssociation")


@_attrs_define
class EquipmentPrizeAssociation:
    """An association to a prize.

    Attributes:
        prize (None | PrizeRefType0): A reference to a prize
    """

    prize: None | PrizeRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prize_ref_type_0 import PrizeRefType0

        prize: dict[str, Any] | None
        if isinstance(self.prize, PrizeRefType0):
            prize = self.prize.to_dict()
        else:
            prize = self.prize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prize": prize,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.prize_ref_type_0 import PrizeRefType0

        d = dict(src_dict)

        def _parse_prize(data: object) -> None | PrizeRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_prize_ref_type_0 = PrizeRefType0.from_dict(data)

                return componentsschemas_prize_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrizeRefType0, data)

        prize = _parse_prize(d.pop("prize"))

        equipment_prize_association = cls(
            prize=prize,
        )

        equipment_prize_association.additional_properties = d
        return equipment_prize_association

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
