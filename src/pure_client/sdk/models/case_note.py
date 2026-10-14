from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classified_case_note_source import ClassifiedCaseNoteSource
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="CaseNote")


@_attrs_define
class CaseNote:
    """A note on a case, detailing title, judgement data and court processing case.

    Attributes:
        court (ExternalOrganizationRefType0 | None): A reference to an organization external to the institution
        judgement_date (datetime.date): The judgement date.
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        title (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        sources (list[ClassifiedCaseNoteSource] | None | Unset): Classified case note sources
    """

    court: ExternalOrganizationRefType0 | None
    judgement_date: datetime.date
    pure_id: int | Unset = UNSET
    title: LocalizedStringType0 | None | Unset = UNSET
    sources: list[ClassifiedCaseNoteSource] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        court: dict[str, Any] | None
        if isinstance(self.court, ExternalOrganizationRefType0):
            court = self.court.to_dict()
        else:
            court = self.court

        judgement_date = self.judgement_date.isoformat()

        pure_id = self.pure_id

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "court": court,
                "judgementDate": judgement_date,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if title is not UNSET:
            field_dict["title"] = title
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classified_case_note_source import ClassifiedCaseNoteSource
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)

        def _parse_court(data: object) -> ExternalOrganizationRefType0 | None:
            if data is None:
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
            return cast(ExternalOrganizationRefType0 | None, data)

        court = _parse_court(d.pop("court"))

        judgement_date = isoparse(d.pop("judgementDate")).date()

        pure_id = d.pop("pureId", UNSET)

        def _parse_title(data: object) -> LocalizedStringType0 | None | Unset:
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

        title = _parse_title(d.pop("title", UNSET))

        def _parse_sources(
            data: object,
        ) -> list[ClassifiedCaseNoteSource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = ClassifiedCaseNoteSource.from_dict(
                        sources_type_0_item_data
                    )

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedCaseNoteSource] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

        case_note = cls(
            court=court,
            judgement_date=judgement_date,
            pure_id=pure_id,
            title=title,
            sources=sources,
        )

        case_note.additional_properties = d
        return case_note

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
