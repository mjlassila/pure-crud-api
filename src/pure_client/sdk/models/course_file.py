from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.course_file_file_store_locations import CourseFileFileStoreLocations
    from ..models.date_range import DateRange
    from ..models.remote_file import RemoteFile
    from ..models.uploaded_file import UploadedFile


T = TypeVar("T", bound="CourseFile")


@_attrs_define
class CourseFile:
    """A file related to a course

    Attributes:
        file_name (str): The documents file name
        mime_type (str): The documents mime type
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        file_id (str | Unset): The id of the file
        size (int | Unset): The documents size in bytes
        url (str | Unset): Download url for the binary file
        file_store_locations (CourseFileFileStoreLocations | Unset): Locations of the binary file in file stores.
        uploaded_file (UploadedFile | Unset): Information about the uploaded file
        remote_file (RemoteFile | Unset): Information about a remote file (Elsevier only)
        file_data (str | Unset): Base64 encoded file data for new files. This property can be used instead of
            uploadedFile for small files
        type_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        title (None | str | Unset): A human readable name of the related file
        license_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        access_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        embargo_period (DateRange | Unset): A date range
    """

    file_name: str
    mime_type: str
    pure_id: int | Unset = UNSET
    file_id: str | Unset = UNSET
    size: int | Unset = UNSET
    url: str | Unset = UNSET
    file_store_locations: CourseFileFileStoreLocations | Unset = UNSET
    uploaded_file: UploadedFile | Unset = UNSET
    remote_file: RemoteFile | Unset = UNSET
    file_data: str | Unset = UNSET
    type_: ClassificationRefType0 | None | Unset = UNSET
    title: None | str | Unset = UNSET
    license_type: ClassificationRefType0 | None | Unset = UNSET
    access_type: ClassificationRefType0 | None | Unset = UNSET
    embargo_period: DateRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

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

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        license_type: dict[str, Any] | None | Unset
        if isinstance(self.license_type, Unset):
            license_type = UNSET
        elif isinstance(self.license_type, ClassificationRefType0):
            license_type = self.license_type.to_dict()
        else:
            license_type = self.license_type

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if embargo_period is not UNSET:
            field_dict["embargoPeriod"] = embargo_period

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.course_file_file_store_locations import (
            CourseFileFileStoreLocations,
        )
        from ..models.date_range import DateRange
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
        file_store_locations: CourseFileFileStoreLocations | Unset
        if isinstance(_file_store_locations, Unset):
            file_store_locations = UNSET
        else:
            file_store_locations = CourseFileFileStoreLocations.from_dict(
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

        def _parse_type_(data: object) -> ClassificationRefType0 | None | Unset:
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

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        course_file = cls(
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
            type_=type_,
            title=title,
            license_type=license_type,
            access_type=access_type,
            embargo_period=embargo_period,
        )

        course_file.additional_properties = d
        return course_file

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
