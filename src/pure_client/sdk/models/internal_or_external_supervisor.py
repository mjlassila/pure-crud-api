from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_person_ref_type_0 import ExternalPersonRefType0
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="InternalOrExternalSupervisor")


@_attrs_define
class InternalOrExternalSupervisor:
    """A supervisor, either internal or external, use as mutually exclusive

    Attributes:
        external_supervisor (ExternalPersonRefType0 | None | Unset): A reference to a person external to the institution
        supervisor (None | PersonRefType0 | Unset): A reference to a person internal to the institution
    """

    external_supervisor: ExternalPersonRefType0 | None | Unset = UNSET
    supervisor: None | PersonRefType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        external_supervisor: dict[str, Any] | None | Unset
        if isinstance(self.external_supervisor, Unset):
            external_supervisor = UNSET
        elif isinstance(self.external_supervisor, ExternalPersonRefType0):
            external_supervisor = self.external_supervisor.to_dict()
        else:
            external_supervisor = self.external_supervisor

        supervisor: dict[str, Any] | None | Unset
        if isinstance(self.supervisor, Unset):
            supervisor = UNSET
        elif isinstance(self.supervisor, PersonRefType0):
            supervisor = self.supervisor.to_dict()
        else:
            supervisor = self.supervisor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_supervisor is not UNSET:
            field_dict["externalSupervisor"] = external_supervisor
        if supervisor is not UNSET:
            field_dict["supervisor"] = supervisor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_person_ref_type_0 import ExternalPersonRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)

        def _parse_external_supervisor(
            data: object,
        ) -> ExternalPersonRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_external_person_ref_type_0 = (
                    ExternalPersonRefType0.from_dict(data)
                )

                return componentsschemas_external_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalPersonRefType0 | None | Unset, data)

        external_supervisor = _parse_external_supervisor(
            d.pop("externalSupervisor", UNSET)
        )

        def _parse_supervisor(data: object) -> None | PersonRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_person_ref_type_0 = PersonRefType0.from_dict(data)

                return componentsschemas_person_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonRefType0 | Unset, data)

        supervisor = _parse_supervisor(d.pop("supervisor", UNSET))

        internal_or_external_supervisor = cls(
            external_supervisor=external_supervisor,
            supervisor=supervisor,
        )

        internal_or_external_supervisor.additional_properties = d
        return internal_or_external_supervisor

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
