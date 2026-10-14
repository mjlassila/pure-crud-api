from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.image_file_file_store_locations import ImageFileFileStoreLocations
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.remote_file import RemoteFile
    from ..models.uploaded_file import UploadedFile


T = TypeVar("T", bound="ImageFile")


@_attrs_define
class ImageFile:
    """An image file

    Attributes:
        file_name (str): The documents file name
        mime_type (str): The documents mime type
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        file_id (str | Unset): The id of the file
        size (int | Unset): The documents size in bytes
        url (str | Unset): Download url for the binary file
        file_store_locations (ImageFileFileStoreLocations | Unset): Locations of the binary file in file stores.
        uploaded_file (UploadedFile | Unset): Information about the uploaded file
        remote_file (RemoteFile | Unset): Information about a remote file (Elsevier only)
        file_data (str | Unset): Base64 encoded file data for new files. This property can be used instead of
            uploadedFile for small files
        type_ (ClassificationRefType0 | None | Unset): A reference to a classification value
        copyright_confirmation (bool | None | Unset): Indicates whether this file has been confirmed to adhere to the
            appropriate copyrights
        caption (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        alt_text (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        copyright_statement (LocalizedStringType0 | None | Unset): A set of string values, one for each submission
            locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
    """

    file_name: str
    mime_type: str
    pure_id: int | Unset = UNSET
    file_id: str | Unset = UNSET
    size: int | Unset = UNSET
    url: str | Unset = UNSET
    file_store_locations: ImageFileFileStoreLocations | Unset = UNSET
    uploaded_file: UploadedFile | Unset = UNSET
    remote_file: RemoteFile | Unset = UNSET
    file_data: str | Unset = UNSET
    type_: ClassificationRefType0 | None | Unset = UNSET
    copyright_confirmation: bool | None | Unset = UNSET
    caption: LocalizedStringType0 | None | Unset = UNSET
    alt_text: LocalizedStringType0 | None | Unset = UNSET
    copyright_statement: LocalizedStringType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0

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

        copyright_confirmation: bool | None | Unset
        if isinstance(self.copyright_confirmation, Unset):
            copyright_confirmation = UNSET
        else:
            copyright_confirmation = self.copyright_confirmation

        caption: dict[str, Any] | None | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        elif isinstance(self.caption, LocalizedStringType0):
            caption = self.caption.to_dict()
        else:
            caption = self.caption

        alt_text: dict[str, Any] | None | Unset
        if isinstance(self.alt_text, Unset):
            alt_text = UNSET
        elif isinstance(self.alt_text, LocalizedStringType0):
            alt_text = self.alt_text.to_dict()
        else:
            alt_text = self.alt_text

        copyright_statement: dict[str, Any] | None | Unset
        if isinstance(self.copyright_statement, Unset):
            copyright_statement = UNSET
        elif isinstance(self.copyright_statement, LocalizedStringType0):
            copyright_statement = self.copyright_statement.to_dict()
        else:
            copyright_statement = self.copyright_statement

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
        if copyright_confirmation is not UNSET:
            field_dict["copyrightConfirmation"] = copyright_confirmation
        if caption is not UNSET:
            field_dict["caption"] = caption
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text
        if copyright_statement is not UNSET:
            field_dict["copyrightStatement"] = copyright_statement

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.image_file_file_store_locations import ImageFileFileStoreLocations
        from ..models.localized_string_type_0 import LocalizedStringType0
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
        file_store_locations: ImageFileFileStoreLocations | Unset
        if isinstance(_file_store_locations, Unset):
            file_store_locations = UNSET
        else:
            file_store_locations = ImageFileFileStoreLocations.from_dict(
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

        def _parse_copyright_confirmation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copyright_confirmation = _parse_copyright_confirmation(
            d.pop("copyrightConfirmation", UNSET)
        )

        def _parse_caption(data: object) -> LocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_localized_string_type_0 = (
                    LocalizedStringType0.from_dict(data)
                )

                return componentsschemas_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedStringType0 | None | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_alt_text(data: object) -> LocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_localized_string_type_0 = (
                    LocalizedStringType0.from_dict(data)
                )

                return componentsschemas_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedStringType0 | None | Unset, data)

        alt_text = _parse_alt_text(d.pop("altText", UNSET))

        def _parse_copyright_statement(
            data: object,
        ) -> LocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_localized_string_type_0 = (
                    LocalizedStringType0.from_dict(data)
                )

                return componentsschemas_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedStringType0 | None | Unset, data)

        copyright_statement = _parse_copyright_statement(
            d.pop("copyrightStatement", UNSET)
        )

        image_file = cls(
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
            copyright_confirmation=copyright_confirmation,
            caption=caption,
            alt_text=alt_text,
            copyright_statement=copyright_statement,
        )

        image_file.additional_properties = d
        return image_file

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
