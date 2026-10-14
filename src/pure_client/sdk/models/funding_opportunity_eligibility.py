from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.funding_opportunity_eligibility_eligibility_fulfilment_type import (
    FundingOpportunityEligibilityEligibilityFulfilmentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="FundingOpportunityEligibility")


@_attrs_define
class FundingOpportunityEligibility:
    """Eligibility of the funding opportunity

    Attributes:
        eligibility_type_classification (ClassificationRefType0 | None): A reference to a classification value
        eligibility_fulfilment_type (FundingOpportunityEligibilityEligibilityFulfilmentType): The eligibility fulfilment
            type
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
    """

    eligibility_type_classification: ClassificationRefType0 | None
    eligibility_fulfilment_type: FundingOpportunityEligibilityEligibilityFulfilmentType
    pure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        eligibility_type_classification: dict[str, Any] | None
        if isinstance(self.eligibility_type_classification, ClassificationRefType0):
            eligibility_type_classification = (
                self.eligibility_type_classification.to_dict()
            )
        else:
            eligibility_type_classification = self.eligibility_type_classification

        eligibility_fulfilment_type = self.eligibility_fulfilment_type.value

        pure_id = self.pure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eligibilityTypeClassification": eligibility_type_classification,
                "eligibilityFulfilmentType": eligibility_fulfilment_type,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)

        def _parse_eligibility_type_classification(
            data: object,
        ) -> ClassificationRefType0 | None:
            if data is None:
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
            return cast(ClassificationRefType0 | None, data)

        eligibility_type_classification = _parse_eligibility_type_classification(
            d.pop("eligibilityTypeClassification")
        )

        eligibility_fulfilment_type = (
            FundingOpportunityEligibilityEligibilityFulfilmentType(
                d.pop("eligibilityFulfilmentType")
            )
        )

        pure_id = d.pop("pureId", UNSET)

        funding_opportunity_eligibility = cls(
            eligibility_type_classification=eligibility_type_classification,
            eligibility_fulfilment_type=eligibility_fulfilment_type,
            pure_id=pure_id,
        )

        funding_opportunity_eligibility.additional_properties = d
        return funding_opportunity_eligibility

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
