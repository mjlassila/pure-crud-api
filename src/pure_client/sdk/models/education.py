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
    from ..models.education_ref_type_0 import EducationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.link_identifier import LinkIdentifier
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.semester_ref_type_0 import SemesterRefType0
    from ..models.specialization_ref_type_0 import SpecializationRefType0
    from ..models.visibility import Visibility


T = TypeVar("T", bound="Education")


@_attrs_define
class Education:
    """An education

    Attributes:
        name (FormattedLocalizedStringType0 | None): A set of localized strings that support formatting. Invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        period (DateRange): A date range
        visibility (Visibility): Visibility of an object
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
        semesters (list[None | SemesterRefType0] | Unset): The semesters belonging to the education
        links (list[Link] | Unset): The links to the education
        organizations (list[None | OrganizationRefType0] | Unset): A collection of organizations on the education
        education_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        specializations (list[None | SpecializationRefType0] | Unset): A collection of specializations on the education
        sort_name (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        profile (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        education_id (None | str | Unset): The education id
        parent (EducationRefType0 | None | Unset): A reference to Education
        link_identifiers (list[LinkIdentifier] | Unset): A collection of link identifiers on the education
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the education.
        system_name (str | Unset): The content system name
    """

    name: FormattedLocalizedStringType0 | None
    period: DateRange
    visibility: Visibility
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
    semesters: list[None | SemesterRefType0] | Unset = UNSET
    links: list[Link] | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | Unset = UNSET
    education_type: ClassificationRefType0 | None | Unset = UNSET
    specializations: list[None | SpecializationRefType0] | Unset = UNSET
    sort_name: FormattedLocalizedStringType0 | None | Unset = UNSET
    profile: FormattedLocalizedStringType0 | None | Unset = UNSET
    education_id: None | str | Unset = UNSET
    parent: EducationRefType0 | None | Unset = UNSET
    link_identifiers: list[LinkIdentifier] | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.education_ref_type_0 import EducationRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.semester_ref_type_0 import SemesterRefType0
        from ..models.specialization_ref_type_0 import SpecializationRefType0

        name: dict[str, Any] | None
        if isinstance(self.name, FormattedLocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        period = self.period.to_dict()

        visibility = self.visibility.to_dict()

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

        semesters: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.semesters, Unset):
            semesters = []
            for semesters_item_data in self.semesters:
                semesters_item: dict[str, Any] | None
                if isinstance(semesters_item_data, SemesterRefType0):
                    semesters_item = semesters_item_data.to_dict()
                else:
                    semesters_item = semesters_item_data
                semesters.append(semesters_item)

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        organizations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item: dict[str, Any] | None
                if isinstance(organizations_item_data, OrganizationRefType0):
                    organizations_item = organizations_item_data.to_dict()
                else:
                    organizations_item = organizations_item_data
                organizations.append(organizations_item)

        education_type: dict[str, Any] | None | Unset
        if isinstance(self.education_type, Unset):
            education_type = UNSET
        elif isinstance(self.education_type, ClassificationRefType0):
            education_type = self.education_type.to_dict()
        else:
            education_type = self.education_type

        specializations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.specializations, Unset):
            specializations = []
            for specializations_item_data in self.specializations:
                specializations_item: dict[str, Any] | None
                if isinstance(specializations_item_data, SpecializationRefType0):
                    specializations_item = specializations_item_data.to_dict()
                else:
                    specializations_item = specializations_item_data
                specializations.append(specializations_item)

        sort_name: dict[str, Any] | None | Unset
        if isinstance(self.sort_name, Unset):
            sort_name = UNSET
        elif isinstance(self.sort_name, FormattedLocalizedStringType0):
            sort_name = self.sort_name.to_dict()
        else:
            sort_name = self.sort_name

        profile: dict[str, Any] | None | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, FormattedLocalizedStringType0):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        education_id: None | str | Unset
        if isinstance(self.education_id, Unset):
            education_id = UNSET
        else:
            education_id = self.education_id

        parent: dict[str, Any] | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, EducationRefType0):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        link_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.link_identifiers, Unset):
            link_identifiers = []
            for link_identifiers_item_data in self.link_identifiers:
                link_identifiers_item = link_identifiers_item_data.to_dict()
                link_identifiers.append(link_identifiers_item)

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "period": period,
                "visibility": visibility,
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
        if semesters is not UNSET:
            field_dict["semesters"] = semesters
        if links is not UNSET:
            field_dict["links"] = links
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if education_type is not UNSET:
            field_dict["educationType"] = education_type
        if specializations is not UNSET:
            field_dict["specializations"] = specializations
        if sort_name is not UNSET:
            field_dict["sortName"] = sort_name
        if profile is not UNSET:
            field_dict["profile"] = profile
        if education_id is not UNSET:
            field_dict["educationId"] = education_id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if link_identifiers is not UNSET:
            field_dict["linkIdentifiers"] = link_identifiers
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange
        from ..models.education_ref_type_0 import EducationRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.link_identifier import LinkIdentifier
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.semester_ref_type_0 import SemesterRefType0
        from ..models.specialization_ref_type_0 import SpecializationRefType0
        from ..models.visibility import Visibility

        d = dict(src_dict)

        def _parse_name(data: object) -> FormattedLocalizedStringType0 | None:
            if data is None:
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
            return cast(FormattedLocalizedStringType0 | None, data)

        name = _parse_name(d.pop("name"))

        period = DateRange.from_dict(d.pop("period"))

        visibility = Visibility.from_dict(d.pop("visibility"))

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

        _semesters = d.pop("semesters", UNSET)
        semesters: list[None | SemesterRefType0] | Unset = UNSET
        if _semesters is not UNSET:
            semesters = []
            for semesters_item_data in _semesters:

                def _parse_semesters_item(data: object) -> None | SemesterRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_semester_ref_type_0 = (
                            SemesterRefType0.from_dict(data)
                        )

                        return componentsschemas_semester_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | SemesterRefType0, data)

                semesters_item = _parse_semesters_item(semesters_item_data)

                semesters.append(semesters_item)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[None | OrganizationRefType0] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:

                def _parse_organizations_item(
                    data: object,
                ) -> None | OrganizationRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_organization_ref_type_0 = (
                            OrganizationRefType0.from_dict(data)
                        )

                        return componentsschemas_organization_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | OrganizationRefType0, data)

                organizations_item = _parse_organizations_item(organizations_item_data)

                organizations.append(organizations_item)

        def _parse_education_type(
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

        education_type = _parse_education_type(d.pop("educationType", UNSET))

        _specializations = d.pop("specializations", UNSET)
        specializations: list[None | SpecializationRefType0] | Unset = UNSET
        if _specializations is not UNSET:
            specializations = []
            for specializations_item_data in _specializations:

                def _parse_specializations_item(
                    data: object,
                ) -> None | SpecializationRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_specialization_ref_type_0 = (
                            SpecializationRefType0.from_dict(data)
                        )

                        return componentsschemas_specialization_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | SpecializationRefType0, data)

                specializations_item = _parse_specializations_item(
                    specializations_item_data
                )

                specializations.append(specializations_item)

        def _parse_sort_name(
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

        sort_name = _parse_sort_name(d.pop("sortName", UNSET))

        def _parse_profile(
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

        profile = _parse_profile(d.pop("profile", UNSET))

        def _parse_education_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_id = _parse_education_id(d.pop("educationId", UNSET))

        def _parse_parent(data: object) -> EducationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_education_ref_type_0 = EducationRefType0.from_dict(
                    data
                )

                return componentsschemas_education_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EducationRefType0 | None | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        _link_identifiers = d.pop("linkIdentifiers", UNSET)
        link_identifiers: list[LinkIdentifier] | Unset = UNSET
        if _link_identifiers is not UNSET:
            link_identifiers = []
            for link_identifiers_item_data in _link_identifiers:
                link_identifiers_item = LinkIdentifier.from_dict(
                    link_identifiers_item_data
                )

                link_identifiers.append(link_identifiers_item)

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

        system_name = d.pop("systemName", UNSET)

        education = cls(
            name=name,
            period=period,
            visibility=visibility,
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
            semesters=semesters,
            links=links,
            organizations=organizations,
            education_type=education_type,
            specializations=specializations,
            sort_name=sort_name,
            profile=profile,
            education_id=education_id,
            parent=parent,
            link_identifiers=link_identifiers,
            keyword_groups=keyword_groups,
            identifiers=identifiers,
            system_name=system_name,
        )

        education.additional_properties = d
        return education

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
