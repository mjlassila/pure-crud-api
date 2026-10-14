from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0


T = TypeVar("T", bound="OpenAccess")


@_attrs_define
class OpenAccess:
    """Open Access information.

    Attributes:
        open_access_permission (ClassificationRefType0 | None | Unset): A reference to a classification value
        open_access_embargo_months (int | None | Unset): Open access embargo months.
        open_access_embargo_date (datetime.date | None | Unset): Open access embargo date.
    """

    open_access_permission: ClassificationRefType0 | None | Unset = UNSET
    open_access_embargo_months: int | None | Unset = UNSET
    open_access_embargo_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        open_access_permission: dict[str, Any] | None | Unset
        if isinstance(self.open_access_permission, Unset):
            open_access_permission = UNSET
        elif isinstance(self.open_access_permission, ClassificationRefType0):
            open_access_permission = self.open_access_permission.to_dict()
        else:
            open_access_permission = self.open_access_permission

        open_access_embargo_months: int | None | Unset
        if isinstance(self.open_access_embargo_months, Unset):
            open_access_embargo_months = UNSET
        else:
            open_access_embargo_months = self.open_access_embargo_months

        open_access_embargo_date: None | str | Unset
        if isinstance(self.open_access_embargo_date, Unset):
            open_access_embargo_date = UNSET
        elif isinstance(self.open_access_embargo_date, datetime.date):
            open_access_embargo_date = self.open_access_embargo_date.isoformat()
        else:
            open_access_embargo_date = self.open_access_embargo_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_access_permission is not UNSET:
            field_dict["openAccessPermission"] = open_access_permission
        if open_access_embargo_months is not UNSET:
            field_dict["openAccessEmbargoMonths"] = open_access_embargo_months
        if open_access_embargo_date is not UNSET:
            field_dict["openAccessEmbargoDate"] = open_access_embargo_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        d = dict(src_dict)

        def _parse_open_access_permission(
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

        open_access_permission = _parse_open_access_permission(
            d.pop("openAccessPermission", UNSET)
        )

        def _parse_open_access_embargo_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_access_embargo_months = _parse_open_access_embargo_months(
            d.pop("openAccessEmbargoMonths", UNSET)
        )

        def _parse_open_access_embargo_date(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                open_access_embargo_date_type_0 = isoparse(data).date()

                return open_access_embargo_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        open_access_embargo_date = _parse_open_access_embargo_date(
            d.pop("openAccessEmbargoDate", UNSET)
        )

        open_access = cls(
            open_access_permission=open_access_permission,
            open_access_embargo_months=open_access_embargo_months,
            open_access_embargo_date=open_access_embargo_date,
        )

        open_access.additional_properties = d
        return open_access

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
