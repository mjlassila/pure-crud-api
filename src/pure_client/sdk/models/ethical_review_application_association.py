from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.application_ref_type_0 import ApplicationRefType0


T = TypeVar("T", bound="EthicalReviewApplicationAssociation")


@_attrs_define
class EthicalReviewApplicationAssociation:
    """An association with an application

    Attributes:
        application (ApplicationRefType0 | None): A reference to an application
    """

    application: ApplicationRefType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_ref_type_0 import ApplicationRefType0

        application: dict[str, Any] | None
        if isinstance(self.application, ApplicationRefType0):
            application = self.application.to_dict()
        else:
            application = self.application

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application": application,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_ref_type_0 import ApplicationRefType0

        d = dict(src_dict)

        def _parse_application(data: object) -> ApplicationRefType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_application_ref_type_0 = (
                    ApplicationRefType0.from_dict(data)
                )

                return componentsschemas_application_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicationRefType0 | None, data)

        application = _parse_application(d.pop("application"))

        ethical_review_application_association = cls(
            application=application,
        )

        ethical_review_application_association.additional_properties = d
        return ethical_review_application_association

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
