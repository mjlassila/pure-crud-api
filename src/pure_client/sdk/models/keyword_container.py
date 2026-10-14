from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.keyword import Keyword


T = TypeVar("T", bound="KeywordContainer")


@_attrs_define
class KeywordContainer:
    """Container for a structured keyword and/or free keywords

    Attributes:
        structured_keyword (ClassificationRefType0 | None): A reference to a classification value
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        state (None | str | Unset): State of the keyword container. Indicates whether the keyword is accepted (ACCEPTED)
            or auto-accepted (AUTO_ACCEPTED).
        origin (None | str | Unset): Origin of the keyword container indicating how it was created. Possible values:
            USER_SUPPLIED (manually added), PROPAGATED. Defaults to USER_SUPPLIED when not specified on write.
        free_keywords (list[Keyword] | None | Unset): Free keywords
    """

    structured_keyword: ClassificationRefType0 | None
    pure_id: int | Unset = UNSET
    state: None | str | Unset = UNSET
    origin: None | str | Unset = UNSET
    free_keywords: list[Keyword] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0

        structured_keyword: dict[str, Any] | None
        if isinstance(self.structured_keyword, ClassificationRefType0):
            structured_keyword = self.structured_keyword.to_dict()
        else:
            structured_keyword = self.structured_keyword

        pure_id = self.pure_id

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        free_keywords: list[dict[str, Any]] | None | Unset
        if isinstance(self.free_keywords, Unset):
            free_keywords = UNSET
        elif isinstance(self.free_keywords, list):
            free_keywords = []
            for free_keywords_type_0_item_data in self.free_keywords:
                free_keywords_type_0_item = free_keywords_type_0_item_data.to_dict()
                free_keywords.append(free_keywords_type_0_item)

        else:
            free_keywords = self.free_keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "structuredKeyword": structured_keyword,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if state is not UNSET:
            field_dict["state"] = state
        if origin is not UNSET:
            field_dict["origin"] = origin
        if free_keywords is not UNSET:
            field_dict["freeKeywords"] = free_keywords

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.keyword import Keyword

        d = dict(src_dict)

        def _parse_structured_keyword(data: object) -> ClassificationRefType0 | None:
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

        structured_keyword = _parse_structured_keyword(d.pop("structuredKeyword"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_free_keywords(data: object) -> list[Keyword] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                free_keywords_type_0 = []
                _free_keywords_type_0 = data
                for free_keywords_type_0_item_data in _free_keywords_type_0:
                    free_keywords_type_0_item = Keyword.from_dict(
                        free_keywords_type_0_item_data
                    )

                    free_keywords_type_0.append(free_keywords_type_0_item)

                return free_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Keyword] | None | Unset, data)

        free_keywords = _parse_free_keywords(d.pop("freeKeywords", UNSET))

        keyword_container = cls(
            structured_keyword=structured_keyword,
            pure_id=pure_id,
            state=state,
            origin=origin,
            free_keywords=free_keywords,
        )

        keyword_container.additional_properties = d
        return keyword_container

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
