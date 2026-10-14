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
    from ..models.date_range import DateRange


T = TypeVar("T", bound="ElectronicVersionType0")


@_attrs_define
class ElectronicVersionType0:
    """Electronic version related to a research output.

    Attributes:
        type_discriminator (str):
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        access_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        embargo_period (DateRange | Unset): A date range
        license_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        user_defined_license (None | str | Unset): License defined by the user.
        visible_on_portal_date (datetime.date | Unset): Date where this document is/will be visible on the portal.
        creator (str | Unset): Username of creator
        created (datetime.datetime | Unset): Date and time of creation
    """

    type_discriminator: str
    pure_id: int | Unset = UNSET
    access_type: ClassificationRefType0 | None | Unset = UNSET
    embargo_period: DateRange | Unset = UNSET
    license_type: ClassificationRefType0 | None | Unset = UNSET
    user_defined_license: None | str | Unset = UNSET
    visible_on_portal_date: datetime.date | Unset = UNSET
    creator: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        type_discriminator = self.type_discriminator

        pure_id = self.pure_id

        access_type: dict[str, Any] | None | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        elif isinstance(self.access_type, ClassificationRefType0):
            access_type = self.access_type.to_dict()
        else:
            access_type = self.access_type

        embargo_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embargo_period, Unset):
            embargo_period = self.embargo_period.to_dict()

        license_type: dict[str, Any] | None | Unset
        if isinstance(self.license_type, Unset):
            license_type = UNSET
        elif isinstance(self.license_type, ClassificationRefType0):
            license_type = self.license_type.to_dict()
        else:
            license_type = self.license_type

        user_defined_license: None | str | Unset
        if isinstance(self.user_defined_license, Unset):
            user_defined_license = UNSET
        else:
            user_defined_license = self.user_defined_license

        visible_on_portal_date: str | Unset = UNSET
        if not isinstance(self.visible_on_portal_date, Unset):
            visible_on_portal_date = self.visible_on_portal_date.isoformat()

        creator = self.creator

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if embargo_period is not UNSET:
            field_dict["embargoPeriod"] = embargo_period
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if user_defined_license is not UNSET:
            field_dict["userDefinedLicense"] = user_defined_license
        if visible_on_portal_date is not UNSET:
            field_dict["visibleOnPortalDate"] = visible_on_portal_date
        if creator is not UNSET:
            field_dict["creator"] = creator
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        pure_id = d.pop("pureId", UNSET)

        def _parse_access_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        access_type = _parse_access_type(d.pop("accessType", UNSET))

        _embargo_period = d.pop("embargoPeriod", UNSET)
        embargo_period: DateRange | Unset
        if isinstance(_embargo_period, Unset):
            embargo_period = UNSET
        else:
            embargo_period = DateRange.from_dict(_embargo_period)

        def _parse_license_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        license_type = _parse_license_type(d.pop("licenseType", UNSET))

        def _parse_user_defined_license(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_defined_license = _parse_user_defined_license(
            d.pop("userDefinedLicense", UNSET)
        )

        _visible_on_portal_date = d.pop("visibleOnPortalDate", UNSET)
        visible_on_portal_date: datetime.date | Unset
        if isinstance(_visible_on_portal_date, Unset):
            visible_on_portal_date = UNSET
        else:
            visible_on_portal_date = isoparse(_visible_on_portal_date).date()

        creator = d.pop("creator", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        electronic_version_type_0 = cls(
            type_discriminator=type_discriminator,
            pure_id=pure_id,
            access_type=access_type,
            embargo_period=embargo_period,
            license_type=license_type,
            user_defined_license=user_defined_license,
            visible_on_portal_date=visible_on_portal_date,
            creator=creator,
            created=created,
        )

        electronic_version_type_0.additional_properties = d
        return electronic_version_type_0

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
