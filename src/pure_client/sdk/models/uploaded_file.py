from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadedFile")


@_attrs_define
class UploadedFile:
    """Information about the uploaded file

    Attributes:
        key (str): Pure key identifer for the file upload
        digest (str | Unset): The calculated digest for the file in Pure
        digest_type (str | Unset): The digest type
        size (int | Unset): The file size of the file in Pure
        mime_type (str | Unset): The mime type detected for the file
        time_stamp (datetime.datetime | Unset): The timestamp Pure received the file
        expires (datetime.datetime | Unset): The timestamp where Pure deletes the uploaded file if it has not been
            attached to any content
    """

    key: str
    digest: str | Unset = UNSET
    digest_type: str | Unset = UNSET
    size: int | Unset = UNSET
    mime_type: str | Unset = UNSET
    time_stamp: datetime.datetime | Unset = UNSET
    expires: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        digest = self.digest

        digest_type = self.digest_type

        size = self.size

        mime_type = self.mime_type

        time_stamp: str | Unset = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        expires: str | Unset = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if digest is not UNSET:
            field_dict["digest"] = digest
        if digest_type is not UNSET:
            field_dict["digestType"] = digest_type
        if size is not UNSET:
            field_dict["size"] = size
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        digest = d.pop("digest", UNSET)

        digest_type = d.pop("digestType", UNSET)

        size = d.pop("size", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        _time_stamp = d.pop("timeStamp", UNSET)
        time_stamp: datetime.datetime | Unset
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = isoparse(_time_stamp)

        _expires = d.pop("expires", UNSET)
        expires: datetime.datetime | Unset
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        uploaded_file = cls(
            key=key,
            digest=digest,
            digest_type=digest_type,
            size=size,
            mime_type=mime_type,
            time_stamp=time_stamp,
            expires=expires,
        )

        uploaded_file.additional_properties = d
        return uploaded_file

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
