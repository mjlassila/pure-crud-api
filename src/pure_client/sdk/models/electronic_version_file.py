from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.electronic_version_file_file_store_locations import (
        ElectronicVersionFileFileStoreLocations,
    )
    from ..models.remote_file import RemoteFile
    from ..models.uploaded_file import UploadedFile


T = TypeVar("T", bound="ElectronicVersionFile")


@_attrs_define
class ElectronicVersionFile:
    """Information about an electronic version file

    Attributes:
        file_name (str): The documents file name
        mime_type (str): The documents mime type
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        file_id (str | Unset): The id of the file
        size (int | Unset): The documents size in bytes
        url (str | Unset): Download url for the binary file
        file_store_locations (ElectronicVersionFileFileStoreLocations | Unset): Locations of the binary file in file
            stores.
        uploaded_file (UploadedFile | Unset): Information about the uploaded file
        remote_file (RemoteFile | Unset): Information about a remote file (Elsevier only)
        file_data (str | Unset): Base64 encoded file data for new files. This property can be used instead of
            uploadedFile for small files
    """

    file_name: str
    mime_type: str
    pure_id: int | Unset = UNSET
    file_id: str | Unset = UNSET
    size: int | Unset = UNSET
    url: str | Unset = UNSET
    file_store_locations: ElectronicVersionFileFileStoreLocations | Unset = UNSET
    uploaded_file: UploadedFile | Unset = UNSET
    remote_file: RemoteFile | Unset = UNSET
    file_data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        mime_type = self.mime_type

        pure_id = self.pure_id

        file_id = self.file_id

        size = self.size

        url = self.url

        file_store_locations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_store_locations, Unset):
            file_store_locations = self.file_store_locations.to_dict()

        uploaded_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uploaded_file, Unset):
            uploaded_file = self.uploaded_file.to_dict()

        remote_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_file, Unset):
            remote_file = self.remote_file.to_dict()

        file_data = self.file_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "mimeType": mime_type,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if size is not UNSET:
            field_dict["size"] = size
        if url is not UNSET:
            field_dict["url"] = url
        if file_store_locations is not UNSET:
            field_dict["fileStoreLocations"] = file_store_locations
        if uploaded_file is not UNSET:
            field_dict["uploadedFile"] = uploaded_file
        if remote_file is not UNSET:
            field_dict["remoteFile"] = remote_file
        if file_data is not UNSET:
            field_dict["fileData"] = file_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.electronic_version_file_file_store_locations import (
            ElectronicVersionFileFileStoreLocations,
        )
        from ..models.remote_file import RemoteFile
        from ..models.uploaded_file import UploadedFile

        d = dict(src_dict)
        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        pure_id = d.pop("pureId", UNSET)

        file_id = d.pop("fileId", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        _file_store_locations = d.pop("fileStoreLocations", UNSET)
        file_store_locations: ElectronicVersionFileFileStoreLocations | Unset
        if isinstance(_file_store_locations, Unset):
            file_store_locations = UNSET
        else:
            file_store_locations = ElectronicVersionFileFileStoreLocations.from_dict(
                _file_store_locations
            )

        _uploaded_file = d.pop("uploadedFile", UNSET)
        uploaded_file: UploadedFile | Unset
        if isinstance(_uploaded_file, Unset):
            uploaded_file = UNSET
        else:
            uploaded_file = UploadedFile.from_dict(_uploaded_file)

        _remote_file = d.pop("remoteFile", UNSET)
        remote_file: RemoteFile | Unset
        if isinstance(_remote_file, Unset):
            remote_file = UNSET
        else:
            remote_file = RemoteFile.from_dict(_remote_file)

        file_data = d.pop("fileData", UNSET)

        electronic_version_file = cls(
            file_name=file_name,
            mime_type=mime_type,
            pure_id=pure_id,
            file_id=file_id,
            size=size,
            url=url,
            file_store_locations=file_store_locations,
            uploaded_file=uploaded_file,
            remote_file=remote_file,
            file_data=file_data,
        )

        electronic_version_file.additional_properties = d
        return electronic_version_file

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
