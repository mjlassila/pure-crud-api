from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.year_month_type_0 import YearMonthType0


T = TypeVar("T", bound="ResearcherCommitment")


@_attrs_define
class ResearcherCommitment:
    """Planned and actual research commitment.

    Attributes:
        year_month (None | YearMonthType0): A date that can be defined by only year and month
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        actual_researcher_commitment (float | None | Unset): The actual researcher commitment.
        planned_researcher_commitment (float | None | Unset): The planned researcher commitment.
    """

    year_month: None | YearMonthType0
    pure_id: int | Unset = UNSET
    actual_researcher_commitment: float | None | Unset = UNSET
    planned_researcher_commitment: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.year_month_type_0 import YearMonthType0

        year_month: dict[str, Any] | None
        if isinstance(self.year_month, YearMonthType0):
            year_month = self.year_month.to_dict()
        else:
            year_month = self.year_month

        pure_id = self.pure_id

        actual_researcher_commitment: float | None | Unset
        if isinstance(self.actual_researcher_commitment, Unset):
            actual_researcher_commitment = UNSET
        else:
            actual_researcher_commitment = self.actual_researcher_commitment

        planned_researcher_commitment: float | None | Unset
        if isinstance(self.planned_researcher_commitment, Unset):
            planned_researcher_commitment = UNSET
        else:
            planned_researcher_commitment = self.planned_researcher_commitment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yearMonth": year_month,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if actual_researcher_commitment is not UNSET:
            field_dict["actualResearcherCommitment"] = actual_researcher_commitment
        if planned_researcher_commitment is not UNSET:
            field_dict["plannedResearcherCommitment"] = planned_researcher_commitment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.year_month_type_0 import YearMonthType0

        d = dict(src_dict)

        def _parse_year_month(data: object) -> None | YearMonthType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_year_month_type_0 = YearMonthType0.from_dict(data)

                return componentsschemas_year_month_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | YearMonthType0, data)

        year_month = _parse_year_month(d.pop("yearMonth"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_actual_researcher_commitment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        actual_researcher_commitment = _parse_actual_researcher_commitment(
            d.pop("actualResearcherCommitment", UNSET)
        )

        def _parse_planned_researcher_commitment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        planned_researcher_commitment = _parse_planned_researcher_commitment(
            d.pop("plannedResearcherCommitment", UNSET)
        )

        researcher_commitment = cls(
            year_month=year_month,
            pure_id=pure_id,
            actual_researcher_commitment=actual_researcher_commitment,
            planned_researcher_commitment=planned_researcher_commitment,
        )

        researcher_commitment.additional_properties = d
        return researcher_commitment

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
