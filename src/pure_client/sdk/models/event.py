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
    from ..models.date_range import DateRange
    from ..models.event_ref_type_0 import EventRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.geo_location_type_0 import GeoLocationType0
    from ..models.identifier import Identifier
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """An event typically a conference, workshop or similar

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
        abbreviated_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support
            formatting. Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        geo_location (GeoLocationType0 | None | Unset): Geographical location
        city (None | str | Unset): The city of the event
        conference_number (None | str | Unset): The conference number of the event
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
        degree_of_recognition (ClassificationRefType0 | None | Unset): A reference to a classification value
        description (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present
        links (list[Link] | None | Unset): Links to information about the event
        location (None | str | Unset): The actual location of the event
        organizers (list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset): The organizers of the event
        lifecycle (DateRange | Unset): A date range
        events (list[EventRefType0 | None] | None | Unset): Other events related to this event
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
        sponsor_organizations (list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset): The event
            sponsors
        subdivision (ClassificationRefType0 | None | Unset): A reference to a classification value
        title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        sub_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        workflow (Workflow | Unset): Information about workflow
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
    abbreviated_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    geo_location: GeoLocationType0 | None | Unset = UNSET
    city: None | str | Unset = UNSET
    conference_number: None | str | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    degree_of_recognition: ClassificationRefType0 | None | Unset = UNSET
    description: FormattedLocalizedStringType0 | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    location: None | str | Unset = UNSET
    organizers: (
        list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset
    ) = UNSET
    lifecycle: DateRange | Unset = UNSET
    events: list[EventRefType0 | None] | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    sponsor_organizations: (
        list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset
    ) = UNSET
    subdivision: ClassificationRefType0 | None | Unset = UNSET
    title: FormattedLocalizedStringType0 | None | Unset = UNSET
    sub_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.geo_location_type_0 import GeoLocationType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

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

        abbreviated_title: dict[str, Any] | None | Unset
        if isinstance(self.abbreviated_title, Unset):
            abbreviated_title = UNSET
        elif isinstance(self.abbreviated_title, FormattedLocalizedStringType0):
            abbreviated_title = self.abbreviated_title.to_dict()
        else:
            abbreviated_title = self.abbreviated_title

        geo_location: dict[str, Any] | None | Unset
        if isinstance(self.geo_location, Unset):
            geo_location = UNSET
        elif isinstance(self.geo_location, GeoLocationType0):
            geo_location = self.geo_location.to_dict()
        else:
            geo_location = self.geo_location

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        conference_number: None | str | Unset
        if isinstance(self.conference_number, Unset):
            conference_number = UNSET
        else:
            conference_number = self.conference_number

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, ClassificationRefType0):
            country = self.country.to_dict()
        else:
            country = self.country

        degree_of_recognition: dict[str, Any] | None | Unset
        if isinstance(self.degree_of_recognition, Unset):
            degree_of_recognition = UNSET
        elif isinstance(self.degree_of_recognition, ClassificationRefType0):
            degree_of_recognition = self.degree_of_recognition.to_dict()
        else:
            degree_of_recognition = self.degree_of_recognition

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, FormattedLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        keyword_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyword_groups, Unset):
            keyword_groups = UNSET
        elif isinstance(self.keyword_groups, list):
            keyword_groups = []
            for keyword_groups_type_0_item_data in self.keyword_groups:
                keyword_groups_type_0_item = keyword_groups_type_0_item_data.to_dict()
                keyword_groups.append(keyword_groups_type_0_item)

        else:
            keyword_groups = self.keyword_groups

        links: list[dict[str, Any]] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        else:
            links = self.links

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        organizers: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.organizers, Unset):
            organizers = UNSET
        elif isinstance(self.organizers, list):
            organizers = []
            for organizers_type_0_item_data in self.organizers:
                organizers_type_0_item: dict[str, Any] | None
                if isinstance(
                    organizers_type_0_item_data,
                    OrganizationOrExternalOrganizationRefType0,
                ):
                    organizers_type_0_item = organizers_type_0_item_data.to_dict()
                else:
                    organizers_type_0_item = organizers_type_0_item_data
                organizers.append(organizers_type_0_item)

        else:
            organizers = self.organizers

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        events: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.events, Unset):
            events = UNSET
        elif isinstance(self.events, list):
            events = []
            for events_type_0_item_data in self.events:
                events_type_0_item: dict[str, Any] | None
                if isinstance(events_type_0_item_data, EventRefType0):
                    events_type_0_item = events_type_0_item_data.to_dict()
                else:
                    events_type_0_item = events_type_0_item_data
                events.append(events_type_0_item)

        else:
            events = self.events

        identifiers: list[dict[str, Any]] | None | Unset
        if isinstance(self.identifiers, Unset):
            identifiers = UNSET
        elif isinstance(self.identifiers, list):
            identifiers = []
            for identifiers_type_0_item_data in self.identifiers:
                identifiers_type_0_item = identifiers_type_0_item_data.to_dict()
                identifiers.append(identifiers_type_0_item)

        else:
            identifiers = self.identifiers

        sponsor_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.sponsor_organizations, Unset):
            sponsor_organizations = UNSET
        elif isinstance(self.sponsor_organizations, list):
            sponsor_organizations = []
            for sponsor_organizations_type_0_item_data in self.sponsor_organizations:
                sponsor_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    sponsor_organizations_type_0_item_data,
                    OrganizationOrExternalOrganizationRefType0,
                ):
                    sponsor_organizations_type_0_item = (
                        sponsor_organizations_type_0_item_data.to_dict()
                    )
                else:
                    sponsor_organizations_type_0_item = (
                        sponsor_organizations_type_0_item_data
                    )
                sponsor_organizations.append(sponsor_organizations_type_0_item)

        else:
            sponsor_organizations = self.sponsor_organizations

        subdivision: dict[str, Any] | None | Unset
        if isinstance(self.subdivision, Unset):
            subdivision = UNSET
        elif isinstance(self.subdivision, ClassificationRefType0):
            subdivision = self.subdivision.to_dict()
        else:
            subdivision = self.subdivision

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, FormattedLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        sub_title: dict[str, Any] | None | Unset
        if isinstance(self.sub_title, Unset):
            sub_title = UNSET
        elif isinstance(self.sub_title, FormattedLocalizedStringType0):
            sub_title = self.sub_title.to_dict()
        else:
            sub_title = self.sub_title

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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
        if abbreviated_title is not UNSET:
            field_dict["abbreviatedTitle"] = abbreviated_title
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if city is not UNSET:
            field_dict["city"] = city
        if conference_number is not UNSET:
            field_dict["conferenceNumber"] = conference_number
        if country is not UNSET:
            field_dict["country"] = country
        if degree_of_recognition is not UNSET:
            field_dict["degreeOfRecognition"] = degree_of_recognition
        if description is not UNSET:
            field_dict["description"] = description
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if links is not UNSET:
            field_dict["links"] = links
        if location is not UNSET:
            field_dict["location"] = location
        if organizers is not UNSET:
            field_dict["organizers"] = organizers
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if events is not UNSET:
            field_dict["events"] = events
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if sponsor_organizations is not UNSET:
            field_dict["sponsorOrganizations"] = sponsor_organizations
        if subdivision is not UNSET:
            field_dict["subdivision"] = subdivision
        if title is not UNSET:
            field_dict["title"] = title
        if sub_title is not UNSET:
            field_dict["subTitle"] = sub_title
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange
        from ..models.event_ref_type_0 import EventRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.geo_location_type_0 import GeoLocationType0
        from ..models.identifier import Identifier
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
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

        def _parse_abbreviated_title(
            data: object,
        ) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        abbreviated_title = _parse_abbreviated_title(d.pop("abbreviatedTitle", UNSET))

        def _parse_geo_location(data: object) -> GeoLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_geo_location_type_0 = GeoLocationType0.from_dict(data)

                return componentsschemas_geo_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GeoLocationType0 | None | Unset, data)

        geo_location = _parse_geo_location(d.pop("geoLocation", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_conference_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conference_number = _parse_conference_number(d.pop("conferenceNumber", UNSET))

        def _parse_country(data: object) -> ClassificationRefType0 | None | Unset:
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

        country = _parse_country(d.pop("country", UNSET))

        def _parse_degree_of_recognition(
            data: object,
        ) -> ClassificationRefType0 | None | Unset:
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

        degree_of_recognition = _parse_degree_of_recognition(
            d.pop("degreeOfRecognition", UNSET)
        )

        def _parse_description(
            data: object,
        ) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_keyword_groups(data: object) -> list[KeywordGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyword_groups_type_0 = []
                _keyword_groups_type_0 = data
                for keyword_groups_type_0_item_data in _keyword_groups_type_0:
                    keyword_groups_type_0_item = KeywordGroup.from_dict(
                        keyword_groups_type_0_item_data
                    )

                    keyword_groups_type_0.append(keyword_groups_type_0_item)

                return keyword_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeywordGroup] | None | Unset, data)

        keyword_groups = _parse_keyword_groups(d.pop("keywordGroups", UNSET))

        def _parse_links(data: object) -> list[Link] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = Link.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Link] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_organizers(
            data: object,
        ) -> list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizers_type_0 = []
                _organizers_type_0 = data
                for organizers_type_0_item_data in _organizers_type_0:

                    def _parse_organizers_type_0_item(
                        data: object,
                    ) -> None | OrganizationOrExternalOrganizationRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_organization_or_external_organization_ref_type_0 = OrganizationOrExternalOrganizationRefType0.from_dict(
                                data
                            )

                            return componentsschemas_organization_or_external_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | OrganizationOrExternalOrganizationRefType0, data
                        )

                    organizers_type_0_item = _parse_organizers_type_0_item(
                        organizers_type_0_item_data
                    )

                    organizers_type_0.append(organizers_type_0_item)

                return organizers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset,
                data,
            )

        organizers = _parse_organizers(d.pop("organizers", UNSET))

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: DateRange | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = DateRange.from_dict(_lifecycle)

        def _parse_events(data: object) -> list[EventRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = []
                _events_type_0 = data
                for events_type_0_item_data in _events_type_0:

                    def _parse_events_type_0_item(data: object) -> EventRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_event_ref_type_0 = (
                                EventRefType0.from_dict(data)
                            )

                            return componentsschemas_event_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(EventRefType0 | None, data)

                    events_type_0_item = _parse_events_type_0_item(
                        events_type_0_item_data
                    )

                    events_type_0.append(events_type_0_item)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventRefType0 | None] | None | Unset, data)

        events = _parse_events(d.pop("events", UNSET))

        def _parse_identifiers(data: object) -> list[Identifier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                identifiers_type_0 = []
                _identifiers_type_0 = data
                for identifiers_type_0_item_data in _identifiers_type_0:
                    identifiers_type_0_item = Identifier.from_dict(
                        identifiers_type_0_item_data
                    )

                    identifiers_type_0.append(identifiers_type_0_item)

                return identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Identifier] | None | Unset, data)

        identifiers = _parse_identifiers(d.pop("identifiers", UNSET))

        def _parse_sponsor_organizations(
            data: object,
        ) -> list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sponsor_organizations_type_0 = []
                _sponsor_organizations_type_0 = data
                for (
                    sponsor_organizations_type_0_item_data
                ) in _sponsor_organizations_type_0:

                    def _parse_sponsor_organizations_type_0_item(
                        data: object,
                    ) -> None | OrganizationOrExternalOrganizationRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_organization_or_external_organization_ref_type_0 = OrganizationOrExternalOrganizationRefType0.from_dict(
                                data
                            )

                            return componentsschemas_organization_or_external_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | OrganizationOrExternalOrganizationRefType0, data
                        )

                    sponsor_organizations_type_0_item = (
                        _parse_sponsor_organizations_type_0_item(
                            sponsor_organizations_type_0_item_data
                        )
                    )

                    sponsor_organizations_type_0.append(
                        sponsor_organizations_type_0_item
                    )

                return sponsor_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset,
                data,
            )

        sponsor_organizations = _parse_sponsor_organizations(
            d.pop("sponsorOrganizations", UNSET)
        )

        def _parse_subdivision(data: object) -> ClassificationRefType0 | None | Unset:
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

        subdivision = _parse_subdivision(d.pop("subdivision", UNSET))

        def _parse_title(data: object) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_sub_title(
            data: object,
        ) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        sub_title = _parse_sub_title(d.pop("subTitle", UNSET))

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        system_name = d.pop("systemName", UNSET)

        event = cls(
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
            abbreviated_title=abbreviated_title,
            geo_location=geo_location,
            city=city,
            conference_number=conference_number,
            country=country,
            degree_of_recognition=degree_of_recognition,
            description=description,
            keyword_groups=keyword_groups,
            links=links,
            location=location,
            organizers=organizers,
            lifecycle=lifecycle,
            events=events,
            identifiers=identifiers,
            sponsor_organizations=sponsor_organizations,
            subdivision=subdivision,
            title=title,
            sub_title=sub_title,
            workflow=workflow,
            system_name=system_name,
        )

        event.additional_properties = d
        return event

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
