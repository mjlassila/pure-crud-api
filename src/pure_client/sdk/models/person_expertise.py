from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.person_ref_type_0 import PersonRefType0
    from ..models.workflow import Workflow


T = TypeVar("T", bound="PersonExpertise")


@_attrs_define
class PersonExpertise:
    """The expertise of the person.

    Attributes:
        type_ (ClassificationRefType0 | None): A reference to a classification value
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
        workflow (Workflow | Unset): Information about workflow
        area_of_expertise (list[str] | None | Unset): A collection of area of expertise.
        area_of_expertise_classifications (list[ClassificationRefType0 | None] | None | Unset): A collection of area of
            expertise classifications.
        willingness_to_media (bool | None | Unset): Indicates willingness to media.
        moderated_willingness_to_media (bool | None | Unset): Indicates moderated willingness to media.
        person (None | PersonRefType0 | Unset): A reference to a person internal to the institution
        system_name (str | Unset): The content system name
    """

    type_: ClassificationRefType0 | None
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
    workflow: Workflow | Unset = UNSET
    area_of_expertise: list[str] | None | Unset = UNSET
    area_of_expertise_classifications: (
        list[ClassificationRefType0 | None] | None | Unset
    ) = UNSET
    willingness_to_media: bool | None | Unset = UNSET
    moderated_willingness_to_media: bool | None | Unset = UNSET
    person: None | PersonRefType0 | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        area_of_expertise: list[str] | None | Unset
        if isinstance(self.area_of_expertise, Unset):
            area_of_expertise = UNSET
        elif isinstance(self.area_of_expertise, list):
            area_of_expertise = self.area_of_expertise

        else:
            area_of_expertise = self.area_of_expertise

        area_of_expertise_classifications: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.area_of_expertise_classifications, Unset):
            area_of_expertise_classifications = UNSET
        elif isinstance(self.area_of_expertise_classifications, list):
            area_of_expertise_classifications = []
            for (
                area_of_expertise_classifications_type_0_item_data
            ) in self.area_of_expertise_classifications:
                area_of_expertise_classifications_type_0_item: dict[str, Any] | None
                if isinstance(
                    area_of_expertise_classifications_type_0_item_data,
                    ClassificationRefType0,
                ):
                    area_of_expertise_classifications_type_0_item = (
                        area_of_expertise_classifications_type_0_item_data.to_dict()
                    )
                else:
                    area_of_expertise_classifications_type_0_item = (
                        area_of_expertise_classifications_type_0_item_data
                    )
                area_of_expertise_classifications.append(
                    area_of_expertise_classifications_type_0_item
                )

        else:
            area_of_expertise_classifications = self.area_of_expertise_classifications

        willingness_to_media: bool | None | Unset
        if isinstance(self.willingness_to_media, Unset):
            willingness_to_media = UNSET
        else:
            willingness_to_media = self.willingness_to_media

        moderated_willingness_to_media: bool | None | Unset
        if isinstance(self.moderated_willingness_to_media, Unset):
            moderated_willingness_to_media = UNSET
        else:
            moderated_willingness_to_media = self.moderated_willingness_to_media

        person: dict[str, Any] | None | Unset
        if isinstance(self.person, Unset):
            person = UNSET
        elif isinstance(self.person, PersonRefType0):
            person = self.person.to_dict()
        else:
            person = self.person

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
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
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if area_of_expertise is not UNSET:
            field_dict["areaOfExpertise"] = area_of_expertise
        if area_of_expertise_classifications is not UNSET:
            field_dict["areaOfExpertiseClassifications"] = (
                area_of_expertise_classifications
            )
        if willingness_to_media is not UNSET:
            field_dict["willingnessToMedia"] = willingness_to_media
        if moderated_willingness_to_media is not UNSET:
            field_dict["moderatedWillingnessToMedia"] = moderated_willingness_to_media
        if person is not UNSET:
            field_dict["person"] = person
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.person_ref_type_0 import PersonRefType0
        from ..models.workflow import Workflow

        d = dict(src_dict)

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

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        def _parse_area_of_expertise(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                area_of_expertise_type_0 = cast(list[str], data)

                return area_of_expertise_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        area_of_expertise = _parse_area_of_expertise(d.pop("areaOfExpertise", UNSET))

        def _parse_area_of_expertise_classifications(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                area_of_expertise_classifications_type_0 = []
                _area_of_expertise_classifications_type_0 = data
                for (
                    area_of_expertise_classifications_type_0_item_data
                ) in _area_of_expertise_classifications_type_0:

                    def _parse_area_of_expertise_classifications_type_0_item(
                        data: object,
                    ) -> ClassificationRefType0 | None:
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

                    area_of_expertise_classifications_type_0_item = (
                        _parse_area_of_expertise_classifications_type_0_item(
                            area_of_expertise_classifications_type_0_item_data
                        )
                    )

                    area_of_expertise_classifications_type_0.append(
                        area_of_expertise_classifications_type_0_item
                    )

                return area_of_expertise_classifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        area_of_expertise_classifications = _parse_area_of_expertise_classifications(
            d.pop("areaOfExpertiseClassifications", UNSET)
        )

        def _parse_willingness_to_media(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        willingness_to_media = _parse_willingness_to_media(
            d.pop("willingnessToMedia", UNSET)
        )

        def _parse_moderated_willingness_to_media(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        moderated_willingness_to_media = _parse_moderated_willingness_to_media(
            d.pop("moderatedWillingnessToMedia", UNSET)
        )

        def _parse_person(data: object) -> None | PersonRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_ref_type_0 = PersonRefType0.from_dict(data)

                return componentsschemas_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonRefType0 | Unset, data)

        person = _parse_person(d.pop("person", UNSET))

        system_name = d.pop("systemName", UNSET)

        person_expertise = cls(
            type_=type_,
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
            workflow=workflow,
            area_of_expertise=area_of_expertise,
            area_of_expertise_classifications=area_of_expertise_classifications,
            willingness_to_media=willingness_to_media,
            moderated_willingness_to_media=moderated_willingness_to_media,
            person=person,
            system_name=system_name,
        )

        person_expertise.additional_properties = d
        return person_expertise

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
