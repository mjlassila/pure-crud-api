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
    from ..models.additional_issn_type_0 import AdditionalISSNType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.identifier import Identifier
    from ..models.issn import ISSN
    from ..models.journal_title import JournalTitle
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.publisher_ref_type_0 import PublisherRefType0
    from ..models.sherpa_romeo_policy import SherpaRomeoPolicy
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Journal")


@_attrs_define
class Journal:
    """A periodical presenting articles on a particular subject.

    Attributes:
        titles (list[JournalTitle]): Titles of the journal, these titles will be available for use when relating the
            journal to other content.
        type_ (ClassificationRefType0 | None): A reference to a classification value
        workflow (Workflow): Information about workflow
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
        issns (list[ISSN] | None | Unset): International Standard Serial Numbers of the journal, ISSNs in this list are
            searchable and selectable when relating the journal to other content
        additional_searchable_issns (list[AdditionalISSNType0 | None] | None | Unset): Additional International Standard
            Serial Numbers of the journal, ISSNs in this list are searchable but not selectable when relating the journal to
            other content
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
        indexed_in_doaj (bool | Unset): Whether the journal is present in the Directory of Open Access Journals
        keyword_groups (list[KeywordGroup] | None | Unset): Keywords associated with the journal
        links (list[Link] | None | Unset): Links to websites or other URLs associated with the journal
        publisher (None | PublisherRefType0 | Unset): A reference to a publisher
        identifiers (list[Identifier] | None | Unset): Identifiers of the Journal, often used to identify the journal in
            other sources, an example could be the Scopus Id of the journal
        additional_searchable_titles (list[str] | None | Unset): Additional searchable titles of the journal, often
            abbreviations that are not used to show a journal, cannot be used when relating the journal to other content.
        sherpa_romeo_policy (SherpaRomeoPolicy | Unset): Describes a SHERPA RoMEO open access policy.
        additional_open_access_information (None | str | Unset): Additional open access information for this journal.
        system_name (str | Unset): The content system name
    """

    titles: list[JournalTitle]
    type_: ClassificationRefType0 | None
    workflow: Workflow
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
    issns: list[ISSN] | None | Unset = UNSET
    additional_searchable_issns: list[AdditionalISSNType0 | None] | None | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    indexed_in_doaj: bool | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    publisher: None | PublisherRefType0 | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    additional_searchable_titles: list[str] | None | Unset = UNSET
    sherpa_romeo_policy: SherpaRomeoPolicy | Unset = UNSET
    additional_open_access_information: None | str | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.additional_issn_type_0 import AdditionalISSNType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.publisher_ref_type_0 import PublisherRefType0

        titles = []
        for titles_item_data in self.titles:
            titles_item = titles_item_data.to_dict()
            titles.append(titles_item)

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        workflow = self.workflow.to_dict()

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

        issns: list[dict[str, Any]] | None | Unset
        if isinstance(self.issns, Unset):
            issns = UNSET
        elif isinstance(self.issns, list):
            issns = []
            for issns_type_0_item_data in self.issns:
                issns_type_0_item = issns_type_0_item_data.to_dict()
                issns.append(issns_type_0_item)

        else:
            issns = self.issns

        additional_searchable_issns: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.additional_searchable_issns, Unset):
            additional_searchable_issns = UNSET
        elif isinstance(self.additional_searchable_issns, list):
            additional_searchable_issns = []
            for (
                additional_searchable_issns_type_0_item_data
            ) in self.additional_searchable_issns:
                additional_searchable_issns_type_0_item: dict[str, Any] | None
                if isinstance(
                    additional_searchable_issns_type_0_item_data, AdditionalISSNType0
                ):
                    additional_searchable_issns_type_0_item = (
                        additional_searchable_issns_type_0_item_data.to_dict()
                    )
                else:
                    additional_searchable_issns_type_0_item = (
                        additional_searchable_issns_type_0_item_data
                    )
                additional_searchable_issns.append(
                    additional_searchable_issns_type_0_item
                )

        else:
            additional_searchable_issns = self.additional_searchable_issns

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, ClassificationRefType0):
            country = self.country.to_dict()
        else:
            country = self.country

        indexed_in_doaj = self.indexed_in_doaj

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

        publisher: dict[str, Any] | None | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        elif isinstance(self.publisher, PublisherRefType0):
            publisher = self.publisher.to_dict()
        else:
            publisher = self.publisher

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

        additional_searchable_titles: list[str] | None | Unset
        if isinstance(self.additional_searchable_titles, Unset):
            additional_searchable_titles = UNSET
        elif isinstance(self.additional_searchable_titles, list):
            additional_searchable_titles = self.additional_searchable_titles

        else:
            additional_searchable_titles = self.additional_searchable_titles

        sherpa_romeo_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sherpa_romeo_policy, Unset):
            sherpa_romeo_policy = self.sherpa_romeo_policy.to_dict()

        additional_open_access_information: None | str | Unset
        if isinstance(self.additional_open_access_information, Unset):
            additional_open_access_information = UNSET
        else:
            additional_open_access_information = self.additional_open_access_information

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "titles": titles,
                "type": type_,
                "workflow": workflow,
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
        if issns is not UNSET:
            field_dict["issns"] = issns
        if additional_searchable_issns is not UNSET:
            field_dict["additionalSearchableIssns"] = additional_searchable_issns
        if country is not UNSET:
            field_dict["country"] = country
        if indexed_in_doaj is not UNSET:
            field_dict["indexedInDoaj"] = indexed_in_doaj
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if links is not UNSET:
            field_dict["links"] = links
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if additional_searchable_titles is not UNSET:
            field_dict["additionalSearchableTitles"] = additional_searchable_titles
        if sherpa_romeo_policy is not UNSET:
            field_dict["sherpaRomeoPolicy"] = sherpa_romeo_policy
        if additional_open_access_information is not UNSET:
            field_dict["additionalOpenAccessInformation"] = (
                additional_open_access_information
            )
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.additional_issn_type_0 import AdditionalISSNType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.identifier import Identifier
        from ..models.issn import ISSN
        from ..models.journal_title import JournalTitle
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.publisher_ref_type_0 import PublisherRefType0
        from ..models.sherpa_romeo_policy import SherpaRomeoPolicy
        from ..models.workflow import Workflow

        d = dict(src_dict)
        titles = []
        _titles = d.pop("titles")
        for titles_item_data in _titles:
            titles_item = JournalTitle.from_dict(titles_item_data)

            titles.append(titles_item)

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

        workflow = Workflow.from_dict(d.pop("workflow"))

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

        def _parse_issns(data: object) -> list[ISSN] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                issns_type_0 = []
                _issns_type_0 = data
                for issns_type_0_item_data in _issns_type_0:
                    issns_type_0_item = ISSN.from_dict(issns_type_0_item_data)

                    issns_type_0.append(issns_type_0_item)

                return issns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ISSN] | None | Unset, data)

        issns = _parse_issns(d.pop("issns", UNSET))

        def _parse_additional_searchable_issns(
            data: object,
        ) -> list[AdditionalISSNType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_searchable_issns_type_0 = []
                _additional_searchable_issns_type_0 = data
                for (
                    additional_searchable_issns_type_0_item_data
                ) in _additional_searchable_issns_type_0:

                    def _parse_additional_searchable_issns_type_0_item(
                        data: object,
                    ) -> AdditionalISSNType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_additional_issn_type_0 = (
                                AdditionalISSNType0.from_dict(data)
                            )

                            return componentsschemas_additional_issn_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(AdditionalISSNType0 | None, data)

                    additional_searchable_issns_type_0_item = (
                        _parse_additional_searchable_issns_type_0_item(
                            additional_searchable_issns_type_0_item_data
                        )
                    )

                    additional_searchable_issns_type_0.append(
                        additional_searchable_issns_type_0_item
                    )

                return additional_searchable_issns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AdditionalISSNType0 | None] | None | Unset, data)

        additional_searchable_issns = _parse_additional_searchable_issns(
            d.pop("additionalSearchableIssns", UNSET)
        )

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

        indexed_in_doaj = d.pop("indexedInDoaj", UNSET)

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

        def _parse_publisher(data: object) -> None | PublisherRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_publisher_ref_type_0 = PublisherRefType0.from_dict(
                    data
                )

                return componentsschemas_publisher_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublisherRefType0 | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

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

        def _parse_additional_searchable_titles(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_searchable_titles_type_0 = cast(list[str], data)

                return additional_searchable_titles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        additional_searchable_titles = _parse_additional_searchable_titles(
            d.pop("additionalSearchableTitles", UNSET)
        )

        _sherpa_romeo_policy = d.pop("sherpaRomeoPolicy", UNSET)
        sherpa_romeo_policy: SherpaRomeoPolicy | Unset
        if isinstance(_sherpa_romeo_policy, Unset):
            sherpa_romeo_policy = UNSET
        else:
            sherpa_romeo_policy = SherpaRomeoPolicy.from_dict(_sherpa_romeo_policy)

        def _parse_additional_open_access_information(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        additional_open_access_information = _parse_additional_open_access_information(
            d.pop("additionalOpenAccessInformation", UNSET)
        )

        system_name = d.pop("systemName", UNSET)

        journal = cls(
            titles=titles,
            type_=type_,
            workflow=workflow,
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
            issns=issns,
            additional_searchable_issns=additional_searchable_issns,
            country=country,
            indexed_in_doaj=indexed_in_doaj,
            keyword_groups=keyword_groups,
            links=links,
            publisher=publisher,
            identifiers=identifiers,
            additional_searchable_titles=additional_searchable_titles,
            sherpa_romeo_policy=sherpa_romeo_policy,
            additional_open_access_information=additional_open_access_information,
            system_name=system_name,
        )

        journal.additional_properties = d
        return journal

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
