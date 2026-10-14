from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.research_output_peer_review_configuration_combination_peer_reviewable import (
    ResearchOutputPeerReviewConfigurationCombinationPeerReviewable,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="ResearchOutputPeerReviewConfigurationCombination")


@_attrs_define
class ResearchOutputPeerReviewConfigurationCombination:
    """A specification for a publication category and it's interrelated fields: peerReview and internationalPeerReview

    Attributes:
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        peer_reviewable (ResearchOutputPeerReviewConfigurationCombinationPeerReviewable | Unset): Research output peer
            reviewable
    """

    category: ClassificationRefType0 | None | Unset = UNSET
    peer_reviewable: (
        ResearchOutputPeerReviewConfigurationCombinationPeerReviewable | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

        peer_reviewable: str | Unset = UNSET
        if not isinstance(self.peer_reviewable, Unset):
            peer_reviewable = self.peer_reviewable.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if peer_reviewable is not UNSET:
            field_dict["peerReviewable"] = peer_reviewable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)

        def _parse_category(data: object) -> ClassificationRefType0 | None | Unset:
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

        category = _parse_category(d.pop("category", UNSET))

        _peer_reviewable = d.pop("peerReviewable", UNSET)
        peer_reviewable: (
            ResearchOutputPeerReviewConfigurationCombinationPeerReviewable | Unset
        )
        if isinstance(_peer_reviewable, Unset):
            peer_reviewable = UNSET
        else:
            peer_reviewable = (
                ResearchOutputPeerReviewConfigurationCombinationPeerReviewable(
                    _peer_reviewable
                )
            )

        research_output_peer_review_configuration_combination = cls(
            category=category,
            peer_reviewable=peer_reviewable,
        )

        research_output_peer_review_configuration_combination.additional_properties = d
        return research_output_peer_review_configuration_combination

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
