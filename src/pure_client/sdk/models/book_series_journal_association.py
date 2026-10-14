from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issn_ref import ISSNRef
    from ..models.journal_ref_type_0 import JournalRefType0
    from ..models.journal_title_ref import JournalTitleRef


T = TypeVar("T", bound="BookSeriesJournalAssociation")


@_attrs_define
class BookSeriesJournalAssociation:
    """A relation describing the association between a book series and the associated journal.

    Attributes:
        journal (JournalRefType0 | None): A reference to a Journal
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        title (JournalTitleRef | Unset): A reference to a journal title
        issn (ISSNRef | Unset): A reference to a journal ISSN
        no (str | Unset):
        volume (str | Unset):
    """

    journal: JournalRefType0 | None
    pure_id: int | Unset = UNSET
    title: JournalTitleRef | Unset = UNSET
    issn: ISSNRef | Unset = UNSET
    no: str | Unset = UNSET
    volume: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.journal_ref_type_0 import JournalRefType0

        journal: dict[str, Any] | None
        if isinstance(self.journal, JournalRefType0):
            journal = self.journal.to_dict()
        else:
            journal = self.journal

        pure_id = self.pure_id

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        issn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issn, Unset):
            issn = self.issn.to_dict()

        no = self.no

        volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "journal": journal,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if title is not UNSET:
            field_dict["title"] = title
        if issn is not UNSET:
            field_dict["issn"] = issn
        if no is not UNSET:
            field_dict["no"] = no
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issn_ref import ISSNRef
        from ..models.journal_ref_type_0 import JournalRefType0
        from ..models.journal_title_ref import JournalTitleRef

        d = dict(src_dict)

        def _parse_journal(data: object) -> JournalRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_journal_ref_type_0 = JournalRefType0.from_dict(data)

                return componentsschemas_journal_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JournalRefType0 | None, data)

        journal = _parse_journal(d.pop("journal"))

        pure_id = d.pop("pureId", UNSET)

        _title = d.pop("title", UNSET)
        title: JournalTitleRef | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = JournalTitleRef.from_dict(_title)

        _issn = d.pop("issn", UNSET)
        issn: ISSNRef | Unset
        if isinstance(_issn, Unset):
            issn = UNSET
        else:
            issn = ISSNRef.from_dict(_issn)

        no = d.pop("no", UNSET)

        volume = d.pop("volume", UNSET)

        book_series_journal_association = cls(
            journal=journal,
            pure_id=pure_id,
            title=title,
            issn=issn,
            no=no,
            volume=volume,
        )

        book_series_journal_association.additional_properties = d
        return book_series_journal_association

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
