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
    from ..models.document import Document


T = TypeVar("T", bound="ApplicationStatus")


@_attrs_define
class ApplicationStatus:
    """A representation of a point in time when the status of an application changed, e.g. the submitted to funder date or
    awarded by funder date of the application.

        Attributes:
            date (datetime.date): The date of the application status.
            status (ClassificationRefType0 | None): A reference to a classification value
            pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
            documents (list[Document] | None | Unset): Related documents of the application status.
            current (bool | Unset): Whether this element reflects the current application status.
    """

    date: datetime.date
    status: ClassificationRefType0 | None
    pure_id: int | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    current: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        date = self.date.isoformat()

        status: dict[str, Any] | None
        if isinstance(self.status, ClassificationRefType0):
            status = self.status.to_dict()
        else:
            status = self.status

        pure_id = self.pure_id

        documents: list[dict[str, Any]] | None | Unset
        if isinstance(self.documents, Unset):
            documents = UNSET
        elif isinstance(self.documents, list):
            documents = []
            for documents_type_0_item_data in self.documents:
                documents_type_0_item = documents_type_0_item_data.to_dict()
                documents.append(documents_type_0_item)

        else:
            documents = self.documents

        current = self.current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "status": status,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if documents is not UNSET:
            field_dict["documents"] = documents
        if current is not UNSET:
            field_dict["current"] = current

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.document import Document

        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        def _parse_status(data: object) -> ClassificationRefType0 | None:
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

        status = _parse_status(d.pop("status"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_documents(data: object) -> list[Document] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                documents_type_0 = []
                _documents_type_0 = data
                for documents_type_0_item_data in _documents_type_0:
                    documents_type_0_item = Document.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Document] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

        current = d.pop("current", UNSET)

        application_status = cls(
            date=date,
            status=status,
            pure_id=pure_id,
            documents=documents,
            current=current,
        )

        application_status.additional_properties = d
        return application_status

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
