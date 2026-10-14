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
    from ..models.concept_ref_type_0 import ConceptRefType0
    from ..models.identifier import Identifier
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.term import Term
    from ..models.thesaurus_ref_type_0 import ThesaurusRefType0


T = TypeVar("T", bound="Concept")


@_attrs_define
class Concept:
    """A concept

    Attributes:
        concept_id (str): ConceptId
        thesaurus (None | ThesaurusRefType0): A reference to a thesaurus
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
        parent_concepts (list[ConceptRefType0 | None] | Unset): ParentConcepts
        name (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        terms (list[Term] | Unset): Terms
        inverse_document_frequency (float | None | Unset): The inverse document frequency
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems.
        system_name (str | Unset): The content system name
    """

    concept_id: str
    thesaurus: None | ThesaurusRefType0
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
    parent_concepts: list[ConceptRefType0 | None] | Unset = UNSET
    name: LocalizedStringType0 | None | Unset = UNSET
    terms: list[Term] | Unset = UNSET
    inverse_document_frequency: float | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.concept_ref_type_0 import ConceptRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.thesaurus_ref_type_0 import ThesaurusRefType0

        concept_id = self.concept_id

        thesaurus: dict[str, Any] | None
        if isinstance(self.thesaurus, ThesaurusRefType0):
            thesaurus = self.thesaurus.to_dict()
        else:
            thesaurus = self.thesaurus

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

        parent_concepts: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.parent_concepts, Unset):
            parent_concepts = []
            for parent_concepts_item_data in self.parent_concepts:
                parent_concepts_item: dict[str, Any] | None
                if isinstance(parent_concepts_item_data, ConceptRefType0):
                    parent_concepts_item = parent_concepts_item_data.to_dict()
                else:
                    parent_concepts_item = parent_concepts_item_data
                parent_concepts.append(parent_concepts_item)

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, LocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        terms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)

        inverse_document_frequency: float | None | Unset
        if isinstance(self.inverse_document_frequency, Unset):
            inverse_document_frequency = UNSET
        else:
            inverse_document_frequency = self.inverse_document_frequency

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
                "conceptId": concept_id,
                "thesaurus": thesaurus,
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
        if parent_concepts is not UNSET:
            field_dict["parentConcepts"] = parent_concepts
        if name is not UNSET:
            field_dict["name"] = name
        if terms is not UNSET:
            field_dict["terms"] = terms
        if inverse_document_frequency is not UNSET:
            field_dict["inverseDocumentFrequency"] = inverse_document_frequency
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.concept_ref_type_0 import ConceptRefType0
        from ..models.identifier import Identifier
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.term import Term
        from ..models.thesaurus_ref_type_0 import ThesaurusRefType0

        d = dict(src_dict)
        concept_id = d.pop("conceptId")

        def _parse_thesaurus(data: object) -> None | ThesaurusRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_thesaurus_ref_type_0 = ThesaurusRefType0.from_dict(
                    data
                )

                return componentsschemas_thesaurus_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThesaurusRefType0, data)

        thesaurus = _parse_thesaurus(d.pop("thesaurus"))

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

        _parent_concepts = d.pop("parentConcepts", UNSET)
        parent_concepts: list[ConceptRefType0 | None] | Unset = UNSET
        if _parent_concepts is not UNSET:
            parent_concepts = []
            for parent_concepts_item_data in _parent_concepts:

                def _parse_parent_concepts_item(data: object) -> ConceptRefType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_concept_ref_type_0 = (
                            ConceptRefType0.from_dict(data)
                        )

                        return componentsschemas_concept_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(ConceptRefType0 | None, data)

                parent_concepts_item = _parse_parent_concepts_item(
                    parent_concepts_item_data
                )

                parent_concepts.append(parent_concepts_item)

        def _parse_name(data: object) -> LocalizedStringType0 | None | Unset:
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

        name = _parse_name(d.pop("name", UNSET))

        _terms = d.pop("terms", UNSET)
        terms: list[Term] | Unset = UNSET
        if _terms is not UNSET:
            terms = []
            for terms_item_data in _terms:
                terms_item = Term.from_dict(terms_item_data)

                terms.append(terms_item)

        def _parse_inverse_document_frequency(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        inverse_document_frequency = _parse_inverse_document_frequency(
            d.pop("inverseDocumentFrequency", UNSET)
        )

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

        concept = cls(
            concept_id=concept_id,
            thesaurus=thesaurus,
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
            parent_concepts=parent_concepts,
            name=name,
            terms=terms,
            inverse_document_frequency=inverse_document_frequency,
            identifiers=identifiers,
            system_name=system_name,
        )

        concept.additional_properties = d
        return concept

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
