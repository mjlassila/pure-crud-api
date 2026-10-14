from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sherpa_romeo_open_access_permission_type_0 import (
        SherpaRomeoOpenAccessPermissionType0,
    )


T = TypeVar("T", bound="SherpaRomeoPolicy")


@_attrs_define
class SherpaRomeoPolicy:
    """Describes a SHERPA RoMEO open access policy.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        open_access_prohibited (bool | Unset): If the policy prohibits Open Access - in which case there won't be any
            Open Access permissions
        open_access_permissions (list[None | SherpaRomeoOpenAccessPermissionType0] | None | Unset): The Open Access
            permissions for this policy
        publisher_policies (list[None | str] | None | Unset): A list of publisher specific policies
        sherpa_romeo_uri (None | str | Unset): The link to the journal in SHERPA RoMEO
        last_updated_date (datetime.datetime | None | Unset): The link to the journal in SHERPA RoMEO
    """

    pure_id: int | Unset = UNSET
    open_access_prohibited: bool | Unset = UNSET
    open_access_permissions: (
        list[None | SherpaRomeoOpenAccessPermissionType0] | None | Unset
    ) = UNSET
    publisher_policies: list[None | str] | None | Unset = UNSET
    sherpa_romeo_uri: None | str | Unset = UNSET
    last_updated_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sherpa_romeo_open_access_permission_type_0 import (
            SherpaRomeoOpenAccessPermissionType0,
        )

        pure_id = self.pure_id

        open_access_prohibited = self.open_access_prohibited

        open_access_permissions: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.open_access_permissions, Unset):
            open_access_permissions = UNSET
        elif isinstance(self.open_access_permissions, list):
            open_access_permissions = []
            for (
                open_access_permissions_type_0_item_data
            ) in self.open_access_permissions:
                open_access_permissions_type_0_item: dict[str, Any] | None
                if isinstance(
                    open_access_permissions_type_0_item_data,
                    SherpaRomeoOpenAccessPermissionType0,
                ):
                    open_access_permissions_type_0_item = (
                        open_access_permissions_type_0_item_data.to_dict()
                    )
                else:
                    open_access_permissions_type_0_item = (
                        open_access_permissions_type_0_item_data
                    )
                open_access_permissions.append(open_access_permissions_type_0_item)

        else:
            open_access_permissions = self.open_access_permissions

        publisher_policies: list[None | str] | None | Unset
        if isinstance(self.publisher_policies, Unset):
            publisher_policies = UNSET
        elif isinstance(self.publisher_policies, list):
            publisher_policies = []
            for publisher_policies_type_0_item_data in self.publisher_policies:
                publisher_policies_type_0_item: None | str
                publisher_policies_type_0_item = publisher_policies_type_0_item_data
                publisher_policies.append(publisher_policies_type_0_item)

        else:
            publisher_policies = self.publisher_policies

        sherpa_romeo_uri: None | str | Unset
        if isinstance(self.sherpa_romeo_uri, Unset):
            sherpa_romeo_uri = UNSET
        else:
            sherpa_romeo_uri = self.sherpa_romeo_uri

        last_updated_date: None | str | Unset
        if isinstance(self.last_updated_date, Unset):
            last_updated_date = UNSET
        elif isinstance(self.last_updated_date, datetime.datetime):
            last_updated_date = self.last_updated_date.isoformat()
        else:
            last_updated_date = self.last_updated_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if open_access_prohibited is not UNSET:
            field_dict["openAccessProhibited"] = open_access_prohibited
        if open_access_permissions is not UNSET:
            field_dict["openAccessPermissions"] = open_access_permissions
        if publisher_policies is not UNSET:
            field_dict["publisherPolicies"] = publisher_policies
        if sherpa_romeo_uri is not UNSET:
            field_dict["sherpaRomeoUri"] = sherpa_romeo_uri
        if last_updated_date is not UNSET:
            field_dict["lastUpdatedDate"] = last_updated_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sherpa_romeo_open_access_permission_type_0 import (
            SherpaRomeoOpenAccessPermissionType0,
        )

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        open_access_prohibited = d.pop("openAccessProhibited", UNSET)

        def _parse_open_access_permissions(
            data: object,
        ) -> list[None | SherpaRomeoOpenAccessPermissionType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                open_access_permissions_type_0 = []
                _open_access_permissions_type_0 = data
                for (
                    open_access_permissions_type_0_item_data
                ) in _open_access_permissions_type_0:

                    def _parse_open_access_permissions_type_0_item(
                        data: object,
                    ) -> None | SherpaRomeoOpenAccessPermissionType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_sherpa_romeo_open_access_permission_type_0 = SherpaRomeoOpenAccessPermissionType0.from_dict(
                                data
                            )

                            return componentsschemas_sherpa_romeo_open_access_permission_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | SherpaRomeoOpenAccessPermissionType0, data)

                    open_access_permissions_type_0_item = (
                        _parse_open_access_permissions_type_0_item(
                            open_access_permissions_type_0_item_data
                        )
                    )

                    open_access_permissions_type_0.append(
                        open_access_permissions_type_0_item
                    )

                return open_access_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | SherpaRomeoOpenAccessPermissionType0] | None | Unset, data
            )

        open_access_permissions = _parse_open_access_permissions(
            d.pop("openAccessPermissions", UNSET)
        )

        def _parse_publisher_policies(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                publisher_policies_type_0 = []
                _publisher_policies_type_0 = data
                for publisher_policies_type_0_item_data in _publisher_policies_type_0:

                    def _parse_publisher_policies_type_0_item(
                        data: object,
                    ) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    publisher_policies_type_0_item = (
                        _parse_publisher_policies_type_0_item(
                            publisher_policies_type_0_item_data
                        )
                    )

                    publisher_policies_type_0.append(publisher_policies_type_0_item)

                return publisher_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        publisher_policies = _parse_publisher_policies(
            d.pop("publisherPolicies", UNSET)
        )

        def _parse_sherpa_romeo_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sherpa_romeo_uri = _parse_sherpa_romeo_uri(d.pop("sherpaRomeoUri", UNSET))

        def _parse_last_updated_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_date_type_0 = isoparse(data)

                return last_updated_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_updated_date = _parse_last_updated_date(d.pop("lastUpdatedDate", UNSET))

        sherpa_romeo_policy = cls(
            pure_id=pure_id,
            open_access_prohibited=open_access_prohibited,
            open_access_permissions=open_access_permissions,
            publisher_policies=publisher_policies,
            sherpa_romeo_uri=sherpa_romeo_uri,
            last_updated_date=last_updated_date,
        )

        sherpa_romeo_policy.additional_properties = d
        return sherpa_romeo_policy

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
