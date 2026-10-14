from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_coverage_coverage_type import MediaCoverageCoverageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_press_media_person_association import (
        AbstractPressMediaPersonAssociation,
    )
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0


T = TypeVar("T", bound="MediaCoverage")


@_attrs_define
class MediaCoverage:
    """A press media coverage

    Attributes:
        coverage_type (MediaCoverageCoverageType): Type value for coverage
        date (datetime.date): The date this coverage referred the story of the press media
        pure_id (int | Unset): Pure database ID of the object, prefer using the UUID if it is present on the entity
        title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        description (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale. Note:
            invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        persons (list[AbstractPressMediaPersonAssociation] | Unset): Person
        url (None | str | Unset): URL related to the coverage
        medium (None | str | Unset): What medium the coverage is in
        media_type (ClassificationRefType0 | None | Unset): A reference to a classification value
        degree_of_recognition (ClassificationRefType0 | None | Unset): A reference to a classification value
        author_producer (None | str | Unset): The person who authored or produced the coverage
        duration_length_size (None | str | Unset): The extent of the Duration, length, or size of the coverage
        country (ClassificationRefType0 | None | Unset): A reference to a classification value
        subdivision (ClassificationRefType0 | None | Unset): A reference to a classification value
        organizations (list[None | OrganizationRefType0] | Unset): Organizations associated with the coverage
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): Organizations associated with
            the coverage, considered external to the system holder
    """

    coverage_type: MediaCoverageCoverageType
    date: datetime.date
    pure_id: int | Unset = UNSET
    title: FormattedLocalizedStringType0 | None | Unset = UNSET
    description: LocalizedStringType0 | None | Unset = UNSET
    persons: list[AbstractPressMediaPersonAssociation] | Unset = UNSET
    url: None | str | Unset = UNSET
    medium: None | str | Unset = UNSET
    media_type: ClassificationRefType0 | None | Unset = UNSET
    degree_of_recognition: ClassificationRefType0 | None | Unset = UNSET
    author_producer: None | str | Unset = UNSET
    duration_length_size: None | str | Unset = UNSET
    country: ClassificationRefType0 | None | Unset = UNSET
    subdivision: ClassificationRefType0 | None | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0

        coverage_type = self.coverage_type.value

        date = self.date.isoformat()

        pure_id = self.pure_id

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, FormattedLocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, LocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        persons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        medium: None | str | Unset
        if isinstance(self.medium, Unset):
            medium = UNSET
        else:
            medium = self.medium

        media_type: dict[str, Any] | None | Unset
        if isinstance(self.media_type, Unset):
            media_type = UNSET
        elif isinstance(self.media_type, ClassificationRefType0):
            media_type = self.media_type.to_dict()
        else:
            media_type = self.media_type

        degree_of_recognition: dict[str, Any] | None | Unset
        if isinstance(self.degree_of_recognition, Unset):
            degree_of_recognition = UNSET
        elif isinstance(self.degree_of_recognition, ClassificationRefType0):
            degree_of_recognition = self.degree_of_recognition.to_dict()
        else:
            degree_of_recognition = self.degree_of_recognition

        author_producer: None | str | Unset
        if isinstance(self.author_producer, Unset):
            author_producer = UNSET
        else:
            author_producer = self.author_producer

        duration_length_size: None | str | Unset
        if isinstance(self.duration_length_size, Unset):
            duration_length_size = UNSET
        else:
            duration_length_size = self.duration_length_size

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, ClassificationRefType0):
            country = self.country.to_dict()
        else:
            country = self.country

        subdivision: dict[str, Any] | None | Unset
        if isinstance(self.subdivision, Unset):
            subdivision = UNSET
        elif isinstance(self.subdivision, ClassificationRefType0):
            subdivision = self.subdivision.to_dict()
        else:
            subdivision = self.subdivision

        organizations: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item: dict[str, Any] | None
                if isinstance(organizations_item_data, OrganizationRefType0):
                    organizations_item = organizations_item_data.to_dict()
                else:
                    organizations_item = organizations_item_data
                organizations.append(organizations_item)

        external_organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.external_organizations, Unset):
            external_organizations = UNSET
        elif isinstance(self.external_organizations, list):
            external_organizations = []
            for external_organizations_type_0_item_data in self.external_organizations:
                external_organizations_type_0_item: dict[str, Any] | None
                if isinstance(
                    external_organizations_type_0_item_data,
                    ExternalOrganizationRefType0,
                ):
                    external_organizations_type_0_item = (
                        external_organizations_type_0_item_data.to_dict()
                    )
                else:
                    external_organizations_type_0_item = (
                        external_organizations_type_0_item_data
                    )
                external_organizations.append(external_organizations_type_0_item)

        else:
            external_organizations = self.external_organizations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coverageType": coverage_type,
                "date": date,
            }
        )
        if pure_id is not UNSET:
            field_dict["pureId"] = pure_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if persons is not UNSET:
            field_dict["persons"] = persons
        if url is not UNSET:
            field_dict["url"] = url
        if medium is not UNSET:
            field_dict["medium"] = medium
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if degree_of_recognition is not UNSET:
            field_dict["degreeOfRecognition"] = degree_of_recognition
        if author_producer is not UNSET:
            field_dict["authorProducer"] = author_producer
        if duration_length_size is not UNSET:
            field_dict["durationLengthSize"] = duration_length_size
        if country is not UNSET:
            field_dict["country"] = country
        if subdivision is not UNSET:
            field_dict["subdivision"] = subdivision
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_press_media_person_association import (
            AbstractPressMediaPersonAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0

        d = dict(src_dict)
        coverage_type = MediaCoverageCoverageType(d.pop("coverageType"))

        date = isoparse(d.pop("date")).date()

        pure_id = d.pop("pureId", UNSET)

        def _parse_title(data: object) -> FormattedLocalizedStringType0 | None | Unset:
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

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> LocalizedStringType0 | None | Unset:
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

        description = _parse_description(d.pop("description", UNSET))

        _persons = d.pop("persons", UNSET)
        persons: list[AbstractPressMediaPersonAssociation] | Unset = UNSET
        if _persons is not UNSET:
            persons = []
            for persons_item_data in _persons:
                persons_item = AbstractPressMediaPersonAssociation.from_dict(
                    persons_item_data
                )

                persons.append(persons_item)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium = _parse_medium(d.pop("medium", UNSET))

        def _parse_media_type(data: object) -> ClassificationRefType0 | None | Unset:
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

        media_type = _parse_media_type(d.pop("mediaType", UNSET))

        def _parse_degree_of_recognition(
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

        degree_of_recognition = _parse_degree_of_recognition(
            d.pop("degreeOfRecognition", UNSET)
        )

        def _parse_author_producer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_producer = _parse_author_producer(d.pop("authorProducer", UNSET))

        def _parse_duration_length_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duration_length_size = _parse_duration_length_size(
            d.pop("durationLengthSize", UNSET)
        )

        def _parse_country(data: object) -> ClassificationRefType0 | None | Unset:
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

        country = _parse_country(d.pop("country", UNSET))

        def _parse_subdivision(data: object) -> ClassificationRefType0 | None | Unset:
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

        subdivision = _parse_subdivision(d.pop("subdivision", UNSET))

        _organizations = d.pop("organizations", UNSET)
        organizations: list[None | OrganizationRefType0] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:

                def _parse_organizations_item(
                    data: object,
                ) -> None | OrganizationRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_organization_ref_type_0 = (
                            OrganizationRefType0.from_dict(data)
                        )

                        return componentsschemas_organization_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | OrganizationRefType0, data)

                organizations_item = _parse_organizations_item(organizations_item_data)

                organizations.append(organizations_item)

        def _parse_external_organizations(
            data: object,
        ) -> list[ExternalOrganizationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_organizations_type_0 = []
                _external_organizations_type_0 = data
                for (
                    external_organizations_type_0_item_data
                ) in _external_organizations_type_0:

                    def _parse_external_organizations_type_0_item(
                        data: object,
                    ) -> ExternalOrganizationRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_external_organization_ref_type_0 = (
                                ExternalOrganizationRefType0.from_dict(data)
                            )

                            return componentsschemas_external_organization_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ExternalOrganizationRefType0 | None, data)

                    external_organizations_type_0_item = (
                        _parse_external_organizations_type_0_item(
                            external_organizations_type_0_item_data
                        )
                    )

                    external_organizations_type_0.append(
                        external_organizations_type_0_item
                    )

                return external_organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalOrganizationRefType0 | None] | None | Unset, data)

        external_organizations = _parse_external_organizations(
            d.pop("externalOrganizations", UNSET)
        )

        media_coverage = cls(
            coverage_type=coverage_type,
            date=date,
            pure_id=pure_id,
            title=title,
            description=description,
            persons=persons,
            url=url,
            medium=medium,
            media_type=media_type,
            degree_of_recognition=degree_of_recognition,
            author_producer=author_producer,
            duration_length_size=duration_length_size,
            country=country,
            subdivision=subdivision,
            organizations=organizations,
            external_organizations=external_organizations,
        )

        media_coverage.additional_properties = d
        return media_coverage

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
