from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_set_ref_type_0 import DataSetRefType0


T = TypeVar("T", bound="PrizeDataSetAssociation")


@_attrs_define
class PrizeDataSetAssociation:
    """An association to a dataset.

    Attributes:
        dataset (DataSetRefType0 | None): A reference to a data set
    """

    dataset: DataSetRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_set_ref_type_0 import DataSetRefType0

        dataset: dict[str, Any] | None
        if isinstance(self.dataset, DataSetRefType0):
            dataset = self.dataset.to_dict()
        else:
            dataset = self.dataset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.data_set_ref_type_0 import DataSetRefType0

        d = dict(src_dict)

        def _parse_dataset(data: object) -> DataSetRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_set_ref_type_0 = DataSetRefType0.from_dict(data)

                return componentsschemas_data_set_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataSetRefType0 | None, data)

        dataset = _parse_dataset(d.pop("dataset"))

        prize_data_set_association = cls(
            dataset=dataset,
        )

        prize_data_set_association.additional_properties = d
        return prize_data_set_association

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
