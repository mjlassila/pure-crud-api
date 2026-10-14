from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.compound_date_range import CompoundDateRange
    from ..models.document import Document
    from ..models.evidence_contact_information import EvidenceContactInformation
    from ..models.identifier import Identifier
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="ImpactEvidence")


@_attrs_define
class ImpactEvidence:
    """ImpactEvidence

    Attributes:
        period (CompoundDateRange): A date range of that can be defined by only year, year and month or a full date
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        evidence_indicator (ClassificationRefType0 | None | Unset): A reference to a classification value
        evidence_title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        evidence_summary (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        evidence_contact_information (list[EvidenceContactInformation] | Unset): Contact information for the evidence.
        documents (list[Document] | None | Unset): Associated documents for the impact evidence.
        links (list[Link] | None | Unset): Links associated with this impact evidence.
        identifiers (list[Identifier] | None | Unset): IDs that this object corresponds to in external systems.
    """

    period: CompoundDateRange
    pure_id: int | Unset = UNSET
    evidence_indicator: ClassificationRefType0 | None | Unset = UNSET
    evidence_title: LocalizedStringType0 | None | Unset = UNSET
    evidence_summary: LocalizedStringType0 | None | Unset = UNSET
    evidence_contact_information: list[EvidenceContactInformation] | Unset = UNSET
    documents: list[Document] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0

        period = self.period.to_dict()

        pure_id = self.pure_id

        evidence_indicator: dict[str, Any] | None | Unset
        if isinstance(self.evidence_indicator, Unset):
            evidence_indicator = UNSET
        elif isinstance(self.evidence_indicator, ClassificationRefType0):
            evidence_indicator = self.evidence_indicator.to_dict()
        else:
            evidence_indicator = self.evidence_indicator

        evidence_title: dict[str, Any] | None | Unset
        if isinstance(self.evidence_title, Unset):
            evidence_title = UNSET
        elif isinstance(self.evidence_title, LocalizedStringType0):
            evidence_title = self.evidence_title.to_dict()
        else:
            evidence_title = self.evidence_title

        evidence_summary: dict[str, Any] | None | Unset
        if isinstance(self.evidence_summary, Unset):
            evidence_summary = UNSET
        elif isinstance(self.evidence_summary, LocalizedStringType0):
            evidence_summary = self.evidence_summary.to_dict()
        else:
            evidence_summary = self.evidence_summary

        evidence_contact_information: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.evidence_contact_information, Unset):
            evidence_contact_information = []
            for (
                evidence_contact_information_item_data
            ) in self.evidence_contact_information:
                evidence_contact_information_item = (
                    evidence_contact_information_item_data.to_dict()
                )
                evidence_contact_information.append(evidence_contact_information_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if evidence_indicator is not UNSET:
            field_dict["evidenceIndicator"] = evidence_indicator
        if evidence_title is not UNSET:
            field_dict["evidenceTitle"] = evidence_title
        if evidence_summary is not UNSET:
            field_dict["evidenceSummary"] = evidence_summary
        if evidence_contact_information is not UNSET:
            field_dict["evidenceContactInformation"] = evidence_contact_information
        if documents is not UNSET:
            field_dict["documents"] = documents
        if links is not UNSET:
            field_dict["links"] = links
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.compound_date_range import CompoundDateRange
        from ..models.document import Document
        from ..models.evidence_contact_information import EvidenceContactInformation
        from ..models.identifier import Identifier
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        period = CompoundDateRange.from_dict(d.pop("period"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_evidence_indicator(
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

        evidence_indicator = _parse_evidence_indicator(
            d.pop("evidenceIndicator", UNSET)
        )

        def _parse_evidence_title(data: object) -> LocalizedStringType0 | None | Unset:
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

        evidence_title = _parse_evidence_title(d.pop("evidenceTitle", UNSET))

        def _parse_evidence_summary(
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

        evidence_summary = _parse_evidence_summary(d.pop("evidenceSummary", UNSET))

        _evidence_contact_information = d.pop("evidenceContactInformation", UNSET)
        evidence_contact_information: list[EvidenceContactInformation] | Unset = UNSET
        if _evidence_contact_information is not UNSET:
            evidence_contact_information = []
            for evidence_contact_information_item_data in _evidence_contact_information:
                evidence_contact_information_item = (
                    EvidenceContactInformation.from_dict(
                        evidence_contact_information_item_data
                    )
                )

                evidence_contact_information.append(evidence_contact_information_item)

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

        impact_evidence = cls(
            period=period,
            pure_id=pure_id,
            evidence_indicator=evidence_indicator,
            evidence_title=evidence_title,
            evidence_summary=evidence_summary,
            evidence_contact_information=evidence_contact_information,
            documents=documents,
            links=links,
            identifiers=identifiers,
        )

        impact_evidence.additional_properties = d
        return impact_evidence

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
