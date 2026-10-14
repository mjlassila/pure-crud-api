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
    from ..models.classified_address import ClassifiedAddress
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.classified_localized_value import ClassifiedLocalizedValue
    from ..models.classified_value import ClassifiedValue
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.date_range import DateRange
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.person_ref_type_0 import PersonRefType0
    from ..models.visibility import Visibility


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """An organization in the institution

    Attributes:
        name (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        type_ (ClassificationRefType0 | None): A reference to a classification value
        lifecycle (DateRange): A date range
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
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
        name_variants (list[ClassifiedLocalizedValue] | None | Unset): A list of organization name variants
        profile_informations (list[ClassifiedFormattedLocalizedValue] | None | Unset): A list of organization profile
            information entries
        photos (list[ImageFile] | None | Unset): A list of organization photos
        addresses (list[ClassifiedAddress] | None | Unset): A list of organization addresses
        phone_numbers (list[ClassifiedValue] | None | Unset): A list of organization phone numbers
        emails (list[ClassifiedValue] | None | Unset): A list of organization email addresses
        web_addresses (list[ClassifiedLocalizedValue] | None | Unset): A list of organization web addresses
        taken_over_by (None | OrganizationRefType0 | Unset): A reference to an organization in the institution
        parents (list[None | OrganizationRefType0] | None | Unset): A list of parent organizations
        contact_persons (list[None | PersonRefType0] | None | Unset): A list of organization contact persons
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present
        cost_centers (list[ClassificationRefType0 | None] | None | Unset): A list of cost center classifications
        visibility (Visibility | Unset): Visibility of an object
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        links (list[Link] | None | Unset): Links associated with this organization.
        main_research_area (ClassificationRefType0 | None | Unset): A reference to a classification value
        system_name (str | Unset): The content system name
    """

    name: LocalizedStringType0 | None
    type_: ClassificationRefType0 | None
    lifecycle: DateRange
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
    identifiers: list[Identifier] | None | Unset = UNSET
    name_variants: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    profile_informations: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    photos: list[ImageFile] | None | Unset = UNSET
    addresses: list[ClassifiedAddress] | None | Unset = UNSET
    phone_numbers: list[ClassifiedValue] | None | Unset = UNSET
    emails: list[ClassifiedValue] | None | Unset = UNSET
    web_addresses: list[ClassifiedLocalizedValue] | None | Unset = UNSET
    taken_over_by: None | OrganizationRefType0 | Unset = UNSET
    parents: list[None | OrganizationRefType0] | None | Unset = UNSET
    contact_persons: list[None | PersonRefType0] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    cost_centers: list[ClassificationRefType0 | None] | None | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    main_research_area: ClassificationRefType0 | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        name: dict[str, Any] | None
        if isinstance(self.name, LocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        lifecycle = self.lifecycle.to_dict()

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

        name_variants: list[dict[str, Any]] | None | Unset
        if isinstance(self.name_variants, Unset):
            name_variants = UNSET
        elif isinstance(self.name_variants, list):
            name_variants = []
            for name_variants_type_0_item_data in self.name_variants:
                name_variants_type_0_item = name_variants_type_0_item_data.to_dict()
                name_variants.append(name_variants_type_0_item)

        else:
            name_variants = self.name_variants

        profile_informations: list[dict[str, Any]] | None | Unset
        if isinstance(self.profile_informations, Unset):
            profile_informations = UNSET
        elif isinstance(self.profile_informations, list):
            profile_informations = []
            for profile_informations_type_0_item_data in self.profile_informations:
                profile_informations_type_0_item = (
                    profile_informations_type_0_item_data.to_dict()
                )
                profile_informations.append(profile_informations_type_0_item)

        else:
            profile_informations = self.profile_informations

        photos: list[dict[str, Any]] | None | Unset
        if isinstance(self.photos, Unset):
            photos = UNSET
        elif isinstance(self.photos, list):
            photos = []
            for photos_type_0_item_data in self.photos:
                photos_type_0_item = photos_type_0_item_data.to_dict()
                photos.append(photos_type_0_item)

        else:
            photos = self.photos

        addresses: list[dict[str, Any]] | None | Unset
        if isinstance(self.addresses, Unset):
            addresses = UNSET
        elif isinstance(self.addresses, list):
            addresses = []
            for addresses_type_0_item_data in self.addresses:
                addresses_type_0_item = addresses_type_0_item_data.to_dict()
                addresses.append(addresses_type_0_item)

        else:
            addresses = self.addresses

        phone_numbers: list[dict[str, Any]] | None | Unset
        if isinstance(self.phone_numbers, Unset):
            phone_numbers = UNSET
        elif isinstance(self.phone_numbers, list):
            phone_numbers = []
            for phone_numbers_type_0_item_data in self.phone_numbers:
                phone_numbers_type_0_item = phone_numbers_type_0_item_data.to_dict()
                phone_numbers.append(phone_numbers_type_0_item)

        else:
            phone_numbers = self.phone_numbers

        emails: list[dict[str, Any]] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = []
            for emails_type_0_item_data in self.emails:
                emails_type_0_item = emails_type_0_item_data.to_dict()
                emails.append(emails_type_0_item)

        else:
            emails = self.emails

        web_addresses: list[dict[str, Any]] | None | Unset
        if isinstance(self.web_addresses, Unset):
            web_addresses = UNSET
        elif isinstance(self.web_addresses, list):
            web_addresses = []
            for web_addresses_type_0_item_data in self.web_addresses:
                web_addresses_type_0_item = web_addresses_type_0_item_data.to_dict()
                web_addresses.append(web_addresses_type_0_item)

        else:
            web_addresses = self.web_addresses

        taken_over_by: dict[str, Any] | None | Unset
        if isinstance(self.taken_over_by, Unset):
            taken_over_by = UNSET
        elif isinstance(self.taken_over_by, OrganizationRefType0):
            taken_over_by = self.taken_over_by.to_dict()
        else:
            taken_over_by = self.taken_over_by

        parents: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.parents, Unset):
            parents = UNSET
        elif isinstance(self.parents, list):
            parents = []
            for parents_type_0_item_data in self.parents:
                parents_type_0_item: dict[str, Any] | None
                if isinstance(parents_type_0_item_data, OrganizationRefType0):
                    parents_type_0_item = parents_type_0_item_data.to_dict()
                else:
                    parents_type_0_item = parents_type_0_item_data
                parents.append(parents_type_0_item)

        else:
            parents = self.parents

        contact_persons: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.contact_persons, Unset):
            contact_persons = UNSET
        elif isinstance(self.contact_persons, list):
            contact_persons = []
            for contact_persons_type_0_item_data in self.contact_persons:
                contact_persons_type_0_item: dict[str, Any] | None
                if isinstance(contact_persons_type_0_item_data, PersonRefType0):
                    contact_persons_type_0_item = (
                        contact_persons_type_0_item_data.to_dict()
                    )
                else:
                    contact_persons_type_0_item = contact_persons_type_0_item_data
                contact_persons.append(contact_persons_type_0_item)

        else:
            contact_persons = self.contact_persons

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

        cost_centers: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.cost_centers, Unset):
            cost_centers = UNSET
        elif isinstance(self.cost_centers, list):
            cost_centers = []
            for cost_centers_type_0_item_data in self.cost_centers:
                cost_centers_type_0_item: dict[str, Any] | None
                if isinstance(cost_centers_type_0_item_data, ClassificationRefType0):
                    cost_centers_type_0_item = cost_centers_type_0_item_data.to_dict()
                else:
                    cost_centers_type_0_item = cost_centers_type_0_item_data
                cost_centers.append(cost_centers_type_0_item)

        else:
            cost_centers = self.cost_centers

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

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

        main_research_area: dict[str, Any] | None | Unset
        if isinstance(self.main_research_area, Unset):
            main_research_area = UNSET
        elif isinstance(self.main_research_area, ClassificationRefType0):
            main_research_area = self.main_research_area.to_dict()
        else:
            main_research_area = self.main_research_area

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "lifecycle": lifecycle,
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
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if name_variants is not UNSET:
            field_dict["nameVariants"] = name_variants
        if profile_informations is not UNSET:
            field_dict["profileInformations"] = profile_informations
        if photos is not UNSET:
            field_dict["photos"] = photos
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if emails is not UNSET:
            field_dict["emails"] = emails
        if web_addresses is not UNSET:
            field_dict["webAddresses"] = web_addresses
        if taken_over_by is not UNSET:
            field_dict["takenOverBy"] = taken_over_by
        if parents is not UNSET:
            field_dict["parents"] = parents
        if contact_persons is not UNSET:
            field_dict["contactPersons"] = contact_persons
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if cost_centers is not UNSET:
            field_dict["costCenters"] = cost_centers
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if links is not UNSET:
            field_dict["links"] = links
        if main_research_area is not UNSET:
            field_dict["mainResearchArea"] = main_research_area
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_address import ClassifiedAddress
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.classified_localized_value import ClassifiedLocalizedValue
        from ..models.classified_value import ClassifiedValue
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.date_range import DateRange
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.person_ref_type_0 import PersonRefType0
        from ..models.visibility import Visibility

        d = dict(src_dict)

        def _parse_name(data: object) -> LocalizedStringType0 | None:
            if data is None:
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
            return cast(LocalizedStringType0 | None, data)

        name = _parse_name(d.pop("name"))

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

        lifecycle = DateRange.from_dict(d.pop("lifecycle"))

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

        def _parse_name_variants(
            data: object,
        ) -> list[ClassifiedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                name_variants_type_0 = []
                _name_variants_type_0 = data
                for name_variants_type_0_item_data in _name_variants_type_0:
                    name_variants_type_0_item = ClassifiedLocalizedValue.from_dict(
                        name_variants_type_0_item_data
                    )

                    name_variants_type_0.append(name_variants_type_0_item)

                return name_variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedLocalizedValue] | None | Unset, data)

        name_variants = _parse_name_variants(d.pop("nameVariants", UNSET))

        def _parse_profile_informations(
            data: object,
        ) -> list[ClassifiedFormattedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                profile_informations_type_0 = []
                _profile_informations_type_0 = data
                for (
                    profile_informations_type_0_item_data
                ) in _profile_informations_type_0:
                    profile_informations_type_0_item = (
                        ClassifiedFormattedLocalizedValue.from_dict(
                            profile_informations_type_0_item_data
                        )
                    )

                    profile_informations_type_0.append(profile_informations_type_0_item)

                return profile_informations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedFormattedLocalizedValue] | None | Unset, data)

        profile_informations = _parse_profile_informations(
            d.pop("profileInformations", UNSET)
        )

        def _parse_photos(data: object) -> list[ImageFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                photos_type_0 = []
                _photos_type_0 = data
                for photos_type_0_item_data in _photos_type_0:
                    photos_type_0_item = ImageFile.from_dict(photos_type_0_item_data)

                    photos_type_0.append(photos_type_0_item)

                return photos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageFile] | None | Unset, data)

        photos = _parse_photos(d.pop("photos", UNSET))

        def _parse_addresses(data: object) -> list[ClassifiedAddress] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                addresses_type_0 = []
                _addresses_type_0 = data
                for addresses_type_0_item_data in _addresses_type_0:
                    addresses_type_0_item = ClassifiedAddress.from_dict(
                        addresses_type_0_item_data
                    )

                    addresses_type_0.append(addresses_type_0_item)

                return addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedAddress] | None | Unset, data)

        addresses = _parse_addresses(d.pop("addresses", UNSET))

        def _parse_phone_numbers(data: object) -> list[ClassifiedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = []
                _phone_numbers_type_0 = data
                for phone_numbers_type_0_item_data in _phone_numbers_type_0:
                    phone_numbers_type_0_item = ClassifiedValue.from_dict(
                        phone_numbers_type_0_item_data
                    )

                    phone_numbers_type_0.append(phone_numbers_type_0_item)

                return phone_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedValue] | None | Unset, data)

        phone_numbers = _parse_phone_numbers(d.pop("phoneNumbers", UNSET))

        def _parse_emails(data: object) -> list[ClassifiedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = []
                _emails_type_0 = data
                for emails_type_0_item_data in _emails_type_0:
                    emails_type_0_item = ClassifiedValue.from_dict(
                        emails_type_0_item_data
                    )

                    emails_type_0.append(emails_type_0_item)

                return emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedValue] | None | Unset, data)

        emails = _parse_emails(d.pop("emails", UNSET))

        def _parse_web_addresses(
            data: object,
        ) -> list[ClassifiedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                web_addresses_type_0 = []
                _web_addresses_type_0 = data
                for web_addresses_type_0_item_data in _web_addresses_type_0:
                    web_addresses_type_0_item = ClassifiedLocalizedValue.from_dict(
                        web_addresses_type_0_item_data
                    )

                    web_addresses_type_0.append(web_addresses_type_0_item)

                return web_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedLocalizedValue] | None | Unset, data)

        web_addresses = _parse_web_addresses(d.pop("webAddresses", UNSET))

        def _parse_taken_over_by(data: object) -> None | OrganizationRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(None | OrganizationRefType0 | Unset, data)

        taken_over_by = _parse_taken_over_by(d.pop("takenOverBy", UNSET))

        def _parse_parents(
            data: object,
        ) -> list[None | OrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parents_type_0 = []
                _parents_type_0 = data
                for parents_type_0_item_data in _parents_type_0:

                    def _parse_parents_type_0_item(
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

                    parents_type_0_item = _parse_parents_type_0_item(
                        parents_type_0_item_data
                    )

                    parents_type_0.append(parents_type_0_item)

                return parents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | OrganizationRefType0] | None | Unset, data)

        parents = _parse_parents(d.pop("parents", UNSET))

        def _parse_contact_persons(
            data: object,
        ) -> list[None | PersonRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contact_persons_type_0 = []
                _contact_persons_type_0 = data
                for contact_persons_type_0_item_data in _contact_persons_type_0:

                    def _parse_contact_persons_type_0_item(
                        data: object,
                    ) -> None | PersonRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_person_ref_type_0 = (
                                PersonRefType0.from_dict(data)
                            )

                            return componentsschemas_person_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | PersonRefType0, data)

                    contact_persons_type_0_item = _parse_contact_persons_type_0_item(
                        contact_persons_type_0_item_data
                    )

                    contact_persons_type_0.append(contact_persons_type_0_item)

                return contact_persons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | PersonRefType0] | None | Unset, data)

        contact_persons = _parse_contact_persons(d.pop("contactPersons", UNSET))

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

        def _parse_cost_centers(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cost_centers_type_0 = []
                _cost_centers_type_0 = data
                for cost_centers_type_0_item_data in _cost_centers_type_0:

                    def _parse_cost_centers_type_0_item(
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

                    cost_centers_type_0_item = _parse_cost_centers_type_0_item(
                        cost_centers_type_0_item_data
                    )

                    cost_centers_type_0.append(cost_centers_type_0_item)

                return cost_centers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        cost_centers = _parse_cost_centers(d.pop("costCenters", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        def _parse_custom_defined_fields(
            data: object,
        ) -> CustomDefinedFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_custom_defined_fields_type_0 = (
                    CustomDefinedFieldsType0.from_dict(data)
                )

                return componentsschemas_custom_defined_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDefinedFieldsType0 | None | Unset, data)

        custom_defined_fields = _parse_custom_defined_fields(
            d.pop("customDefinedFields", UNSET)
        )

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

        def _parse_main_research_area(
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

        main_research_area = _parse_main_research_area(d.pop("mainResearchArea", UNSET))

        system_name = d.pop("systemName", UNSET)

        organization = cls(
            name=name,
            type_=type_,
            lifecycle=lifecycle,
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
            identifiers=identifiers,
            name_variants=name_variants,
            profile_informations=profile_informations,
            photos=photos,
            addresses=addresses,
            phone_numbers=phone_numbers,
            emails=emails,
            web_addresses=web_addresses,
            taken_over_by=taken_over_by,
            parents=parents,
            contact_persons=contact_persons,
            keyword_groups=keyword_groups,
            cost_centers=cost_centers,
            visibility=visibility,
            custom_defined_fields=custom_defined_fields,
            links=links,
            main_research_area=main_research_area,
            system_name=system_name,
        )

        organization.additional_properties = d
        return organization

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
