from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.organization_or_external_organization_ref_type_0 import (
        OrganizationOrExternalOrganizationRefType0,
    )
    from ..models.system_currency_amount import SystemCurrencyAmount


T = TypeVar("T", bound="EquipmentDetails")


@_attrs_define
class EquipmentDetails:
    """Details about a piece of equipment

    Attributes:
        name (FormattedLocalizedStringType0 | None): A set of localized strings that support formatting. Invalid locale
            values will be ignored. Example: {'en_GB': 'Some text'}.
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        identifiers (list[Identifier] | None | Unset): IDs associated with this object. Such as serial number,
            manufacturer id , internal id.
        acquisition_date (datetime.date | None | Unset): Acquisition date
        decommission_date (datetime.date | None | Unset): Decommission date
        value (SystemCurrencyAmount | Unset): A monetary value in the Pure installation's system currency as defined by
            the W3C's Payment Request standard: https://www.w3.org/TR/payment-request/#paymentcurrencyamount-dictionary
        manufacturers (list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset): A collection of
            manufacturers
    """

    name: FormattedLocalizedStringType0 | None
    pure_id: int | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    acquisition_date: datetime.date | None | Unset = UNSET
    decommission_date: datetime.date | None | Unset = UNSET
    value: SystemCurrencyAmount | Unset = UNSET
    manufacturers: (
        list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )

        name: dict[str, Any] | None
        if isinstance(self.name, FormattedLocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        pure_id = self.pure_id

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

        acquisition_date: None | str | Unset
        if isinstance(self.acquisition_date, Unset):
            acquisition_date = UNSET
        elif isinstance(self.acquisition_date, datetime.date):
            acquisition_date = self.acquisition_date.isoformat()
        else:
            acquisition_date = self.acquisition_date

        decommission_date: None | str | Unset
        if isinstance(self.decommission_date, Unset):
            decommission_date = UNSET
        elif isinstance(self.decommission_date, datetime.date):
            decommission_date = self.decommission_date.isoformat()
        else:
            decommission_date = self.decommission_date

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        manufacturers: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.manufacturers, Unset):
            manufacturers = UNSET
        elif isinstance(self.manufacturers, list):
            manufacturers = []
            for manufacturers_type_0_item_data in self.manufacturers:
                manufacturers_type_0_item: dict[str, Any] | None
                if isinstance(
                    manufacturers_type_0_item_data,
                    OrganizationOrExternalOrganizationRefType0,
                ):
                    manufacturers_type_0_item = manufacturers_type_0_item_data.to_dict()
                else:
                    manufacturers_type_0_item = manufacturers_type_0_item_data
                manufacturers.append(manufacturers_type_0_item)

        else:
            manufacturers = self.manufacturers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if acquisition_date is not UNSET:
            field_dict["acquisitionDate"] = acquisition_date
        if decommission_date is not UNSET:
            field_dict["decommissionDate"] = decommission_date
        if value is not UNSET:
            field_dict["value"] = value
        if manufacturers is not UNSET:
            field_dict["manufacturers"] = manufacturers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.organization_or_external_organization_ref_type_0 import (
            OrganizationOrExternalOrganizationRefType0,
        )
        from ..models.system_currency_amount import SystemCurrencyAmount

        d = dict(src_dict)

        def _parse_name(data: object) -> FormattedLocalizedStringType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_formatted_localized_string_type_0 = (
                    FormattedLocalizedStringType0.from_dict(data)
                )

                return componentsschemas_formatted_localized_string_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormattedLocalizedStringType0 | None, data)

        name = _parse_name(d.pop("name"))

        pure_id = d.pop("pureId", UNSET)

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

        def _parse_acquisition_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquisition_date_type_0 = isoparse(data).date()

                return acquisition_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        acquisition_date = _parse_acquisition_date(d.pop("acquisitionDate", UNSET))

        def _parse_decommission_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decommission_date_type_0 = isoparse(data).date()

                return decommission_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        decommission_date = _parse_decommission_date(d.pop("decommissionDate", UNSET))

        _value = d.pop("value", UNSET)
        value: SystemCurrencyAmount | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = SystemCurrencyAmount.from_dict(_value)

        def _parse_manufacturers(
            data: object,
        ) -> list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                manufacturers_type_0 = []
                _manufacturers_type_0 = data
                for manufacturers_type_0_item_data in _manufacturers_type_0:

                    def _parse_manufacturers_type_0_item(
                        data: object,
                    ) -> None | OrganizationOrExternalOrganizationRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_organization_or_external_organization_ref_type_0 = OrganizationOrExternalOrganizationRefType0.from_dict(
                                data
                            )

                            return componentsschemas_organization_or_external_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | OrganizationOrExternalOrganizationRefType0, data
                        )

                    manufacturers_type_0_item = _parse_manufacturers_type_0_item(
                        manufacturers_type_0_item_data
                    )

                    manufacturers_type_0.append(manufacturers_type_0_item)

                return manufacturers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | OrganizationOrExternalOrganizationRefType0] | None | Unset,
                data,
            )

        manufacturers = _parse_manufacturers(d.pop("manufacturers", UNSET))

        equipment_details = cls(
            name=name,
            pure_id=pure_id,
            identifiers=identifiers,
            acquisition_date=acquisition_date,
            decommission_date=decommission_date,
            value=value,
            manufacturers=manufacturers,
        )

        equipment_details.additional_properties = d
        return equipment_details

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
