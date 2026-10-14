from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.concept_ref_type_0 import ConceptRefType0


T = TypeVar("T", bound="RankedConcept")


@_attrs_define
class RankedConcept:
    """A ranked concept

    Attributes:
        concept (ConceptRefType0 | None): A reference to a concept
        rank (float): The rank of the ranked concept. If this is not set on creation, the ranked concept will have a
            default rank value of 0
        weighted_rank (float | None | Unset): WeightedRank
        frequency (int | None | Unset): Frequency
    """

    concept: ConceptRefType0 | None
    rank: float
    weighted_rank: float | None | Unset = UNSET
    frequency: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.concept_ref_type_0 import ConceptRefType0

        concept: dict[str, Any] | None
        if isinstance(self.concept, ConceptRefType0):
            concept = self.concept.to_dict()
        else:
            concept = self.concept

        rank = self.rank

        weighted_rank: float | None | Unset
        if isinstance(self.weighted_rank, Unset):
            weighted_rank = UNSET
        else:
            weighted_rank = self.weighted_rank

        frequency: int | None | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "concept": concept,
                "rank": rank,
            }
        )
        if weighted_rank is not UNSET:
            field_dict["weightedRank"] = weighted_rank
        if frequency is not UNSET:
            field_dict["frequency"] = frequency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.concept_ref_type_0 import ConceptRefType0

        d = dict(src_dict)

        def _parse_concept(data: object) -> ConceptRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_concept_ref_type_0 = ConceptRefType0.from_dict(data)

                return componentsschemas_concept_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConceptRefType0 | None, data)

        concept = _parse_concept(d.pop("concept"))

        rank = d.pop("rank")

        def _parse_weighted_rank(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weighted_rank = _parse_weighted_rank(d.pop("weightedRank", UNSET))

        def _parse_frequency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        ranked_concept = cls(
            concept=concept,
            rank=rank,
            weighted_rank=weighted_rank,
            frequency=frequency,
        )

        ranked_concept.additional_properties = d
        return ranked_concept

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
