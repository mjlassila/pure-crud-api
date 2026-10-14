from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.publisher_ref_type_0 import PublisherRefType0


T = TypeVar("T", bound="PublisherEditorialWorkAssociation")


@_attrs_define
class PublisherEditorialWorkAssociation:
    """An editorial work association with a publisher.

    Attributes:
        type_discriminator (str):
        publisher (None | PublisherRefType0): A reference to a publisher
    """

    type_discriminator: str
    publisher: None | PublisherRefType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.publisher_ref_type_0 import PublisherRefType0

        type_discriminator = self.type_discriminator

        publisher: dict[str, Any] | None
        if isinstance(self.publisher, PublisherRefType0):
            publisher = self.publisher.to_dict()
        else:
            publisher = self.publisher

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeDiscriminator": type_discriminator,
                "publisher": publisher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.publisher_ref_type_0 import PublisherRefType0

        d = dict(src_dict)
        type_discriminator = d.pop("typeDiscriminator")

        def _parse_publisher(data: object) -> None | PublisherRefType0:
            if data is None:
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
            return cast(None | PublisherRefType0, data)

        publisher = _parse_publisher(d.pop("publisher"))

        publisher_editorial_work_association = cls(
            type_discriminator=type_discriminator,
            publisher=publisher,
        )

        publisher_editorial_work_association.additional_properties = d
        return publisher_editorial_work_association

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
