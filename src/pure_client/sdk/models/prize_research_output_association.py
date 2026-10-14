from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.research_output_ref_type_0 import ResearchOutputRefType0


T = TypeVar("T", bound="PrizeResearchOutputAssociation")


@_attrs_define
class PrizeResearchOutputAssociation:
    """An association to a research output.

    Attributes:
        research_output (None | ResearchOutputRefType0): A reference to a research output
    """

    research_output: None | ResearchOutputRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0

        research_output: dict[str, Any] | None
        if isinstance(self.research_output, ResearchOutputRefType0):
            research_output = self.research_output.to_dict()
        else:
            research_output = self.research_output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "researchOutput": research_output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0

        d = dict(src_dict)

        def _parse_research_output(data: object) -> None | ResearchOutputRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_research_output_ref_type_0 = (
                    ResearchOutputRefType0.from_dict(data)
                )

                return componentsschemas_research_output_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResearchOutputRefType0, data)

        research_output = _parse_research_output(d.pop("researchOutput"))

        prize_research_output_association = cls(
            research_output=research_output,
        )

        prize_research_output_association.additional_properties = d
        return prize_research_output_association

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
