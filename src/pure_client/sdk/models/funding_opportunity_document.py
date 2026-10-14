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
    from ..models.funding_opportunity_document_file_store_locations import (
        FundingOpportunityDocumentFileStoreLocations,
    )
    from ..models.remote_file import RemoteFile
    from ..models.uploaded_file import UploadedFile
    from ..models.visibility import Visibility


T = TypeVar("T", bound="FundingOpportunityDocument")


@_attrs_define
class FundingOpportunityDocument:
    """Funding Opportunity document

    Attributes:
        file_name (str): The documents file name
        mime_type (str): The documents mime type
        type_ (ClassificationRefType0 | None): A reference to a classification value
        visibility (Visibility): Visibility of an object
        version_type (ClassificationRefType0 | None): A reference to a classification value
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        file_id (str | Unset): The id of the file
        size (int | Unset): The documents size in bytes
        url (str | Unset): Download url for the binary file
        file_store_locations (FundingOpportunityDocumentFileStoreLocations | Unset): Locations of the binary file in
            file stores.
        uploaded_file (UploadedFile | Unset): Information about the uploaded file
        remote_file (RemoteFile | Unset): Information about a remote file (Elsevier only)
        file_data (str | Unset): Base64 encoded file data for new files. This property can be used instead of
            uploadedFile for small files
        title (None | str | Unset): Document title
        license_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        visible_on_portal_date (datetime.date | Unset): The date the document will be available on the portal
        creator (str | Unset): The user that created the document
        created (datetime.datetime | Unset): Create date for the document
    """

    file_name: str
    mime_type: str
    type_: ClassificationRefType0 | None
    visibility: Visibility
    version_type: ClassificationRefType0 | None
    pure_id: int | Unset = UNSET
    file_id: str | Unset = UNSET
    size: int | Unset = UNSET
    url: str | Unset = UNSET
    file_store_locations: FundingOpportunityDocumentFileStoreLocations | Unset = UNSET
    uploaded_file: UploadedFile | Unset = UNSET
    remote_file: RemoteFile | Unset = UNSET
    file_data: str | Unset = UNSET
    title: None | str | Unset = UNSET
    license_: ClassificationRefType0 | None | Unset = UNSET
    visible_on_portal_date: datetime.date | Unset = UNSET
    creator: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        file_name = self.file_name

        mime_type = self.mime_type

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        visibility = self.visibility.to_dict()

        version_type: dict[str, Any] | None
        if isinstance(self.version_type, ClassificationRefType0):
            version_type = self.version_type.to_dict()
        else:
            version_type = self.version_type

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

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        license_: dict[str, Any] | None | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        elif isinstance(self.license_, ClassificationRefType0):
            license_ = self.license_.to_dict()
        else:
            license_ = self.license_

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
                "fileName": file_name,
                "mimeType": mime_type,
                "type": type_,
                "visibility": visibility,
                "versionType": version_type,
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
        if title is not UNSET:
            field_dict["title"] = title
        if license_ is not UNSET:
            field_dict["license"] = license_
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
        from ..models.funding_opportunity_document_file_store_locations import (
            FundingOpportunityDocumentFileStoreLocations,
        )
        from ..models.remote_file import RemoteFile
        from ..models.uploaded_file import UploadedFile
        from ..models.visibility import Visibility

        d = dict(src_dict)
        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        def _parse_type_(data: object) -> ClassificationRefType0 | None:
            if data is None:
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
            return cast(ClassificationRefType0 | None, data)

        type_ = _parse_type_(d.pop("type"))

        visibility = Visibility.from_dict(d.pop("visibility"))

        def _parse_version_type(data: object) -> ClassificationRefType0 | None:
            if data is None:
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
            return cast(ClassificationRefType0 | None, data)

        version_type = _parse_version_type(d.pop("versionType"))

        pure_id = d.pop("pureId", UNSET)

        file_id = d.pop("fileId", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        _file_store_locations = d.pop("fileStoreLocations", UNSET)
        file_store_locations: FundingOpportunityDocumentFileStoreLocations | Unset
        if isinstance(_file_store_locations, Unset):
            file_store_locations = UNSET
        else:
            file_store_locations = (
                FundingOpportunityDocumentFileStoreLocations.from_dict(
                    _file_store_locations
                )
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

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_license_(data: object) -> ClassificationRefType0 | None | Unset:
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

        license_ = _parse_license_(d.pop("license", UNSET))

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

        funding_opportunity_document = cls(
            file_name=file_name,
            mime_type=mime_type,
            type_=type_,
            visibility=visibility,
            version_type=version_type,
            pure_id=pure_id,
            file_id=file_id,
            size=size,
            url=url,
            file_store_locations=file_store_locations,
            uploaded_file=uploaded_file,
            remote_file=remote_file,
            file_data=file_data,
            title=title,
            license_=license_,
            visible_on_portal_date=visible_on_portal_date,
            creator=creator,
            created=created,
        )

        funding_opportunity_document.additional_properties = d
        return funding_opportunity_document

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
