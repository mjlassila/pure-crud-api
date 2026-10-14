from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.date_range import DateRange
    from ..models.person_ref_type_0 import PersonRefType0


T = TypeVar("T", bound="PersonSuperviseeAssociation")


@_attrs_define
class PersonSuperviseeAssociation:
    """Association between a person and their supervisee

    Attributes:
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        period (DateRange | Unset): A date range
        supervision_percentage (int | Unset): Percentage for which the Supervisor is responsible for the total
            supervision
        supervisor_role (ClassificationRefType0 | None | Unset): A reference to a classification value
        supervisee (None | PersonRefType0 | Unset): A reference to a person internal to the institution
    """

    pure_id: int | Unset = UNSET
    period: DateRange | Unset = UNSET
    supervision_percentage: int | Unset = UNSET
    supervisor_role: ClassificationRefType0 | None | Unset = UNSET
    supervisee: None | PersonRefType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.person_ref_type_0 import PersonRefType0

        pure_id = self.pure_id

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        supervision_percentage = self.supervision_percentage

        supervisor_role: dict[str, Any] | None | Unset
        if isinstance(self.supervisor_role, Unset):
            supervisor_role = UNSET
        elif isinstance(self.supervisor_role, ClassificationRefType0):
            supervisor_role = self.supervisor_role.to_dict()
        else:
            supervisor_role = self.supervisor_role

        supervisee: dict[str, Any] | None | Unset
        if isinstance(self.supervisee, Unset):
            supervisee = UNSET
        elif isinstance(self.supervisee, PersonRefType0):
            supervisee = self.supervisee.to_dict()
        else:
            supervisee = self.supervisee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if period is not UNSET:
            field_dict["period"] = period
        if supervision_percentage is not UNSET:
            field_dict["supervisionPercentage"] = supervision_percentage
        if supervisor_role is not UNSET:
            field_dict["supervisorRole"] = supervisor_role
        if supervisee is not UNSET:
            field_dict["supervisee"] = supervisee

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.date_range import DateRange
        from ..models.person_ref_type_0 import PersonRefType0

        d = dict(src_dict)
        pure_id = d.pop("pureId", UNSET)

        _period = d.pop("period", UNSET)
        period: DateRange | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = DateRange.from_dict(_period)

        supervision_percentage = d.pop("supervisionPercentage", UNSET)

        def _parse_supervisor_role(
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

        supervisor_role = _parse_supervisor_role(d.pop("supervisorRole", UNSET))

        def _parse_supervisee(data: object) -> None | PersonRefType0 | Unset:
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

        supervisee = _parse_supervisee(d.pop("supervisee", UNSET))

        person_supervisee_association = cls(
            pure_id=pure_id,
            period=period,
            supervision_percentage=supervision_percentage,
            supervisor_role=supervisor_role,
            supervisee=supervisee,
        )

        person_supervisee_association.additional_properties = d
        return person_supervisee_association

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
