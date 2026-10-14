from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_version import ArticleVersion


T = TypeVar("T", bound="SherpaRomeoOpenAccessPermissionType0")


@_attrs_define
class SherpaRomeoOpenAccessPermissionType0:
    """Describes a SHERPA RoMEO access permissions object used in a policy.

    Attributes:
        article_version (ArticleVersion): Version of an article
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        licenses (list[None | str] | None | Unset): The licenses the article must adhere to.
        conditions (list[None | str] | None | Unset): Any conditions that must be fulfilled.
        prerequisites (list[None | str] | None | Unset): Any prerequisites that must be fulfilled.
        funder_prerequisites (list[None | str] | None | Unset): Any funder prerequisites that must be fulfilled.
        subject_prerequisites (list[None | str] | None | Unset): Any subject prerequisites that must be fulfilled.
        locations (list[None | str] | None | Unset): Locations where the article is permitted to be placed.
        publisher_deposits (list[None | str] | None | Unset): The location(s) the publisher will automatically deposit
            the article into.
        additional_fee (bool | Unset): If an additional fee is required to make the article Open Access.
        embargo (None | str | Unset): How long the article should be embargoed. Will be a number follow by a unit -
            days, months or years.
    """

    article_version: ArticleVersion
    pure_id: int | Unset = UNSET
    licenses: list[None | str] | None | Unset = UNSET
    conditions: list[None | str] | None | Unset = UNSET
    prerequisites: list[None | str] | None | Unset = UNSET
    funder_prerequisites: list[None | str] | None | Unset = UNSET
    subject_prerequisites: list[None | str] | None | Unset = UNSET
    locations: list[None | str] | None | Unset = UNSET
    publisher_deposits: list[None | str] | None | Unset = UNSET
    additional_fee: bool | Unset = UNSET
    embargo: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article_version = self.article_version.to_dict()

        pure_id = self.pure_id

        licenses: list[None | str] | None | Unset
        if isinstance(self.licenses, Unset):
            licenses = UNSET
        elif isinstance(self.licenses, list):
            licenses = []
            for licenses_type_0_item_data in self.licenses:
                licenses_type_0_item: None | str
                licenses_type_0_item = licenses_type_0_item_data
                licenses.append(licenses_type_0_item)

        else:
            licenses = self.licenses

        conditions: list[None | str] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item: None | str
                conditions_type_0_item = conditions_type_0_item_data
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        prerequisites: list[None | str] | None | Unset
        if isinstance(self.prerequisites, Unset):
            prerequisites = UNSET
        elif isinstance(self.prerequisites, list):
            prerequisites = []
            for prerequisites_type_0_item_data in self.prerequisites:
                prerequisites_type_0_item: None | str
                prerequisites_type_0_item = prerequisites_type_0_item_data
                prerequisites.append(prerequisites_type_0_item)

        else:
            prerequisites = self.prerequisites

        funder_prerequisites: list[None | str] | None | Unset
        if isinstance(self.funder_prerequisites, Unset):
            funder_prerequisites = UNSET
        elif isinstance(self.funder_prerequisites, list):
            funder_prerequisites = []
            for funder_prerequisites_type_0_item_data in self.funder_prerequisites:
                funder_prerequisites_type_0_item: None | str
                funder_prerequisites_type_0_item = funder_prerequisites_type_0_item_data
                funder_prerequisites.append(funder_prerequisites_type_0_item)

        else:
            funder_prerequisites = self.funder_prerequisites

        subject_prerequisites: list[None | str] | None | Unset
        if isinstance(self.subject_prerequisites, Unset):
            subject_prerequisites = UNSET
        elif isinstance(self.subject_prerequisites, list):
            subject_prerequisites = []
            for subject_prerequisites_type_0_item_data in self.subject_prerequisites:
                subject_prerequisites_type_0_item: None | str
                subject_prerequisites_type_0_item = (
                    subject_prerequisites_type_0_item_data
                )
                subject_prerequisites.append(subject_prerequisites_type_0_item)

        else:
            subject_prerequisites = self.subject_prerequisites

        locations: list[None | str] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item: None | str
                locations_type_0_item = locations_type_0_item_data
                locations.append(locations_type_0_item)

        else:
            locations = self.locations

        publisher_deposits: list[None | str] | None | Unset
        if isinstance(self.publisher_deposits, Unset):
            publisher_deposits = UNSET
        elif isinstance(self.publisher_deposits, list):
            publisher_deposits = []
            for publisher_deposits_type_0_item_data in self.publisher_deposits:
                publisher_deposits_type_0_item: None | str
                publisher_deposits_type_0_item = publisher_deposits_type_0_item_data
                publisher_deposits.append(publisher_deposits_type_0_item)

        else:
            publisher_deposits = self.publisher_deposits

        additional_fee = self.additional_fee

        embargo: None | str | Unset
        if isinstance(self.embargo, Unset):
            embargo = UNSET
        else:
            embargo = self.embargo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "articleVersion": article_version,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if prerequisites is not UNSET:
            field_dict["prerequisites"] = prerequisites
        if funder_prerequisites is not UNSET:
            field_dict["funderPrerequisites"] = funder_prerequisites
        if subject_prerequisites is not UNSET:
            field_dict["subjectPrerequisites"] = subject_prerequisites
        if locations is not UNSET:
            field_dict["locations"] = locations
        if publisher_deposits is not UNSET:
            field_dict["publisherDeposits"] = publisher_deposits
        if additional_fee is not UNSET:
            field_dict["additionalFee"] = additional_fee
        if embargo is not UNSET:
            field_dict["embargo"] = embargo

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.article_version import ArticleVersion

        d = dict(src_dict)
        article_version = ArticleVersion.from_dict(d.pop("articleVersion"))

        pure_id = d.pop("pureId", UNSET)

        def _parse_licenses(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                licenses_type_0 = []
                _licenses_type_0 = data
                for licenses_type_0_item_data in _licenses_type_0:

                    def _parse_licenses_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    licenses_type_0_item = _parse_licenses_type_0_item(
                        licenses_type_0_item_data
                    )

                    licenses_type_0.append(licenses_type_0_item)

                return licenses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        licenses = _parse_licenses(d.pop("licenses", UNSET))

        def _parse_conditions(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:

                    def _parse_conditions_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    conditions_type_0_item = _parse_conditions_type_0_item(
                        conditions_type_0_item_data
                    )

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_prerequisites(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prerequisites_type_0 = []
                _prerequisites_type_0 = data
                for prerequisites_type_0_item_data in _prerequisites_type_0:

                    def _parse_prerequisites_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    prerequisites_type_0_item = _parse_prerequisites_type_0_item(
                        prerequisites_type_0_item_data
                    )

                    prerequisites_type_0.append(prerequisites_type_0_item)

                return prerequisites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        prerequisites = _parse_prerequisites(d.pop("prerequisites", UNSET))

        def _parse_funder_prerequisites(
            data: object,
        ) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funder_prerequisites_type_0 = []
                _funder_prerequisites_type_0 = data
                for (
                    funder_prerequisites_type_0_item_data
                ) in _funder_prerequisites_type_0:

                    def _parse_funder_prerequisites_type_0_item(
                        data: object,
                    ) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    funder_prerequisites_type_0_item = (
                        _parse_funder_prerequisites_type_0_item(
                            funder_prerequisites_type_0_item_data
                        )
                    )

                    funder_prerequisites_type_0.append(funder_prerequisites_type_0_item)

                return funder_prerequisites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        funder_prerequisites = _parse_funder_prerequisites(
            d.pop("funderPrerequisites", UNSET)
        )

        def _parse_subject_prerequisites(
            data: object,
        ) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subject_prerequisites_type_0 = []
                _subject_prerequisites_type_0 = data
                for (
                    subject_prerequisites_type_0_item_data
                ) in _subject_prerequisites_type_0:

                    def _parse_subject_prerequisites_type_0_item(
                        data: object,
                    ) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    subject_prerequisites_type_0_item = (
                        _parse_subject_prerequisites_type_0_item(
                            subject_prerequisites_type_0_item_data
                        )
                    )

                    subject_prerequisites_type_0.append(
                        subject_prerequisites_type_0_item
                    )

                return subject_prerequisites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        subject_prerequisites = _parse_subject_prerequisites(
            d.pop("subjectPrerequisites", UNSET)
        )

        def _parse_locations(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in _locations_type_0:

                    def _parse_locations_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    locations_type_0_item = _parse_locations_type_0_item(
                        locations_type_0_item_data
                    )

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))

        def _parse_publisher_deposits(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                publisher_deposits_type_0 = []
                _publisher_deposits_type_0 = data
                for publisher_deposits_type_0_item_data in _publisher_deposits_type_0:

                    def _parse_publisher_deposits_type_0_item(
                        data: object,
                    ) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    publisher_deposits_type_0_item = (
                        _parse_publisher_deposits_type_0_item(
                            publisher_deposits_type_0_item_data
                        )
                    )

                    publisher_deposits_type_0.append(publisher_deposits_type_0_item)

                return publisher_deposits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        publisher_deposits = _parse_publisher_deposits(
            d.pop("publisherDeposits", UNSET)
        )

        additional_fee = d.pop("additionalFee", UNSET)

        def _parse_embargo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embargo = _parse_embargo(d.pop("embargo", UNSET))

        sherpa_romeo_open_access_permission_type_0 = cls(
            article_version=article_version,
            pure_id=pure_id,
            licenses=licenses,
            conditions=conditions,
            prerequisites=prerequisites,
            funder_prerequisites=funder_prerequisites,
            subject_prerequisites=subject_prerequisites,
            locations=locations,
            publisher_deposits=publisher_deposits,
            additional_fee=additional_fee,
            embargo=embargo,
        )

        sherpa_romeo_open_access_permission_type_0.additional_properties = d
        return sherpa_romeo_open_access_permission_type_0

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
