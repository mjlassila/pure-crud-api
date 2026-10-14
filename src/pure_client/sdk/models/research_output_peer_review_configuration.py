from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.research_output_peer_review_configuration_combination import (
        ResearchOutputPeerReviewConfigurationCombination,
    )


T = TypeVar("T", bound="ResearchOutputPeerReviewConfiguration")


@_attrs_define
class ResearchOutputPeerReviewConfiguration:
    """A specification for a research output type and the allowed combinations of it's interrelated fields: category,
    peerReview, and internationPeerReview

        Attributes:
            research_output_type (ClassificationRefType0 | None | Unset): A reference to a classification value
            allowed_combinations (list[ResearchOutputPeerReviewConfigurationCombination] | Unset): The valid combinations of
                the interrelated fields
    """

    research_output_type: ClassificationRefType0 | None | Unset = UNSET
    allowed_combinations: (
        list[ResearchOutputPeerReviewConfigurationCombination] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        research_output_type: dict[str, Any] | None | Unset
        if isinstance(self.research_output_type, Unset):
            research_output_type = UNSET
        elif isinstance(self.research_output_type, ClassificationRefType0):
            research_output_type = self.research_output_type.to_dict()
        else:
            research_output_type = self.research_output_type

        allowed_combinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowed_combinations, Unset):
            allowed_combinations = []
            for allowed_combinations_item_data in self.allowed_combinations:
                allowed_combinations_item = allowed_combinations_item_data.to_dict()
                allowed_combinations.append(allowed_combinations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if research_output_type is not UNSET:
            field_dict["researchOutputType"] = research_output_type
        if allowed_combinations is not UNSET:
            field_dict["allowedCombinations"] = allowed_combinations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.research_output_peer_review_configuration_combination import (
            ResearchOutputPeerReviewConfigurationCombination,
        )

        d = dict(src_dict)

        def _parse_research_output_type(
            data: object,
        ) -> ClassificationRefType0 | None | Unset:
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

        research_output_type = _parse_research_output_type(
            d.pop("researchOutputType", UNSET)
        )

        _allowed_combinations = d.pop("allowedCombinations", UNSET)
        allowed_combinations: (
            list[ResearchOutputPeerReviewConfigurationCombination] | Unset
        ) = UNSET
        if _allowed_combinations is not UNSET:
            allowed_combinations = []
            for allowed_combinations_item_data in _allowed_combinations:
                allowed_combinations_item = (
                    ResearchOutputPeerReviewConfigurationCombination.from_dict(
                        allowed_combinations_item_data
                    )
                )

                allowed_combinations.append(allowed_combinations_item)

        research_output_peer_review_configuration = cls(
            research_output_type=research_output_type,
            allowed_combinations=allowed_combinations,
        )

        research_output_peer_review_configuration.additional_properties = d
        return research_output_peer_review_configuration

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
