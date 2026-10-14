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
    from ..models.cerif_address_type_0 import CERIFAddressType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.date_range import DateRange
    from ..models.document import Document
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="ExternalOrganization")


@_attrs_define
class ExternalOrganization:
    """An organization external to the institution

    Attributes:
        name (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
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
        nature_types (list[ClassificationRefType0 | None] | None | Unset): Nature of the organizations work
        acronym (None | str | Unset): Acronym of organization name
        alternative_names (list[str] | None | Unset): Alternative names of organization
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems. Such as
            a Scopus ID. Used by Pure where it is necessary to identify objects to specific external systems
        address (CERIFAddressType0 | None | Unset): A physical address
        phone_number (None | str | Unset): Phone number
        mobile_phone_number (None | str | Unset): Phone number (mobile)
        fax (None | str | Unset): Fax number
        email (None | str | Unset): Email address
        bank_account_number (None | str | Unset): Bank account number
        vat_number (None | str | Unset): VAT number
        documents (list[Document] | None | Unset): Arbitrary documents relevant to the organization
        images (list[ImageFile] | None | Unset): External organization image
        links (list[Link] | None | Unset): Links to information about the organization
        keyword_groups (list[KeywordGroup] | None | Unset): A group for each type of keyword present
        note (None | str | Unset): A free-form note about the organization
        visibility (Visibility | Unset): Visibility of an object
        workflow (Workflow | Unset): Information about workflow
        taken_over_by (None | OrganizationOrExternalOrganizationRefType0 | Unset): A reference to an organization in the
            institution or an external organization
        lifecycle (DateRange | Unset): A date range
        parent (ExternalOrganizationRefType0 | None | Unset): A reference to an organization external to the institution
        system_name (str | Unset): The content system name
    """

    name: LocalizedStringType0 | None
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
    nature_types: list[ClassificationRefType0 | None] | None | Unset = UNSET
    acronym: None | str | Unset = UNSET
    alternative_names: list[str] | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    address: CERIFAddressType0 | None | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    mobile_phone_number: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    bank_account_number: None | str | Unset = UNSET
    vat_number: None | str | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    note: None | str | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    taken_over_by: None | OrganizationOrExternalOrganizationRefType0 | Unset = UNSET
    lifecycle: DateRange | Unset = UNSET
    parent: ExternalOrganizationRefType0 | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cerif_address_type_0 import CERIFAddressType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

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

        nature_types: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.nature_types, Unset):
            nature_types = UNSET
        elif isinstance(self.nature_types, list):
            nature_types = []
            for nature_types_type_0_item_data in self.nature_types:
                nature_types_type_0_item: dict[str, Any] | None
                if isinstance(nature_types_type_0_item_data, ClassificationRefType0):
                    nature_types_type_0_item = nature_types_type_0_item_data.to_dict()
                else:
                    nature_types_type_0_item = nature_types_type_0_item_data
                nature_types.append(nature_types_type_0_item)

        else:
            nature_types = self.nature_types

        acronym: None | str | Unset
        if isinstance(self.acronym, Unset):
            acronym = UNSET
        else:
            acronym = self.acronym

        alternative_names: list[str] | None | Unset
        if isinstance(self.alternative_names, Unset):
            alternative_names = UNSET
        elif isinstance(self.alternative_names, list):
            alternative_names = self.alternative_names

        else:
            alternative_names = self.alternative_names

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

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, CERIFAddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        mobile_phone_number: None | str | Unset
        if isinstance(self.mobile_phone_number, Unset):
            mobile_phone_number = UNSET
        else:
            mobile_phone_number = self.mobile_phone_number

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        bank_account_number: None | str | Unset
        if isinstance(self.bank_account_number, Unset):
            bank_account_number = UNSET
        else:
            bank_account_number = self.bank_account_number

        vat_number: None | str | Unset
        if isinstance(self.vat_number, Unset):
            vat_number = UNSET
        else:
            vat_number = self.vat_number

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

        images: list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

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

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        taken_over_by: dict[str, Any] | None | Unset
        if isinstance(self.taken_over_by, Unset):
            taken_over_by = UNSET
        elif isinstance(self.taken_over_by, OrganizationOrExternalOrganizationRefType0):
            taken_over_by = self.taken_over_by.to_dict()
        else:
            taken_over_by = self.taken_over_by

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        parent: dict[str, Any] | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, ExternalOrganizationRefType0):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
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
        if nature_types is not UNSET:
            field_dict["natureTypes"] = nature_types
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if alternative_names is not UNSET:
            field_dict["alternativeNames"] = alternative_names
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if address is not UNSET:
            field_dict["address"] = address
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if mobile_phone_number is not UNSET:
            field_dict["mobilePhoneNumber"] = mobile_phone_number
        if fax is not UNSET:
            field_dict["fax"] = fax
        if email is not UNSET:
            field_dict["email"] = email
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number
        if documents is not UNSET:
            field_dict["documents"] = documents
        if images is not UNSET:
            field_dict["images"] = images
        if links is not UNSET:
            field_dict["links"] = links
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if note is not UNSET:
            field_dict["note"] = note
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if taken_over_by is not UNSET:
            field_dict["takenOverBy"] = taken_over_by
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if parent is not UNSET:
            field_dict["parent"] = parent
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cerif_address_type_0 import CERIFAddressType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange
        from ..models.document import Document
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

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

        def _parse_nature_types(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nature_types_type_0 = []
                _nature_types_type_0 = data
                for nature_types_type_0_item_data in _nature_types_type_0:

                    def _parse_nature_types_type_0_item(
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

                    nature_types_type_0_item = _parse_nature_types_type_0_item(
                        nature_types_type_0_item_data
                    )

                    nature_types_type_0.append(nature_types_type_0_item)

                return nature_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        nature_types = _parse_nature_types(d.pop("natureTypes", UNSET))

        def _parse_acronym(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acronym = _parse_acronym(d.pop("acronym", UNSET))

        def _parse_alternative_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alternative_names_type_0 = cast(list[str], data)

                return alternative_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        alternative_names = _parse_alternative_names(d.pop("alternativeNames", UNSET))

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

        def _parse_address(data: object) -> CERIFAddressType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cerif_address_type_0 = CERIFAddressType0.from_dict(
                    data
                )

                return componentsschemas_cerif_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CERIFAddressType0 | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_mobile_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mobile_phone_number = _parse_mobile_phone_number(
            d.pop("mobilePhoneNumber", UNSET)
        )

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_bank_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_account_number = _parse_bank_account_number(
            d.pop("bankAccountNumber", UNSET)
        )

        def _parse_vat_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vat_number = _parse_vat_number(d.pop("vatNumber", UNSET))

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

        def _parse_images(data: object) -> list[ImageFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = ImageFile.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageFile] | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))

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

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        def _parse_taken_over_by(
            data: object,
        ) -> None | OrganizationOrExternalOrganizationRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_or_external_organization_ref_type_0 = (
                    OrganizationOrExternalOrganizationRefType0.from_dict(data)
                )

                return (
                    componentsschemas_organization_or_external_organization_ref_type_0
                )
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationOrExternalOrganizationRefType0 | Unset, data)

        taken_over_by = _parse_taken_over_by(d.pop("takenOverBy", UNSET))

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: DateRange | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = DateRange.from_dict(_lifecycle)

        def _parse_parent(data: object) -> ExternalOrganizationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_external_organization_ref_type_0 = (
                    ExternalOrganizationRefType0.from_dict(data)
                )

                return componentsschemas_external_organization_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalOrganizationRefType0 | None | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        system_name = d.pop("systemName", UNSET)

        external_organization = cls(
            name=name,
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
            nature_types=nature_types,
            acronym=acronym,
            alternative_names=alternative_names,
            identifiers=identifiers,
            address=address,
            phone_number=phone_number,
            mobile_phone_number=mobile_phone_number,
            fax=fax,
            email=email,
            bank_account_number=bank_account_number,
            vat_number=vat_number,
            documents=documents,
            images=images,
            links=links,
            keyword_groups=keyword_groups,
            note=note,
            visibility=visibility,
            workflow=workflow,
            taken_over_by=taken_over_by,
            lifecycle=lifecycle,
            parent=parent,
            system_name=system_name,
        )

        external_organization.additional_properties = d
        return external_organization

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
