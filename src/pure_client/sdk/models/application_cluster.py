from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.application_cluster_status import ApplicationClusterStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_ref_type_0 import ApplicationRefType0
    from ..models.project_ref_type_0 import ProjectRefType0


T = TypeVar("T", bound="ApplicationCluster")


@_attrs_define
class ApplicationCluster:
    """An application cluster groups related applications from their individual relations.

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        uuid (UUID | Unset): UUID, this is the primary identity of the entity
        created_by (str | Unset): Username of creator
        created_date (datetime.datetime | Unset): Date and time of creation
        modified_by (str | Unset): Username of the user that performed a modification
        modified_date (datetime.datetime | Unset): Date and time of last modification
        portal_url (str | Unset): URL of the content on the Pure Portal
        pretty_url_identifiers (list[str] | Unset): All pretty URLs
        previous_uuids (list[str] | Unset): UUIDs of other content items which have been merged into this content item
            (or similar)
        version (None | str | Unset): Used to guard against conflicting updates. For new content this is null, and for
            existing content the current value. The property should never be modified by a client, except in the rare case
            where the client wants to perform an update irrespective of if other clients have made updates in the meantime,
            also known as a "dirty write". A dirty write is performed by not including the property value or setting the
            property to null
        title (str | Unset): The title of the application cluster.
        contained_applications (list[ApplicationRefType0 | None] | Unset): The applications grouped in the application
            cluster. Applications are automatically added when related to other applications in this cluster.
        project (None | ProjectRefType0 | Unset): A reference to project
        status (ApplicationClusterStatus | Unset): Application cluster status value
        date_of_status_change (datetime.date | Unset): The date of the last status change of the application cluster.
        system_name (str | Unset): The content system name
    """

    pure_id: int | Unset = UNSET
    uuid: UUID | Unset = UNSET
    created_by: str | Unset = UNSET
    created_date: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    portal_url: str | Unset = UNSET
    pretty_url_identifiers: list[str] | Unset = UNSET
    previous_uuids: list[str] | Unset = UNSET
    version: None | str | Unset = UNSET
    title: str | Unset = UNSET
    contained_applications: list[ApplicationRefType0 | None] | Unset = UNSET
    project: None | ProjectRefType0 | Unset = UNSET
    status: ApplicationClusterStatus | Unset = UNSET
    date_of_status_change: datetime.date | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.project_ref_type_0 import ProjectRefType0

        pure_id = self.pure_id

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        created_by = self.created_by

        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        modified_by = self.modified_by

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        portal_url = self.portal_url

        pretty_url_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pretty_url_identifiers, Unset):
            pretty_url_identifiers = self.pretty_url_identifiers

        previous_uuids: list[str] | Unset = UNSET
        if not isinstance(self.previous_uuids, Unset):
            previous_uuids = self.previous_uuids

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        title = self.title

        contained_applications: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.contained_applications, Unset):
            contained_applications = []
            for contained_applications_item_data in self.contained_applications:
                contained_applications_item: dict[str, Any] | None
                if isinstance(contained_applications_item_data, ApplicationRefType0):
                    contained_applications_item = (
                        contained_applications_item_data.to_dict()
                    )
                else:
                    contained_applications_item = contained_applications_item_data
                contained_applications.append(contained_applications_item)

        project: dict[str, Any] | None | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, ProjectRefType0):
            project = self.project.to_dict()
        else:
            project = self.project

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        date_of_status_change: str | Unset = UNSET
        if not isinstance(self.date_of_status_change, Unset):
            date_of_status_change = self.date_of_status_change.isoformat()

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if portal_url is not UNSET:
            field_dict["portalUrl"] = portal_url
        if pretty_url_identifiers is not UNSET:
            field_dict["prettyUrlIdentifiers"] = pretty_url_identifiers
        if previous_uuids is not UNSET:
            field_dict["previousUuids"] = previous_uuids
        if version is not UNSET:
            field_dict["version"] = version
        if title is not UNSET:
            field_dict["title"] = title
        if contained_applications is not UNSET:
            field_dict["containedApplications"] = contained_applications
        if project is not UNSET:
            field_dict["project"] = project
        if status is not UNSET:
            field_dict["status"] = status
        if date_of_status_change is not UNSET:
            field_dict["dateOfStatusChange"] = date_of_status_change
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.project_ref_type_0 import ProjectRefType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        created_by = d.pop("createdBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        modified_by = d.pop("modifiedBy", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        portal_url = d.pop("portalUrl", UNSET)

        pretty_url_identifiers = cast(list[str], d.pop("prettyUrlIdentifiers", UNSET))

        previous_uuids = cast(list[str], d.pop("previousUuids", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        title = d.pop("title", UNSET)

        _contained_applications = d.pop("containedApplications", UNSET)
        contained_applications: list[ApplicationRefType0 | None] | Unset = UNSET
        if _contained_applications is not UNSET:
            contained_applications = []
            for contained_applications_item_data in _contained_applications:

                def _parse_contained_applications_item(
                    data: object,
                ) -> ApplicationRefType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_application_ref_type_0 = (
                            ApplicationRefType0.from_dict(data)
                        )

                        return componentsschemas_application_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(ApplicationRefType0 | None, data)

                contained_applications_item = _parse_contained_applications_item(
                    contained_applications_item_data
                )

                contained_applications.append(contained_applications_item)

        def _parse_project(data: object) -> None | ProjectRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_project_ref_type_0 = ProjectRefType0.from_dict(data)

                return componentsschemas_project_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProjectRefType0 | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        _status = d.pop("status", UNSET)
        status: ApplicationClusterStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApplicationClusterStatus(_status)

        _date_of_status_change = d.pop("dateOfStatusChange", UNSET)
        date_of_status_change: datetime.date | Unset
        if isinstance(_date_of_status_change, Unset):
            date_of_status_change = UNSET
        else:
            date_of_status_change = isoparse(_date_of_status_change).date()

        system_name = d.pop("systemName", UNSET)

        application_cluster = cls(
            pure_id=pure_id,
            uuid=uuid,
            created_by=created_by,
            created_date=created_date,
            modified_by=modified_by,
            modified_date=modified_date,
            portal_url=portal_url,
            pretty_url_identifiers=pretty_url_identifiers,
            previous_uuids=previous_uuids,
            version=version,
            title=title,
            contained_applications=contained_applications,
            project=project,
            status=status,
            date_of_status_change=date_of_status_change,
            system_name=system_name,
        )

        application_cluster.additional_properties = d
        return application_cluster

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
