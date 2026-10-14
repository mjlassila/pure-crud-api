from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_contributor_association import AbstractContributorAssociation
    from ..models.activity_ref_type_0 import ActivityRefType0
    from ..models.additional_file_electronic_version import (
        AdditionalFileElectronicVersion,
    )
    from ..models.article_processing_charge import ArticleProcessingCharge
    from ..models.book_series_journal_association import BookSeriesJournalAssociation
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.classified_formatted_localized_value import (
        ClassifiedFormattedLocalizedValue,
    )
    from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
    from ..models.electronic_version_type_0 import ElectronicVersionType0
    from ..models.equipment_ref_type_0 import EquipmentRefType0
    from ..models.external_organization_ref_type_0 import ExternalOrganizationRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.formatted_string import FormattedString
    from ..models.funding_details import FundingDetails
    from ..models.identifier import Identifier
    from ..models.image_file import ImageFile
    from ..models.keyword_group import KeywordGroup
    from ..models.link import Link
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.organization_ref_type_0 import OrganizationRefType0
    from ..models.project_awardable_association_type_0 import (
        ProjectAwardableAssociationType0,
    )
    from ..models.publication_series import PublicationSeries
    from ..models.publication_status import PublicationStatus
    from ..models.research_output_association_type_0 import (
        ResearchOutputAssociationType0,
    )
    from ..models.research_output_data_set_association_type_0 import (
        ResearchOutputDataSetAssociationType0,
    )
    from ..models.research_output_impact_association_type_0 import (
        ResearchOutputImpactAssociationType0,
    )
    from ..models.research_output_press_media_association_type_0 import (
        ResearchOutputPressMediaAssociationType0,
    )
    from ..models.research_output_prize_association_type_0 import (
        ResearchOutputPrizeAssociationType0,
    )
    from ..models.research_output_student_thesis_association_type_0 import (
        ResearchOutputStudentThesisAssociationType0,
    )
    from ..models.visibility import Visibility
    from ..models.workflow import Workflow


T = TypeVar("T", bound="Memorandum")


