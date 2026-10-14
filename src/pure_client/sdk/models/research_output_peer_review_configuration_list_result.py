from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.research_output_peer_review_configuration import (
        ResearchOutputPeerReviewConfiguration,
    )


T = TypeVar("T", bound="ResearchOutputPeerReviewConfigurationListResult")


@_attrs_define
class ResearchOutputPeerReviewConfigurationListResult:
    """List of research output peer review configurations

    Attributes:
        research_output_peer_review_configurations (list[ResearchOutputPeerReviewConfiguration] | Unset):
    """

    research_output_peer_review_configurations: (
        list[ResearchOutputPeerReviewConfiguration] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        research_output_peer_review_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_output_peer_review_configurations, Unset):
            research_output_peer_review_configurations = []
            for (
                research_output_peer_review_configurations_item_data
            ) in self.research_output_peer_review_configurations:
                research_output_peer_review_configurations_item = (
                    research_output_peer_review_configurations_item_data.to_dict()
                )
                research_output_peer_review_configurations.append(
                    research_output_peer_review_configurations_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if research_output_peer_review_configurations is not UNSET:
            field_dict["researchOutputPeerReviewConfigurations"] = (
                research_output_peer_review_configurations
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.research_output_peer_review_configuration import (
            ResearchOutputPeerReviewConfiguration,
        )

        d = dict(src_dict)
        _research_output_peer_review_configurations = d.pop(
            "researchOutputPeerReviewConfigurations", UNSET
        )
        research_output_peer_review_configurations: (
            list[ResearchOutputPeerReviewConfiguration] | Unset
        ) = UNSET
        if _research_output_peer_review_configurations is not UNSET:
            research_output_peer_review_configurations = []
            for (
                research_output_peer_review_configurations_item_data
            ) in _research_output_peer_review_configurations:
                research_output_peer_review_configurations_item = (
                    ResearchOutputPeerReviewConfiguration.from_dict(
                        research_output_peer_review_configurations_item_data
                    )
                )

                research_output_peer_review_configurations.append(
                    research_output_peer_review_configurations_item
                )

        research_output_peer_review_configuration_list_result = cls(
            research_output_peer_review_configurations=research_output_peer_review_configurations,
        )

        research_output_peer_review_configuration_list_result.additional_properties = d
        return research_output_peer_review_configuration_list_result

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
