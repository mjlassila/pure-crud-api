from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.keyword_group_configuration_selection_mode_sorting_order import (
    KeywordGroupConfigurationSelectionModeSortingOrder,
)
from ..models.keyword_group_configuration_userdefined_keyword_edit_mode import (
    KeywordGroupConfigurationUserdefinedKeywordEditMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_scheme_ref_type_0 import ClassificationSchemeRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="KeywordGroupConfiguration")


@_attrs_define
class KeywordGroupConfiguration:
    """A specification of the allowed behavior of a specified keyword group

    Attributes:
        target_system_name (str): The content system name this configuration applies to
        logical_name (str): Defines a logical name for the group that makes it easy to find
        weight (int): Used to order keyword group configurations for the target family. Keyword groups will also be
            ordered in the contexts they appear in. The kKeyword group configuration with the highest weight value comes
            first.
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        uuid (UUID | Unset): UUID, this is the primary identity of the entity
        created_by (str | Unset): Username of creator
        created_date (datetime.datetime | Unset): Date and time of creation
        modified_by (str | Unset): Username of the user that performed a modification
        modified_date (datetime.datetime | Unset): Date and time of last modification
        portal_url (str | Unset): URL of the content on the Pure Portal
        pretty_url_identifiers (list[str] | Unset): All pretty URLs
        previous_uuids (list[str] | Unset): UUIDs of other content items which have been merged into this content item
            (or similar)
        version (None | str | Unset): Used to guard against conflicting updates. For new content this is null, and for
            existing content the current value. The property should never be modified by a client, except in the rare case
            where the client wants to perform an update irrespective of if other clients have made updates in the meantime,
            also known as a "dirty write". A dirty write is performed by not including the property value or setting the
            property to null
        identifiers (list[Identifier] | None | Unset): Identifiers related to the KeywordGroupConfiguration.
        keyword_group_type (str | Unset): The OpenAPI schema type of this keyword configuration
        name (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        description (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        classification_scheme (ClassificationSchemeRefType0 | None | Unset): A reference to a classification scheme
        allow_userdefined_keywords (bool | Unset): Defines if user defined keywords are allowed
        limit_to_leaf_selection (bool | Unset): Defines if selection of classifications is limited to leafs or also
            intermediate nodes
        min_amount_of_keywords (int | None | Unset): Used to set the minimum amount of keywords that has to be chosen
            from this keyword group
        max_amount_of_keywords (int | None | Unset): Used to set the maximum amount of keywords that can to be chosen
            from this keyword group
        modifying_roles (list[None | str] | None | Unset): List of roles that may modify this keyword group where it is
            in use on some content. An empty set indicates there is no limit on which roles may edit the group
        userdefined_keyword_edit_mode (KeywordGroupConfigurationUserdefinedKeywordEditMode | Unset): User defined
            keyword edit mode
        selection_mode_sorting_order (KeywordGroupConfigurationSelectionModeSortingOrder | Unset): Select sorting order
            of in the selection mode
        tags (list[str] | Unset): A list of tags that can be used to identify this group. Any string can be used as a
            tag, but there are a few strings that have a special interpretation: 1) 'visible-on-portal' - keywords are shown
            in the portal, 2) 'visible-in-ws' - keywords are accessible through the web service, 3) 'visible-in-long-
            renderers' - keywords are shown in long renderings of content, 4) 'show-filter-on-portal' - there will be a
            filter option for keywords of this group on the portal.
        relation_type (None | str | Unset): The schema name of the type (with the ability to associate keywords) on
            which the keyword group configuration is related to, e.g. StaffOrganizationAssociation. It can also be set to
            null (default value), which means the keyword group configuration is related to the main type (the target system
            name) and not a relation of the main type.
        system_name (str | Unset): The content system name
    """

    target_system_name: str
    logical_name: str
    weight: int
    pure_id: int | Unset = UNSET
    uuid: UUID | Unset = UNSET
    created_by: str | Unset = UNSET
    created_date: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    portal_url: str | Unset = UNSET
    pretty_url_identifiers: list[str] | Unset = UNSET
    previous_uuids: list[str] | Unset = UNSET
    version: None | str | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    keyword_group_type: str | Unset = UNSET
    name: LocalizedStringType0 | None | Unset = UNSET
    description: FormattedLocalizedStringType0 | None | Unset = UNSET
    classification_scheme: ClassificationSchemeRefType0 | None | Unset = UNSET
    allow_userdefined_keywords: bool | Unset = UNSET
    limit_to_leaf_selection: bool | Unset = UNSET
    min_amount_of_keywords: int | None | Unset = UNSET
    max_amount_of_keywords: int | None | Unset = UNSET
    modifying_roles: list[None | str] | None | Unset = UNSET
    userdefined_keyword_edit_mode: (
        KeywordGroupConfigurationUserdefinedKeywordEditMode | Unset
    ) = UNSET
    selection_mode_sorting_order: (
        KeywordGroupConfigurationSelectionModeSortingOrder | Unset
    ) = UNSET
    tags: list[str] | Unset = UNSET
    relation_type: None | str | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_scheme_ref_type_0 import (
            ClassificationSchemeRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0

        target_system_name = self.target_system_name

        logical_name = self.logical_name

        weight = self.weight

        pure_id = self.pure_id

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        created_by = self.created_by

        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        modified_by = self.modified_by

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        portal_url = self.portal_url

        pretty_url_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pretty_url_identifiers, Unset):
            pretty_url_identifiers = self.pretty_url_identifiers

        previous_uuids: list[str] | Unset = UNSET
        if not isinstance(self.previous_uuids, Unset):
            previous_uuids = self.previous_uuids

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

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

        keyword_group_type = self.keyword_group_type

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, LocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, FormattedLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        classification_scheme: dict[str, Any] | None | Unset
        if isinstance(self.classification_scheme, Unset):
            classification_scheme = UNSET
        elif isinstance(self.classification_scheme, ClassificationSchemeRefType0):
            classification_scheme = self.classification_scheme.to_dict()
        else:
            classification_scheme = self.classification_scheme

        allow_userdefined_keywords = self.allow_userdefined_keywords

        limit_to_leaf_selection = self.limit_to_leaf_selection

        min_amount_of_keywords: int | None | Unset
        if isinstance(self.min_amount_of_keywords, Unset):
            min_amount_of_keywords = UNSET
        else:
            min_amount_of_keywords = self.min_amount_of_keywords

        max_amount_of_keywords: int | None | Unset
        if isinstance(self.max_amount_of_keywords, Unset):
            max_amount_of_keywords = UNSET
        else:
            max_amount_of_keywords = self.max_amount_of_keywords

        modifying_roles: list[None | str] | None | Unset
        if isinstance(self.modifying_roles, Unset):
            modifying_roles = UNSET
        elif isinstance(self.modifying_roles, list):
            modifying_roles = []
            for modifying_roles_type_0_item_data in self.modifying_roles:
                modifying_roles_type_0_item: None | str
                modifying_roles_type_0_item = modifying_roles_type_0_item_data
                modifying_roles.append(modifying_roles_type_0_item)

        else:
            modifying_roles = self.modifying_roles

        userdefined_keyword_edit_mode: str | Unset = UNSET
        if not isinstance(self.userdefined_keyword_edit_mode, Unset):
            userdefined_keyword_edit_mode = self.userdefined_keyword_edit_mode.value

        selection_mode_sorting_order: str | Unset = UNSET
        if not isinstance(self.selection_mode_sorting_order, Unset):
            selection_mode_sorting_order = self.selection_mode_sorting_order.value

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        relation_type: None | str | Unset
        if isinstance(self.relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = self.relation_type

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetSystemName": target_system_name,
                "logicalName": logical_name,
                "weight": weight,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if portal_url is not UNSET:
            field_dict["portalUrl"] = portal_url
        if pretty_url_identifiers is not UNSET:
            field_dict["prettyUrlIdentifiers"] = pretty_url_identifiers
        if previous_uuids is not UNSET:
            field_dict["previousUuids"] = previous_uuids
        if version is not UNSET:
            field_dict["version"] = version
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if keyword_group_type is not UNSET:
            field_dict["keywordGroupType"] = keyword_group_type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if classification_scheme is not UNSET:
            field_dict["classificationScheme"] = classification_scheme
        if allow_userdefined_keywords is not UNSET:
            field_dict["allowUserdefinedKeywords"] = allow_userdefined_keywords
        if limit_to_leaf_selection is not UNSET:
            field_dict["limitToLeafSelection"] = limit_to_leaf_selection
        if min_amount_of_keywords is not UNSET:
            field_dict["minAmountOfKeywords"] = min_amount_of_keywords
        if max_amount_of_keywords is not UNSET:
            field_dict["maxAmountOfKeywords"] = max_amount_of_keywords
        if modifying_roles is not UNSET:
            field_dict["modifyingRoles"] = modifying_roles
        if userdefined_keyword_edit_mode is not UNSET:
            field_dict["userdefinedKeywordEditMode"] = userdefined_keyword_edit_mode
        if selection_mode_sorting_order is not UNSET:
            field_dict["selectionModeSortingOrder"] = selection_mode_sorting_order
        if tags is not UNSET:
            field_dict["tags"] = tags
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_scheme_ref_type_0 import (
            ClassificationSchemeRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        target_system_name = d.pop("targetSystemName")

        logical_name = d.pop("logicalName")

        weight = d.pop("weight")

        pure_id = d.pop("pureId", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        created_by = d.pop("createdBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        modified_by = d.pop("modifiedBy", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        portal_url = d.pop("portalUrl", UNSET)

        pretty_url_identifiers = cast(list[str], d.pop("prettyUrlIdentifiers", UNSET))

        previous_uuids = cast(list[str], d.pop("previousUuids", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

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

        keyword_group_type = d.pop("keywordGroupType", UNSET)

        def _parse_name(data: object) -> LocalizedStringType0 | None | Unset:
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

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(
            data: object,
        ) -> FormattedLocalizedStringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(FormattedLocalizedStringType0 | None | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_classification_scheme(
            data: object,
        ) -> ClassificationSchemeRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_classification_scheme_ref_type_0 = (
                    ClassificationSchemeRefType0.from_dict(data)
                )

                return componentsschemas_classification_scheme_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClassificationSchemeRefType0 | None | Unset, data)

        classification_scheme = _parse_classification_scheme(
            d.pop("classificationScheme", UNSET)
        )

        allow_userdefined_keywords = d.pop("allowUserdefinedKeywords", UNSET)

        limit_to_leaf_selection = d.pop("limitToLeafSelection", UNSET)

        def _parse_min_amount_of_keywords(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_amount_of_keywords = _parse_min_amount_of_keywords(
            d.pop("minAmountOfKeywords", UNSET)
        )

        def _parse_max_amount_of_keywords(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_amount_of_keywords = _parse_max_amount_of_keywords(
            d.pop("maxAmountOfKeywords", UNSET)
        )

        def _parse_modifying_roles(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modifying_roles_type_0 = []
                _modifying_roles_type_0 = data
                for modifying_roles_type_0_item_data in _modifying_roles_type_0:

                    def _parse_modifying_roles_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    modifying_roles_type_0_item = _parse_modifying_roles_type_0_item(
                        modifying_roles_type_0_item_data
                    )

                    modifying_roles_type_0.append(modifying_roles_type_0_item)

                return modifying_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        modifying_roles = _parse_modifying_roles(d.pop("modifyingRoles", UNSET))

        _userdefined_keyword_edit_mode = d.pop("userdefinedKeywordEditMode", UNSET)
        userdefined_keyword_edit_mode: (
            KeywordGroupConfigurationUserdefinedKeywordEditMode | Unset
        )
        if isinstance(_userdefined_keyword_edit_mode, Unset):
            userdefined_keyword_edit_mode = UNSET
        else:
            userdefined_keyword_edit_mode = (
                KeywordGroupConfigurationUserdefinedKeywordEditMode(
                    _userdefined_keyword_edit_mode
                )
            )

        _selection_mode_sorting_order = d.pop("selectionModeSortingOrder", UNSET)
        selection_mode_sorting_order: (
            KeywordGroupConfigurationSelectionModeSortingOrder | Unset
        )
        if isinstance(_selection_mode_sorting_order, Unset):
            selection_mode_sorting_order = UNSET
        else:
            selection_mode_sorting_order = (
                KeywordGroupConfigurationSelectionModeSortingOrder(
                    _selection_mode_sorting_order
                )
            )

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_relation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation_type = _parse_relation_type(d.pop("relationType", UNSET))

        system_name = d.pop("systemName", UNSET)

        keyword_group_configuration = cls(
            target_system_name=target_system_name,
            logical_name=logical_name,
            weight=weight,
            pure_id=pure_id,
            uuid=uuid,
            created_by=created_by,
            created_date=created_date,
            modified_by=modified_by,
            modified_date=modified_date,
            portal_url=portal_url,
            pretty_url_identifiers=pretty_url_identifiers,
            previous_uuids=previous_uuids,
            version=version,
            identifiers=identifiers,
            keyword_group_type=keyword_group_type,
            name=name,
            description=description,
            classification_scheme=classification_scheme,
            allow_userdefined_keywords=allow_userdefined_keywords,
            limit_to_leaf_selection=limit_to_leaf_selection,
            min_amount_of_keywords=min_amount_of_keywords,
            max_amount_of_keywords=max_amount_of_keywords,
            modifying_roles=modifying_roles,
            userdefined_keyword_edit_mode=userdefined_keyword_edit_mode,
            selection_mode_sorting_order=selection_mode_sorting_order,
            tags=tags,
            relation_type=relation_type,
            system_name=system_name,
        )

        keyword_group_configuration.additional_properties = d
        return keyword_group_configuration

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