@_attrs_define
class Memorandum:
    """A memorandum or exposition.

    Attributes:
        title (FormattedString): A string containing HTML formatted text
        type_ (ClassificationRefType0 | None): A reference to a classification value
        category (ClassificationRefType0 | None): A reference to a classification value
        publication_statuses (list[PublicationStatus]): Manage the research output's different statuses and dates these
            were reached.
        language (ClassificationRefType0 | None): A reference to a classification value
        contributors (list[AbstractContributorAssociation]): Contributors and their affiliations
        managing_organization (None | OrganizationRefType0): A reference to an organization in the institution
        type_discriminator (str):
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
        sub_title (FormattedString | Unset): A string containing HTML formatted text
        peer_review (bool | None | Unset): Indicates whether the research output is peer reviewed or not. Query the
            /research-outputs/allowed-peer-review-configurations endpoint for allowed values.
        international_peer_review (bool | None | Unset): Indicates whether the research output is internationally peer
            reviewed or not. Query the /research-outputs/allowed-peer-review-configurations endpoint for allowed values.
        translated_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support
            formatting. Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        translated_sub_title (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support
            formatting. Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        organizations (list[None | OrganizationRefType0] | None | Unset): A collection of organizational unit
            affiliations.
        external_organizations (list[ExternalOrganizationRefType0 | None] | None | Unset): A collection of external
            organization affiliations.
        total_number_of_contributors (int | None | Unset): The total number of authors from author collaborations.
        submission_year (int | None | Unset): The submission year of the research output.
        main_research_area (ClassificationRefType0 | None | Unset): A reference to a classification value
        electronic_versions (list[ElectronicVersionType0 | None] | None | Unset): Electronic versions of this research
            output.
        additional_files (list[AdditionalFileElectronicVersion] | None | Unset): Additional files related to this
            research output.
        links (list[Link] | None | Unset): Additional links associated with this research output.
        article_processing_charge (ArticleProcessingCharge | Unset): Holds information on the article processing charge
        keyword_groups (list[KeywordGroup] | None | Unset): Groups of keywords associated with the research output.
        bibliographical_note (LocalizedStringType0 | None | Unset): A set of string values, one for each submission
            locale. Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        descriptions (list[ClassifiedFormattedLocalizedValue] | None | Unset): A list of descriptions for this research
            output. Query the relevant /research-outputs/allowed-*-description-types endpoint for allowed types.
        visibility (Visibility | Unset): Visibility of an object
        workflow (Workflow | Unset): Information about workflow
        identifiers (list[Identifier] | None | Unset): Identifiers related to the research output.
        prizes (list[None | ResearchOutputPrizeAssociationType0] | None | Unset): Prizes related to the research output,
        press_medias (list[None | ResearchOutputPressMediaAssociationType0] | None | Unset): Press media related to the
            research output,
        data_sets (list[None | ResearchOutputDataSetAssociationType0] | None | Unset): Data sets related to the research
            output,
        student_thesis (list[None | ResearchOutputStudentThesisAssociationType0] | None | Unset): Student thesis related
            to the research output,
        impacts (list[None | ResearchOutputImpactAssociationType0] | None | Unset): Impacts related to the research
            output,
        activities (list[ActivityRefType0 | None] | None | Unset): Activities related to the research output,
        equipment (list[EquipmentRefType0 | None] | None | Unset): Equipment related to the research output.
        projects (list[None | ProjectAwardableAssociationType0] | None | Unset): Projects related to the research
            output.
        research_outputs (list[None | ResearchOutputAssociationType0] | None | Unset): Other related research outputs.
        custom_defined_fields (CustomDefinedFieldsType0 | None | Unset): Map of CustomDefinedField values, where the key
            is the field identifier Example: { "fieldName1": "typeDiscriminator": "Integer", "value" : 1}.
        images (list[ImageFile] | None | Unset): Image files with a maximum file size of 1MB
        funding_text (LocalizedStringType0 | None | Unset): A set of string values, one for each submission locale.
            Note: invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        funding_details (list[FundingDetails] | None | Unset): The funding details for the research output
        abstract (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        system_name (str | Unset): The content system name
        applicant (ExternalOrganizationRefType0 | None | Unset): A reference to an organization external to the
            institution
        project_number (None | str | Unset): The project number.
        journal_number (None | str | Unset): The journal number.
        date_finished (datetime.date | None | Unset): The date finished.
        number_of_pages (int | None | Unset): The number of pages in the research output.
        publication_series (list[PublicationSeries] | None | Unset): The publication series this research output is part
            of.
        book_series (list[BookSeriesJournalAssociation] | None | Unset): The book series this research output is part
            of.
    """

    title: FormattedString
    type_: ClassificationRefType0 | None
    category: ClassificationRefType0 | None
    publication_statuses: list[PublicationStatus]
    language: ClassificationRefType0 | None
    contributors: list[AbstractContributorAssociation]
    managing_organization: None | OrganizationRefType0
    type_discriminator: str
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
    sub_title: FormattedString | Unset = UNSET
    peer_review: bool | None | Unset = UNSET
    international_peer_review: bool | None | Unset = UNSET
    translated_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    translated_sub_title: FormattedLocalizedStringType0 | None | Unset = UNSET
    organizations: list[None | OrganizationRefType0] | None | Unset = UNSET
    external_organizations: list[ExternalOrganizationRefType0 | None] | None | Unset = (
        UNSET
    )
    total_number_of_contributors: int | None | Unset = UNSET
    submission_year: int | None | Unset = UNSET
    main_research_area: ClassificationRefType0 | None | Unset = UNSET
    electronic_versions: list[ElectronicVersionType0 | None] | None | Unset = UNSET
    additional_files: list[AdditionalFileElectronicVersion] | None | Unset = UNSET
    links: list[Link] | None | Unset = UNSET
    article_processing_charge: ArticleProcessingCharge | Unset = UNSET
    keyword_groups: list[KeywordGroup] | None | Unset = UNSET
    bibliographical_note: LocalizedStringType0 | None | Unset = UNSET
    descriptions: list[ClassifiedFormattedLocalizedValue] | None | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    workflow: Workflow | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    prizes: list[None | ResearchOutputPrizeAssociationType0] | None | Unset = UNSET
    press_medias: (
        list[None | ResearchOutputPressMediaAssociationType0] | None | Unset
    ) = UNSET
    data_sets: list[None | ResearchOutputDataSetAssociationType0] | None | Unset = UNSET
    student_thesis: (
        list[None | ResearchOutputStudentThesisAssociationType0] | None | Unset
    ) = UNSET
    impacts: list[None | ResearchOutputImpactAssociationType0] | None | Unset = UNSET
    activities: list[ActivityRefType0 | None] | None | Unset = UNSET
    equipment: list[EquipmentRefType0 | None] | None | Unset = UNSET
    projects: list[None | ProjectAwardableAssociationType0] | None | Unset = UNSET
    research_outputs: list[None | ResearchOutputAssociationType0] | None | Unset = UNSET
    custom_defined_fields: CustomDefinedFieldsType0 | None | Unset = UNSET
    images: list[ImageFile] | None | Unset = UNSET
    funding_text: LocalizedStringType0 | None | Unset = UNSET
    funding_details: list[FundingDetails] | None | Unset = UNSET
    abstract: FormattedLocalizedStringType0 | None | Unset = UNSET
    system_name: str | Unset = UNSET
    applicant: ExternalOrganizationRefType0 | None | Unset = UNSET
    project_number: None | str | Unset = UNSET
    journal_number: None | str | Unset = UNSET
    date_finished: datetime.date | None | Unset = UNSET
    number_of_pages: int | None | Unset = UNSET
    publication_series: list[PublicationSeries] | None | Unset = UNSET
    book_series: list[BookSeriesJournalAssociation] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.electronic_version_type_0 import ElectronicVersionType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.project_awardable_association_type_0 import (
            ProjectAwardableAssociationType0,
        )
        from ..models.research_output_association_type_0 import (
            ResearchOutputAssociationType0,
        )
        from ..models.research_output_data_set_association_type_0 import (
            ResearchOutputDataSetAssociationType0,
        )
        from ..models.research_output_impact_association_type_0 import (
            ResearchOutputImpactAssociationType0,
        )
        from ..models.research_output_press_media_association_type_0 import (
            ResearchOutputPressMediaAssociationType0,
        )
        from ..models.research_output_prize_association_type_0 import (
            ResearchOutputPrizeAssociationType0,
        )
        from ..models.research_output_student_thesis_association_type_0 import (
            ResearchOutputStudentThesisAssociationType0,
        )

        title = self.title.to_dict()

        type_: dict[str, Any] | None
        if isinstance(self.type_, ClassificationRefType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        category: dict[str, Any] | None
        if isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

        publication_statuses = []
        for publication_statuses_item_data in self.publication_statuses:
            publication_statuses_item = publication_statuses_item_data.to_dict()
            publication_statuses.append(publication_statuses_item)

        language: dict[str, Any] | None
        if isinstance(self.language, ClassificationRefType0):
            language = self.language.to_dict()
        else:
            language = self.language

        contributors = []
        for contributors_item_data in self.contributors:
            contributors_item = contributors_item_data.to_dict()
            contributors.append(contributors_item)

        managing_organization: dict[str, Any] | None
        if isinstance(self.managing_organization, OrganizationRefType0):
            managing_organization = self.managing_organization.to_dict()
        else:
            managing_organization = self.managing_organization

        type_discriminator = self.type_discriminator

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

        sub_title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_title, Unset):
            sub_title = self.sub_title.to_dict()

        peer_review: bool | None | Unset
        if isinstance(self.peer_review, Unset):
            peer_review = UNSET
        else:
            peer_review = self.peer_review

        international_peer_review: bool | None | Unset
        if isinstance(self.international_peer_review, Unset):
            international_peer_review = UNSET
        else:
            international_peer_review = self.international_peer_review

        translated_title: dict[str, Any] | None | Unset
        if isinstance(self.translated_title, Unset):
            translated_title = UNSET
        elif isinstance(self.translated_title, FormattedLocalizedStringType0):
            translated_title = self.translated_title.to_dict()
        else:
            translated_title = self.translated_title

        translated_sub_title: dict[str, Any] | None | Unset
        if isinstance(self.translated_sub_title, Unset):
            translated_sub_title = UNSET
        elif isinstance(self.translated_sub_title, FormattedLocalizedStringType0):
            translated_sub_title = self.translated_sub_title.to_dict()
        else:
            translated_sub_title = self.translated_sub_title

        organizations: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item: dict[str, Any] | None
                if isinstance(organizations_type_0_item_data, OrganizationRefType0):
                    organizations_type_0_item = organizations_type_0_item_data.to_dict()
                else:
                    organizations_type_0_item = organizations_type_0_item_data
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

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

        total_number_of_contributors: int | None | Unset
        if isinstance(self.total_number_of_contributors, Unset):
            total_number_of_contributors = UNSET
        else:
            total_number_of_contributors = self.total_number_of_contributors

        submission_year: int | None | Unset
        if isinstance(self.submission_year, Unset):
            submission_year = UNSET
        else:
            submission_year = self.submission_year

        main_research_area: dict[str, Any] | None | Unset
        if isinstance(self.main_research_area, Unset):
            main_research_area = UNSET
        elif isinstance(self.main_research_area, ClassificationRefType0):
            main_research_area = self.main_research_area.to_dict()
        else:
            main_research_area = self.main_research_area

        electronic_versions: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.electronic_versions, Unset):
            electronic_versions = UNSET
        elif isinstance(self.electronic_versions, list):
            electronic_versions = []
            for electronic_versions_type_0_item_data in self.electronic_versions:
                electronic_versions_type_0_item: dict[str, Any] | None
                if isinstance(
                    electronic_versions_type_0_item_data, ElectronicVersionType0
                ):
                    electronic_versions_type_0_item = (
                        electronic_versions_type_0_item_data.to_dict()
                    )
                else:
                    electronic_versions_type_0_item = (
                        electronic_versions_type_0_item_data
                    )
                electronic_versions.append(electronic_versions_type_0_item)

        else:
            electronic_versions = self.electronic_versions

        additional_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.additional_files, Unset):
            additional_files = UNSET
        elif isinstance(self.additional_files, list):
            additional_files = []
            for additional_files_type_0_item_data in self.additional_files:
                additional_files_type_0_item = (
                    additional_files_type_0_item_data.to_dict()
                )
                additional_files.append(additional_files_type_0_item)

        else:
            additional_files = self.additional_files

        links: list[dict[str, Any]] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        else:
            links = self.links

        article_processing_charge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.article_processing_charge, Unset):
            article_processing_charge = self.article_processing_charge.to_dict()

        keyword_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyword_groups, Unset):
            keyword_groups = UNSET
        elif isinstance(self.keyword_groups, list):
            keyword_groups = []
            for keyword_groups_type_0_item_data in self.keyword_groups:
                keyword_groups_type_0_item = keyword_groups_type_0_item_data.to_dict()
                keyword_groups.append(keyword_groups_type_0_item)

        else:
            keyword_groups = self.keyword_groups

        bibliographical_note: dict[str, Any] | None | Unset
        if isinstance(self.bibliographical_note, Unset):
            bibliographical_note = UNSET
        elif isinstance(self.bibliographical_note, LocalizedStringType0):
            bibliographical_note = self.bibliographical_note.to_dict()
        else:
            bibliographical_note = self.bibliographical_note

        descriptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.descriptions, Unset):
            descriptions = UNSET
        elif isinstance(self.descriptions, list):
            descriptions = []
            for descriptions_type_0_item_data in self.descriptions:
                descriptions_type_0_item = descriptions_type_0_item_data.to_dict()
                descriptions.append(descriptions_type_0_item)

        else:
            descriptions = self.descriptions

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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

        prizes: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.prizes, Unset):
            prizes = UNSET
        elif isinstance(self.prizes, list):
            prizes = []
            for prizes_type_0_item_data in self.prizes:
                prizes_type_0_item: dict[str, Any] | None
                if isinstance(
                    prizes_type_0_item_data, ResearchOutputPrizeAssociationType0
                ):
                    prizes_type_0_item = prizes_type_0_item_data.to_dict()
                else:
                    prizes_type_0_item = prizes_type_0_item_data
                prizes.append(prizes_type_0_item)

        else:
            prizes = self.prizes

        press_medias: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.press_medias, Unset):
            press_medias = UNSET
        elif isinstance(self.press_medias, list):
            press_medias = []
            for press_medias_type_0_item_data in self.press_medias:
                press_medias_type_0_item: dict[str, Any] | None
                if isinstance(
                    press_medias_type_0_item_data,
                    ResearchOutputPressMediaAssociationType0,
                ):
                    press_medias_type_0_item = press_medias_type_0_item_data.to_dict()
                else:
                    press_medias_type_0_item = press_medias_type_0_item_data
                press_medias.append(press_medias_type_0_item)

        else:
            press_medias = self.press_medias

        data_sets: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.data_sets, Unset):
            data_sets = UNSET
        elif isinstance(self.data_sets, list):
            data_sets = []
            for data_sets_type_0_item_data in self.data_sets:
                data_sets_type_0_item: dict[str, Any] | None
                if isinstance(
                    data_sets_type_0_item_data, ResearchOutputDataSetAssociationType0
                ):
                    data_sets_type_0_item = data_sets_type_0_item_data.to_dict()
                else:
                    data_sets_type_0_item = data_sets_type_0_item_data
                data_sets.append(data_sets_type_0_item)

        else:
            data_sets = self.data_sets

        student_thesis: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.student_thesis, Unset):
            student_thesis = UNSET
        elif isinstance(self.student_thesis, list):
            student_thesis = []
            for student_thesis_type_0_item_data in self.student_thesis:
                student_thesis_type_0_item: dict[str, Any] | None
                if isinstance(
                    student_thesis_type_0_item_data,
                    ResearchOutputStudentThesisAssociationType0,
                ):
                    student_thesis_type_0_item = (
                        student_thesis_type_0_item_data.to_dict()
                    )
                else:
                    student_thesis_type_0_item = student_thesis_type_0_item_data
                student_thesis.append(student_thesis_type_0_item)

        else:
            student_thesis = self.student_thesis

        impacts: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.impacts, Unset):
            impacts = UNSET
        elif isinstance(self.impacts, list):
            impacts = []
            for impacts_type_0_item_data in self.impacts:
                impacts_type_0_item: dict[str, Any] | None
                if isinstance(
                    impacts_type_0_item_data, ResearchOutputImpactAssociationType0
                ):
                    impacts_type_0_item = impacts_type_0_item_data.to_dict()
                else:
                    impacts_type_0_item = impacts_type_0_item_data
                impacts.append(impacts_type_0_item)

        else:
            impacts = self.impacts

        activities: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.activities, Unset):
            activities = UNSET
        elif isinstance(self.activities, list):
            activities = []
            for activities_type_0_item_data in self.activities:
                activities_type_0_item: dict[str, Any] | None
                if isinstance(activities_type_0_item_data, ActivityRefType0):
                    activities_type_0_item = activities_type_0_item_data.to_dict()
                else:
                    activities_type_0_item = activities_type_0_item_data
                activities.append(activities_type_0_item)

        else:
            activities = self.activities

        equipment: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.equipment, Unset):
            equipment = UNSET
        elif isinstance(self.equipment, list):
            equipment = []
            for equipment_type_0_item_data in self.equipment:
                equipment_type_0_item: dict[str, Any] | None
                if isinstance(equipment_type_0_item_data, EquipmentRefType0):
                    equipment_type_0_item = equipment_type_0_item_data.to_dict()
                else:
                    equipment_type_0_item = equipment_type_0_item_data
                equipment.append(equipment_type_0_item)

        else:
            equipment = self.equipment

        projects: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item: dict[str, Any] | None
                if isinstance(
                    projects_type_0_item_data, ProjectAwardableAssociationType0
                ):
                    projects_type_0_item = projects_type_0_item_data.to_dict()
                else:
                    projects_type_0_item = projects_type_0_item_data
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        research_outputs: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.research_outputs, Unset):
            research_outputs = UNSET
        elif isinstance(self.research_outputs, list):
            research_outputs = []
            for research_outputs_type_0_item_data in self.research_outputs:
                research_outputs_type_0_item: dict[str, Any] | None
                if isinstance(
                    research_outputs_type_0_item_data, ResearchOutputAssociationType0
                ):
                    research_outputs_type_0_item = (
                        research_outputs_type_0_item_data.to_dict()
                    )
                else:
                    research_outputs_type_0_item = research_outputs_type_0_item_data
                research_outputs.append(research_outputs_type_0_item)

        else:
            research_outputs = self.research_outputs

        custom_defined_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_defined_fields, Unset):
            custom_defined_fields = UNSET
        elif isinstance(self.custom_defined_fields, CustomDefinedFieldsType0):
            custom_defined_fields = self.custom_defined_fields.to_dict()
        else:
            custom_defined_fields = self.custom_defined_fields

        images: list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        funding_text: dict[str, Any] | None | Unset
        if isinstance(self.funding_text, Unset):
            funding_text = UNSET
        elif isinstance(self.funding_text, LocalizedStringType0):
            funding_text = self.funding_text.to_dict()
        else:
            funding_text = self.funding_text

        funding_details: list[dict[str, Any]] | None | Unset
        if isinstance(self.funding_details, Unset):
            funding_details = UNSET
        elif isinstance(self.funding_details, list):
            funding_details = []
            for funding_details_type_0_item_data in self.funding_details:
                funding_details_type_0_item = funding_details_type_0_item_data.to_dict()
                funding_details.append(funding_details_type_0_item)

        else:
            funding_details = self.funding_details

        abstract: dict[str, Any] | None | Unset
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        elif isinstance(self.abstract, FormattedLocalizedStringType0):
            abstract = self.abstract.to_dict()
        else:
            abstract = self.abstract

        system_name = self.system_name

        applicant: dict[str, Any] | None | Unset
        if isinstance(self.applicant, Unset):
            applicant = UNSET
        elif isinstance(self.applicant, ExternalOrganizationRefType0):
            applicant = self.applicant.to_dict()
        else:
            applicant = self.applicant

        project_number: None | str | Unset
        if isinstance(self.project_number, Unset):
            project_number = UNSET
        else:
            project_number = self.project_number

        journal_number: None | str | Unset
        if isinstance(self.journal_number, Unset):
            journal_number = UNSET
        else:
            journal_number = self.journal_number

        date_finished: None | str | Unset
        if isinstance(self.date_finished, Unset):
            date_finished = UNSET
        elif isinstance(self.date_finished, datetime.date):
            date_finished = self.date_finished.isoformat()
        else:
            date_finished = self.date_finished

        number_of_pages: int | None | Unset
        if isinstance(self.number_of_pages, Unset):
            number_of_pages = UNSET
        else:
            number_of_pages = self.number_of_pages

        publication_series: list[dict[str, Any]] | None | Unset
        if isinstance(self.publication_series, Unset):
            publication_series = UNSET
        elif isinstance(self.publication_series, list):
            publication_series = []
            for publication_series_type_0_item_data in self.publication_series:
                publication_series_type_0_item = (
                    publication_series_type_0_item_data.to_dict()
                )
                publication_series.append(publication_series_type_0_item)

        else:
            publication_series = self.publication_series

        book_series: list[dict[str, Any]] | None | Unset
        if isinstance(self.book_series, Unset):
            book_series = UNSET
        elif isinstance(self.book_series, list):
            book_series = []
            for book_series_type_0_item_data in self.book_series:
                book_series_type_0_item = book_series_type_0_item_data.to_dict()
                book_series.append(book_series_type_0_item)

        else:
            book_series = self.book_series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "type": type_,
                "category": category,
                "publicationStatuses": publication_statuses,
                "language": language,
                "contributors": contributors,
                "managingOrganization": managing_organization,
                "typeDiscriminator": type_discriminator,
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
        if sub_title is not UNSET:
            field_dict["subTitle"] = sub_title
        if peer_review is not UNSET:
            field_dict["peerReview"] = peer_review
        if international_peer_review is not UNSET:
            field_dict["internationalPeerReview"] = international_peer_review
        if translated_title is not UNSET:
            field_dict["translatedTitle"] = translated_title
        if translated_sub_title is not UNSET:
            field_dict["translatedSubTitle"] = translated_sub_title
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if external_organizations is not UNSET:
            field_dict["externalOrganizations"] = external_organizations
        if total_number_of_contributors is not UNSET:
            field_dict["totalNumberOfContributors"] = total_number_of_contributors
        if submission_year is not UNSET:
            field_dict["submissionYear"] = submission_year
        if main_research_area is not UNSET:
            field_dict["mainResearchArea"] = main_research_area
        if electronic_versions is not UNSET:
            field_dict["electronicVersions"] = electronic_versions
        if additional_files is not UNSET:
            field_dict["additionalFiles"] = additional_files
        if links is not UNSET:
            field_dict["links"] = links
        if article_processing_charge is not UNSET:
            field_dict["articleProcessingCharge"] = article_processing_charge
        if keyword_groups is not UNSET:
            field_dict["keywordGroups"] = keyword_groups
        if bibliographical_note is not UNSET:
            field_dict["bibliographicalNote"] = bibliographical_note
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if press_medias is not UNSET:
            field_dict["pressMedias"] = press_medias
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if student_thesis is not UNSET:
            field_dict["studentThesis"] = student_thesis
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if activities is not UNSET:
            field_dict["activities"] = activities
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if projects is not UNSET:
            field_dict["projects"] = projects
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if custom_defined_fields is not UNSET:
            field_dict["customDefinedFields"] = custom_defined_fields
        if images is not UNSET:
            field_dict["images"] = images
        if funding_text is not UNSET:
            field_dict["fundingText"] = funding_text
        if funding_details is not UNSET:
            field_dict["fundingDetails"] = funding_details
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if applicant is not UNSET:
            field_dict["applicant"] = applicant
        if project_number is not UNSET:
            field_dict["projectNumber"] = project_number
        if journal_number is not UNSET:
            field_dict["journalNumber"] = journal_number
        if date_finished is not UNSET:
            field_dict["dateFinished"] = date_finished
        if number_of_pages is not UNSET:
            field_dict["numberOfPages"] = number_of_pages
        if publication_series is not UNSET:
            field_dict["publicationSeries"] = publication_series
        if book_series is not UNSET:
            field_dict["bookSeries"] = book_series

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abstract_contributor_association import (
            AbstractContributorAssociation,
        )
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.additional_file_electronic_version import (
            AdditionalFileElectronicVersion,
        )
        from ..models.article_processing_charge import ArticleProcessingCharge
        from ..models.book_series_journal_association import (
            BookSeriesJournalAssociation,
        )
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.classified_formatted_localized_value import (
            ClassifiedFormattedLocalizedValue,
        )
        from ..models.custom_defined_fields_type_0 import CustomDefinedFieldsType0
        from ..models.electronic_version_type_0 import ElectronicVersionType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.external_organization_ref_type_0 import (
            ExternalOrganizationRefType0,
        )
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.formatted_string import FormattedString
        from ..models.funding_details import FundingDetails
        from ..models.identifier import Identifier
        from ..models.image_file import ImageFile
        from ..models.keyword_group import KeywordGroup
        from ..models.link import Link
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.organization_ref_type_0 import OrganizationRefType0
        from ..models.project_awardable_association_type_0 import (
            ProjectAwardableAssociationType0,
        )
        from ..models.publication_series import PublicationSeries
        from ..models.publication_status import PublicationStatus
        from ..models.research_output_association_type_0 import (
            ResearchOutputAssociationType0,
        )
        from ..models.research_output_data_set_association_type_0 import (
            ResearchOutputDataSetAssociationType0,
        )
        from ..models.research_output_impact_association_type_0 import (
            ResearchOutputImpactAssociationType0,
        )
        from ..models.research_output_press_media_association_type_0 import (
            ResearchOutputPressMediaAssociationType0,
        )
        from ..models.research_output_prize_association_type_0 import (
            ResearchOutputPrizeAssociationType0,
        )
        from ..models.research_output_student_thesis_association_type_0 import (
            ResearchOutputStudentThesisAssociationType0,
        )
        from ..models.visibility import Visibility
        from ..models.workflow import Workflow

        d = dict(src_dict)
        title = FormattedString.from_dict(d.pop("title"))

        def _parse_type_(data: object) -> ClassificationRefType0 | None:
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

        type_ = _parse_type_(d.pop("type"))

        def _parse_category(data: object) -> ClassificationRefType0 | None:
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

        category = _parse_category(d.pop("category"))

        publication_statuses = []
        _publication_statuses = d.pop("publicationStatuses")
        for publication_statuses_item_data in _publication_statuses:
            publication_statuses_item = PublicationStatus.from_dict(
                publication_statuses_item_data
            )

            publication_statuses.append(publication_statuses_item)

        def _parse_language(data: object) -> ClassificationRefType0 | None:
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

        language = _parse_language(d.pop("language"))

        contributors = []
        _contributors = d.pop("contributors")
        for contributors_item_data in _contributors:
            contributors_item = AbstractContributorAssociation.from_dict(
                contributors_item_data
            )

            contributors.append(contributors_item)

        def _parse_managing_organization(data: object) -> None | OrganizationRefType0:
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

        managing_organization = _parse_managing_organization(
            d.pop("managingOrganization")
        )

        type_discriminator = d.pop("typeDiscriminator")

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

        _sub_title = d.pop("subTitle", UNSET)
        sub_title: FormattedString | Unset
        if isinstance(_sub_title, Unset):
            sub_title = UNSET
        else:
            sub_title = FormattedString.from_dict(_sub_title)

        def _parse_peer_review(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        peer_review = _parse_peer_review(d.pop("peerReview", UNSET))

        def _parse_international_peer_review(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        international_peer_review = _parse_international_peer_review(
            d.pop("internationalPeerReview", UNSET)
        )

        def _parse_translated_title(
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

        translated_title = _parse_translated_title(d.pop("translatedTitle", UNSET))

        def _parse_translated_sub_title(
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

        translated_sub_title = _parse_translated_sub_title(
            d.pop("translatedSubTitle", UNSET)
        )

        def _parse_organizations(
            data: object,
        ) -> list[None | OrganizationRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:

                    def _parse_organizations_type_0_item(
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

                    organizations_type_0_item = _parse_organizations_type_0_item(
                        organizations_type_0_item_data
                    )

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | OrganizationRefType0] | None | Unset, data)

        organizations = _parse_organizations(d.pop("organizations", UNSET))

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

        def _parse_total_number_of_contributors(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_number_of_contributors = _parse_total_number_of_contributors(
            d.pop("totalNumberOfContributors", UNSET)
        )

        def _parse_submission_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        submission_year = _parse_submission_year(d.pop("submissionYear", UNSET))

        def _parse_main_research_area(
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

        main_research_area = _parse_main_research_area(d.pop("mainResearchArea", UNSET))

        def _parse_electronic_versions(
            data: object,
        ) -> list[ElectronicVersionType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                electronic_versions_type_0 = []
                _electronic_versions_type_0 = data
                for electronic_versions_type_0_item_data in _electronic_versions_type_0:

                    def _parse_electronic_versions_type_0_item(
                        data: object,
                    ) -> ElectronicVersionType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_electronic_version_type_0 = (
                                ElectronicVersionType0.from_dict(data)
                            )

                            return componentsschemas_electronic_version_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ElectronicVersionType0 | None, data)

                    electronic_versions_type_0_item = (
                        _parse_electronic_versions_type_0_item(
                            electronic_versions_type_0_item_data
                        )
                    )

                    electronic_versions_type_0.append(electronic_versions_type_0_item)

                return electronic_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ElectronicVersionType0 | None] | None | Unset, data)

        electronic_versions = _parse_electronic_versions(
            d.pop("electronicVersions", UNSET)
        )

        def _parse_additional_files(
            data: object,
        ) -> list[AdditionalFileElectronicVersion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_files_type_0 = []
                _additional_files_type_0 = data
                for additional_files_type_0_item_data in _additional_files_type_0:
                    additional_files_type_0_item = (
                        AdditionalFileElectronicVersion.from_dict(
                            additional_files_type_0_item_data
                        )
                    )

                    additional_files_type_0.append(additional_files_type_0_item)

                return additional_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AdditionalFileElectronicVersion] | None | Unset, data)

        additional_files = _parse_additional_files(d.pop("additionalFiles", UNSET))

        def _parse_links(data: object) -> list[Link] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = Link.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Link] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))

        _article_processing_charge = d.pop("articleProcessingCharge", UNSET)
        article_processing_charge: ArticleProcessingCharge | Unset
        if isinstance(_article_processing_charge, Unset):
            article_processing_charge = UNSET
        else:
            article_processing_charge = ArticleProcessingCharge.from_dict(
                _article_processing_charge
            )

        def _parse_keyword_groups(data: object) -> list[KeywordGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyword_groups_type_0 = []
                _keyword_groups_type_0 = data
                for keyword_groups_type_0_item_data in _keyword_groups_type_0:
                    keyword_groups_type_0_item = KeywordGroup.from_dict(
                        keyword_groups_type_0_item_data
                    )

                    keyword_groups_type_0.append(keyword_groups_type_0_item)

                return keyword_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeywordGroup] | None | Unset, data)

        keyword_groups = _parse_keyword_groups(d.pop("keywordGroups", UNSET))

        def _parse_bibliographical_note(
            data: object,
        ) -> LocalizedStringType0 | None | Unset:
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

        bibliographical_note = _parse_bibliographical_note(
            d.pop("bibliographicalNote", UNSET)
        )

        def _parse_descriptions(
            data: object,
        ) -> list[ClassifiedFormattedLocalizedValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                descriptions_type_0 = []
                _descriptions_type_0 = data
                for descriptions_type_0_item_data in _descriptions_type_0:
                    descriptions_type_0_item = (
                        ClassifiedFormattedLocalizedValue.from_dict(
                            descriptions_type_0_item_data
                        )
                    )

                    descriptions_type_0.append(descriptions_type_0_item)

                return descriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClassifiedFormattedLocalizedValue] | None | Unset, data)

        descriptions = _parse_descriptions(d.pop("descriptions", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

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

        def _parse_prizes(
            data: object,
        ) -> list[None | ResearchOutputPrizeAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prizes_type_0 = []
                _prizes_type_0 = data
                for prizes_type_0_item_data in _prizes_type_0:

                    def _parse_prizes_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputPrizeAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_prize_association_type_0 = ResearchOutputPrizeAssociationType0.from_dict(
                                data
                            )

                            return componentsschemas_research_output_prize_association_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ResearchOutputPrizeAssociationType0, data)

                    prizes_type_0_item = _parse_prizes_type_0_item(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ResearchOutputPrizeAssociationType0] | None | Unset, data
            )

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_press_medias(
            data: object,
        ) -> list[None | ResearchOutputPressMediaAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                press_medias_type_0 = []
                _press_medias_type_0 = data
                for press_medias_type_0_item_data in _press_medias_type_0:

                    def _parse_press_medias_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputPressMediaAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_press_media_association_type_0 = ResearchOutputPressMediaAssociationType0.from_dict(
                                data
                            )

                            return componentsschemas_research_output_press_media_association_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | ResearchOutputPressMediaAssociationType0, data
                        )

                    press_medias_type_0_item = _parse_press_medias_type_0_item(
                        press_medias_type_0_item_data
                    )

                    press_medias_type_0.append(press_medias_type_0_item)

                return press_medias_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ResearchOutputPressMediaAssociationType0] | None | Unset,
                data,
            )

        press_medias = _parse_press_medias(d.pop("pressMedias", UNSET))

        def _parse_data_sets(
            data: object,
        ) -> list[None | ResearchOutputDataSetAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_sets_type_0 = []
                _data_sets_type_0 = data
                for data_sets_type_0_item_data in _data_sets_type_0:

                    def _parse_data_sets_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputDataSetAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_data_set_association_type_0 = ResearchOutputDataSetAssociationType0.from_dict(
                                data
                            )

                            return componentsschemas_research_output_data_set_association_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ResearchOutputDataSetAssociationType0, data)

                    data_sets_type_0_item = _parse_data_sets_type_0_item(
                        data_sets_type_0_item_data
                    )

                    data_sets_type_0.append(data_sets_type_0_item)

                return data_sets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ResearchOutputDataSetAssociationType0] | None | Unset, data
            )

        data_sets = _parse_data_sets(d.pop("dataSets", UNSET))

        def _parse_student_thesis(
            data: object,
        ) -> list[None | ResearchOutputStudentThesisAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                student_thesis_type_0 = []
                _student_thesis_type_0 = data
                for student_thesis_type_0_item_data in _student_thesis_type_0:

                    def _parse_student_thesis_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputStudentThesisAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_student_thesis_association_type_0 = ResearchOutputStudentThesisAssociationType0.from_dict(
                                data
                            )

                            return componentsschemas_research_output_student_thesis_association_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            None | ResearchOutputStudentThesisAssociationType0, data
                        )

                    student_thesis_type_0_item = _parse_student_thesis_type_0_item(
                        student_thesis_type_0_item_data
                    )

                    student_thesis_type_0.append(student_thesis_type_0_item)

                return student_thesis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ResearchOutputStudentThesisAssociationType0] | None | Unset,
                data,
            )

        student_thesis = _parse_student_thesis(d.pop("studentThesis", UNSET))

        def _parse_impacts(
            data: object,
        ) -> list[None | ResearchOutputImpactAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                impacts_type_0 = []
                _impacts_type_0 = data
                for impacts_type_0_item_data in _impacts_type_0:

                    def _parse_impacts_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputImpactAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_impact_association_type_0 = ResearchOutputImpactAssociationType0.from_dict(
                                data
                            )

                            return componentsschemas_research_output_impact_association_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ResearchOutputImpactAssociationType0, data)

                    impacts_type_0_item = _parse_impacts_type_0_item(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ResearchOutputImpactAssociationType0] | None | Unset, data
            )

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_activities(
            data: object,
        ) -> list[ActivityRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                activities_type_0 = []
                _activities_type_0 = data
                for activities_type_0_item_data in _activities_type_0:

                    def _parse_activities_type_0_item(
                        data: object,
                    ) -> ActivityRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_activity_ref_type_0 = (
                                ActivityRefType0.from_dict(data)
                            )

                            return componentsschemas_activity_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ActivityRefType0 | None, data)

                    activities_type_0_item = _parse_activities_type_0_item(
                        activities_type_0_item_data
                    )

                    activities_type_0.append(activities_type_0_item)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityRefType0 | None] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_equipment(
            data: object,
        ) -> list[EquipmentRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                equipment_type_0 = []
                _equipment_type_0 = data
                for equipment_type_0_item_data in _equipment_type_0:

                    def _parse_equipment_type_0_item(
                        data: object,
                    ) -> EquipmentRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_equipment_ref_type_0 = (
                                EquipmentRefType0.from_dict(data)
                            )

                            return componentsschemas_equipment_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(EquipmentRefType0 | None, data)

                    equipment_type_0_item = _parse_equipment_type_0_item(
                        equipment_type_0_item_data
                    )

                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquipmentRefType0 | None] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[None | ProjectAwardableAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in _projects_type_0:

                    def _parse_projects_type_0_item(
                        data: object,
                    ) -> None | ProjectAwardableAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_project_awardable_association_type_0 = (
                                ProjectAwardableAssociationType0.from_dict(data)
                            )

                            return (
                                componentsschemas_project_awardable_association_type_0
                            )
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ProjectAwardableAssociationType0, data)

                    projects_type_0_item = _parse_projects_type_0_item(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ProjectAwardableAssociationType0] | None | Unset, data
            )

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[None | ResearchOutputAssociationType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                research_outputs_type_0 = []
                _research_outputs_type_0 = data
                for research_outputs_type_0_item_data in _research_outputs_type_0:

                    def _parse_research_outputs_type_0_item(
                        data: object,
                    ) -> None | ResearchOutputAssociationType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_association_type_0 = (
                                ResearchOutputAssociationType0.from_dict(data)
                            )

                            return componentsschemas_research_output_association_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ResearchOutputAssociationType0, data)

                    research_outputs_type_0_item = _parse_research_outputs_type_0_item(
                        research_outputs_type_0_item_data
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[None | ResearchOutputAssociationType0] | None | Unset, data
            )

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

        def _parse_custom_defined_fields(
            data: object,
        ) -> CustomDefinedFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_custom_defined_fields_type_0 = (
                    CustomDefinedFieldsType0.from_dict(data)
                )

                return componentsschemas_custom_defined_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDefinedFieldsType0 | None | Unset, data)

        custom_defined_fields = _parse_custom_defined_fields(
            d.pop("customDefinedFields", UNSET)
        )

        def _parse_images(data: object) -> list[ImageFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = ImageFile.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageFile] | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_funding_text(data: object) -> LocalizedStringType0 | None | Unset:
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

        funding_text = _parse_funding_text(d.pop("fundingText", UNSET))

        def _parse_funding_details(data: object) -> list[FundingDetails] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_details_type_0 = []
                _funding_details_type_0 = data
                for funding_details_type_0_item_data in _funding_details_type_0:
                    funding_details_type_0_item = FundingDetails.from_dict(
                        funding_details_type_0_item_data
                    )

                    funding_details_type_0.append(funding_details_type_0_item)

                return funding_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FundingDetails] | None | Unset, data)

        funding_details = _parse_funding_details(d.pop("fundingDetails", UNSET))

        def _parse_abstract(
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

        abstract = _parse_abstract(d.pop("abstract", UNSET))

        system_name = d.pop("systemName", UNSET)

        def _parse_applicant(
            data: object,
        ) -> ExternalOrganizationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(ExternalOrganizationRefType0 | None | Unset, data)

        applicant = _parse_applicant(d.pop("applicant", UNSET))

        def _parse_project_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_number = _parse_project_number(d.pop("projectNumber", UNSET))

        def _parse_journal_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        journal_number = _parse_journal_number(d.pop("journalNumber", UNSET))

        def _parse_date_finished(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_finished_type_0 = isoparse(data).date()

                return date_finished_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_finished = _parse_date_finished(d.pop("dateFinished", UNSET))

        def _parse_number_of_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_pages = _parse_number_of_pages(d.pop("numberOfPages", UNSET))

        def _parse_publication_series(
            data: object,
        ) -> list[PublicationSeries] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                publication_series_type_0 = []
                _publication_series_type_0 = data
                for publication_series_type_0_item_data in _publication_series_type_0:
                    publication_series_type_0_item = PublicationSeries.from_dict(
                        publication_series_type_0_item_data
                    )

                    publication_series_type_0.append(publication_series_type_0_item)

                return publication_series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PublicationSeries] | None | Unset, data)

        publication_series = _parse_publication_series(
            d.pop("publicationSeries", UNSET)
        )

        def _parse_book_series(
            data: object,
        ) -> list[BookSeriesJournalAssociation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                book_series_type_0 = []
                _book_series_type_0 = data
                for book_series_type_0_item_data in _book_series_type_0:
                    book_series_type_0_item = BookSeriesJournalAssociation.from_dict(
                        book_series_type_0_item_data
                    )

                    book_series_type_0.append(book_series_type_0_item)

                return book_series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookSeriesJournalAssociation] | None | Unset, data)

        book_series = _parse_book_series(d.pop("bookSeries", UNSET))

        memorandum = cls(
            title=title,
            type_=type_,
            category=category,
            publication_statuses=publication_statuses,
            language=language,
            contributors=contributors,
            managing_organization=managing_organization,
            type_discriminator=type_discriminator,
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
            sub_title=sub_title,
            peer_review=peer_review,
            international_peer_review=international_peer_review,
            translated_title=translated_title,
            translated_sub_title=translated_sub_title,
            organizations=organizations,
            external_organizations=external_organizations,
            total_number_of_contributors=total_number_of_contributors,
            submission_year=submission_year,
            main_research_area=main_research_area,
            electronic_versions=electronic_versions,
            additional_files=additional_files,
            links=links,
            article_processing_charge=article_processing_charge,
            keyword_groups=keyword_groups,
            bibliographical_note=bibliographical_note,
            descriptions=descriptions,
            visibility=visibility,
            workflow=workflow,
            identifiers=identifiers,
            prizes=prizes,
            press_medias=press_medias,
            data_sets=data_sets,
            student_thesis=student_thesis,
            impacts=impacts,
            activities=activities,
            equipment=equipment,
            projects=projects,
            research_outputs=research_outputs,
            custom_defined_fields=custom_defined_fields,
            images=images,
            funding_text=funding_text,
            funding_details=funding_details,
            abstract=abstract,
            system_name=system_name,
            applicant=applicant,
            project_number=project_number,
            journal_number=journal_number,
            date_finished=date_finished,
            number_of_pages=number_of_pages,
            publication_series=publication_series,
            book_series=book_series,
        )

        memorandum.additional_properties = d
        return memorandum

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
