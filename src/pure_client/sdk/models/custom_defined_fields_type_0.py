from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_defined_field_type_0 import CustomDefinedFieldType0


T = TypeVar("T", bound="CustomDefinedFieldsType0")


@_attrs_define
class CustomDefinedFieldsType0:
    """Map of CustomDefinedField values, where the key is the field identifier

    Example:
        { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}

    """

    additional_properties: dict[str, CustomDefinedFieldType0 | None] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_defined_field_type_0 import CustomDefinedFieldType0

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, CustomDefinedFieldType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_defined_field_type_0 import CustomDefinedFieldType0

        d = dict(src_dict)
        custom_defined_fields_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> CustomDefinedFieldType0 | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_custom_defined_field_type_0 = (
                        CustomDefinedFieldType0.from_dict(data)
                    )

                    return componentsschemas_custom_defined_field_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(CustomDefinedFieldType0 | None, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        custom_defined_fields_type_0.additional_properties = additional_properties
        return custom_defined_fields_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CustomDefinedFieldType0 | None:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CustomDefinedFieldType0 | None) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
