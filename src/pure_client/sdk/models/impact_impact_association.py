from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.impact_ref_type_0 import ImpactRefType0


T = TypeVar("T", bound="ImpactImpactAssociation")


@_attrs_define
class ImpactImpactAssociation:
    """An association to an impact

    Attributes:
        impact (ImpactRefType0 | None): A reference to impact
    """

    impact: ImpactRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.impact_ref_type_0 import ImpactRefType0

        impact: dict[str, Any] | None
        if isinstance(self.impact, ImpactRefType0):
            impact = self.impact.to_dict()
        else:
            impact = self.impact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "impact": impact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.impact_ref_type_0 import ImpactRefType0

        d = dict(src_dict)

        def _parse_impact(data: object) -> ImpactRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_impact_ref_type_0 = ImpactRefType0.from_dict(data)

                return componentsschemas_impact_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImpactRefType0 | None, data)

        impact = _parse_impact(d.pop("impact"))

        impact_impact_association = cls(
            impact=impact,
        )

        impact_impact_association.additional_properties = d
        return impact_impact_association

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
