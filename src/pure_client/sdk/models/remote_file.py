from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.remote_file_file_state import RemoteFileFileState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteFile")


@_attrs_define
class RemoteFile:
    """Information about a remote file (Elsevier only)

    Attributes:
        source_id (str): The remote source ID
        store_name (str): The name of the remote store
        file_id (str): The remote file ID
        file_state (RemoteFileFileState): The remote file state
        time_stamp (datetime.datetime | Unset): The timestamp at which the file was stored
        metadata_update_required (bool | Unset): Whether the file's metadata should be updated Default: False.
    """

    source_id: str
    store_name: str
    file_id: str
    file_state: RemoteFileFileState
    time_stamp: datetime.datetime | Unset = UNSET
    metadata_update_required: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_id = self.source_id

        store_name = self.store_name

        file_id = self.file_id

        file_state = self.file_state.value

        time_stamp: str | Unset = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        metadata_update_required = self.metadata_update_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceId": source_id,
                "storeName": store_name,
                "fileId": file_id,
                "fileState": file_state,
            }
        )
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if metadata_update_required is not UNSET:
            field_dict["metadataUpdateRequired"] = metadata_update_required

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_id = d.pop("sourceId")

        store_name = d.pop("storeName")

        file_id = d.pop("fileId")

        file_state = RemoteFileFileState(d.pop("fileState"))

        _time_stamp = d.pop("timeStamp", UNSET)
        time_stamp: datetime.datetime | Unset
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = isoparse(_time_stamp)

        metadata_update_required = d.pop("metadataUpdateRequired", UNSET)

        remote_file = cls(
            source_id=source_id,
            store_name=store_name,
            file_id=file_id,
            file_state=file_state,
            time_stamp=time_stamp,
            metadata_update_required=metadata_update_required,
        )

        remote_file.additional_properties = d
        return remote_file

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
