from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.journal_association_type_0 import JournalAssociationType0


T = TypeVar("T", bound="JournalEditorialWorkAssociation")


@_attrs_define
class JournalEditorialWorkAssociation:
    """An editorial work association with a journal.

    Attributes:
        type_discriminator (str):
        journal (JournalAssociationType0 | None): A journal associated with a research output.
    """

    type_discriminator: str
    journal: JournalAssociationType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.journal_association_type_0 import JournalAssociationType0

        type_discriminator = self.type_discriminator

        journal: dict[str, Any] | None
        if isinstance(self.journal, JournalAssociationType0):
            journal = self.journal.to_dict()
        else:
            journal = self.journal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "journal": journal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.journal_association_type_0 import JournalAssociationType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_journal(data: object) -> JournalAssociationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_journal_association_type_0 = (
                    JournalAssociationType0.from_dict(data)
                )

                return componentsschemas_journal_association_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JournalAssociationType0 | None, data)

        journal = _parse_journal(d.pop("journal"))

        journal_editorial_work_association = cls(
            type_discriminator=type_discriminator,
            journal=journal,
        )

        journal_editorial_work_association.additional_properties = d
        return journal_editorial_work_association

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
