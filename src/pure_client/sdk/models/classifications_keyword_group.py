from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.identifier import Identifier
    from ..models.keyword_container import KeywordContainer
    from ..models.localized_string_type_0 import LocalizedStringType0


T = TypeVar("T", bound="ClassificationsKeywordGroup")


@_attrs_define
class ClassificationsKeywordGroup:
    """De-normalized version of the full keyword group representation for instances where only structured keywords can be
    selected

        Attributes:
            logical_name (str): Unique name of the configuration that specifies this keyword group
            type_discriminator (str):
            pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
            name (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
                invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
            identifiers (list[Identifier] | None | Unset): Identifiers related to the KeywordGroup.
            classifications (list[ClassificationRefType0 | None] | None | Unset): A list classifications extracted from the
                keyword group structured keyword concept
            keyword_containers (list[KeywordContainer] | None | Unset): Keyword containers with state and origin metadata
                (read-only). The flat classifications list determines which keywords exist on write; keywordContainers provides
                supplementary metadata (e.g. origin).
    """

    logical_name: str
    type_discriminator: str
    pure_id: int | Unset = UNSET
    name: LocalizedStringType0 | None | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    classifications: list[ClassificationRefType0 | None] | None | Unset = UNSET
    keyword_containers: list[KeywordContainer] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.localized_string_type_0 import LocalizedStringType0

        logical_name = self.logical_name

        type_discriminator = self.type_discriminator

        pure_id = self.pure_id

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, LocalizedStringType0):
            name = self.name.to_dict()
        else:
            name = self.name

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

        classifications: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.classifications, Unset):
            classifications = UNSET
        elif isinstance(self.classifications, list):
            classifications = []
            for classifications_type_0_item_data in self.classifications:
                classifications_type_0_item: dict[str, Any] | None
                if isinstance(classifications_type_0_item_data, ClassificationRefType0):
                    classifications_type_0_item = (
                        classifications_type_0_item_data.to_dict()
                    )
                else:
                    classifications_type_0_item = classifications_type_0_item_data
                classifications.append(classifications_type_0_item)

        else:
            classifications = self.classifications

        keyword_containers: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyword_containers, Unset):
            keyword_containers = UNSET
        elif isinstance(self.keyword_containers, list):
            keyword_containers = []
            for keyword_containers_type_0_item_data in self.keyword_containers:
                keyword_containers_type_0_item = (
                    keyword_containers_type_0_item_data.to_dict()
                )
                keyword_containers.append(keyword_containers_type_0_item)

        else:
            keyword_containers = self.keyword_containers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logicalName": logical_name,
                "typeDiscriminator": type_discriminator,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if name is not UNSET:
            field_dict["name"] = name
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if classifications is not UNSET:
            field_dict["classifications"] = classifications
        if keyword_containers is not UNSET:
            field_dict["keywordContainers"] = keyword_containers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.identifier import Identifier
        from ..models.keyword_container import KeywordContainer
        from ..models.localized_string_type_0 import LocalizedStringType0

        d = dict(src_dict)
        logical_name = d.pop("logicalName")

        type_discriminator = d.pop("typeDiscriminator")

        pure_id = d.pop("pureId", UNSET)

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

        def _parse_classifications(
            data: object,
        ) -> list[ClassificationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                classifications_type_0 = []
                _classifications_type_0 = data
                for classifications_type_0_item_data in _classifications_type_0:

                    def _parse_classifications_type_0_item(
                        data: object,
                    ) -> ClassificationRefType0 | None:
                        if data is None:
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
                        return cast(ClassificationRefType0 | None, data)

                    classifications_type_0_item = _parse_classifications_type_0_item(
                        classifications_type_0_item_data
                    )

                    classifications_type_0.append(classifications_type_0_item)

                return classifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassificationRefType0 | None] | None | Unset, data)

        classifications = _parse_classifications(d.pop("classifications", UNSET))

        def _parse_keyword_containers(
            data: object,
        ) -> list[KeywordContainer] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyword_containers_type_0 = []
                _keyword_containers_type_0 = data
                for keyword_containers_type_0_item_data in _keyword_containers_type_0:
                    keyword_containers_type_0_item = KeywordContainer.from_dict(
                        keyword_containers_type_0_item_data
                    )

                    keyword_containers_type_0.append(keyword_containers_type_0_item)

                return keyword_containers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeywordContainer] | None | Unset, data)

        keyword_containers = _parse_keyword_containers(
            d.pop("keywordContainers", UNSET)
        )

        classifications_keyword_group = cls(
            logical_name=logical_name,
            type_discriminator=type_discriminator,
            pure_id=pure_id,
            name=name,
            identifiers=identifiers,
            classifications=classifications,
            keyword_containers=keyword_containers,
        )

        classifications_keyword_group.additional_properties = d
        return classifications_keyword_group

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
