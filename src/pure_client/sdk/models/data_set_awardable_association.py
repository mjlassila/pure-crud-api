from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_ref_type_0 import AwardRefType0
    from ..models.data_set_ref_type_0 import DataSetRefType0


T = TypeVar("T", bound="DataSetAwardableAssociation")


@_attrs_define
class DataSetAwardableAssociation:
    """A relation to a dataset, optionally in the context of the Award that made it possible.

    Attributes:
        data_set (DataSetRefType0 | None): A reference to a data set
        award (AwardRefType0 | None | Unset): A reference to an award
    """

    data_set: DataSetRefType0 | None
    award: AwardRefType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.data_set_ref_type_0 import DataSetRefType0

        data_set: dict[str, Any] | None
        if isinstance(self.data_set, DataSetRefType0):
            data_set = self.data_set.to_dict()
        else:
            data_set = self.data_set

        award: dict[str, Any] | None | Unset
        if isinstance(self.award, Unset):
            award = UNSET
        elif isinstance(self.award, AwardRefType0):
            award = self.award.to_dict()
        else:
            award = self.award

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataSet": data_set,
            }
        )
        if award is not UNSET:
            field_dict["award"] = award

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.data_set_ref_type_0 import DataSetRefType0

        d = dict(src_dict)

        def _parse_data_set(data: object) -> DataSetRefType0 | None:
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

        data_set = _parse_data_set(d.pop("dataSet"))

        def _parse_award(data: object) -> AwardRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_award_ref_type_0 = AwardRefType0.from_dict(data)

                return componentsschemas_award_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwardRefType0 | None | Unset, data)

        award = _parse_award(d.pop("award", UNSET))

        data_set_awardable_association = cls(
            data_set=data_set,
            award=award,
        )

        data_set_awardable_association.additional_properties = d
        return data_set_awardable_association

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
