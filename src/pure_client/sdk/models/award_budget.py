from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_funding_budget_association import AwardFundingBudgetAssociation
    from ..models.visibility import Visibility


T = TypeVar("T", bound="AwardBudget")


@_attrs_define
class AwardBudget:
    """A budget for an award.

    Attributes:
        visibility (Visibility): Visibility of an object
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        budgets (list[AwardFundingBudgetAssociation] | None | Unset): Individual entries of the budget.
    """

    visibility: Visibility
    pure_id: int | Unset = UNSET
    budgets: list[AwardFundingBudgetAssociation] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visibility = self.visibility.to_dict()

        pure_id = self.pure_id

        budgets: list[dict[str, Any]] | None | Unset
        if isinstance(self.budgets, Unset):
            budgets = UNSET
        elif isinstance(self.budgets, list):
            budgets = []
            for budgets_type_0_item_data in self.budgets:
                budgets_type_0_item = budgets_type_0_item_data.to_dict()
                budgets.append(budgets_type_0_item)

        else:
            budgets = self.budgets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if budgets is not UNSET:
            field_dict["budgets"] = budgets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.award_funding_budget_association import (
            AwardFundingBudgetAssociation,
        )
        from ..models.visibility import Visibility

        d = dict(src_dict)
        visibility = Visibility.from_dict(d.pop("visibility"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_budgets(
            data: object,
        ) -> list[AwardFundingBudgetAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                budgets_type_0 = []
                _budgets_type_0 = data
                for budgets_type_0_item_data in _budgets_type_0:
                    budgets_type_0_item = AwardFundingBudgetAssociation.from_dict(
                        budgets_type_0_item_data
                    )

                    budgets_type_0.append(budgets_type_0_item)

                return budgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AwardFundingBudgetAssociation] | None | Unset, data)

        budgets = _parse_budgets(d.pop("budgets", UNSET))

        award_budget = cls(
            visibility=visibility,
            pure_id=pure_id,
            budgets=budgets,
        )

        award_budget.additional_properties = d
        return award_budget

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
