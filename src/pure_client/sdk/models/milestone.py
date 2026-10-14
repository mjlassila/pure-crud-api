from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.milestone_milestone_type import MilestoneMilestoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_ref_type_0 import ApplicationRefType0
    from ..models.award_ref_type_0 import AwardRefType0
    from ..models.classification_ref_type_0 import ClassificationRefType0
    from ..models.contract_ref_type_0 import ContractRefType0
    from ..models.ethical_review_ref_type_0 import EthicalReviewRefType0
    from ..models.formatted_localized_string_type_0 import FormattedLocalizedStringType0
    from ..models.identifier import Identifier
    from ..models.localized_string_type_0 import LocalizedStringType0
    from ..models.milestone_document import MilestoneDocument
    from ..models.milestone_reminder import MilestoneReminder
    from ..models.project_ref_type_0 import ProjectRefType0
    from ..models.user_ref_type_0 import UserRefType0


T = TypeVar("T", bound="Milestone")


@_attrs_define
class Milestone:
    """A milestone.

    Attributes:
        title (LocalizedStringType0 | None): A set of string values, one for each submission locale. Note: invalid
            locale values will be ignored. Example: {'en_GB': 'Some text'}.
        milestone_type (MilestoneMilestoneType): Selected milestone type. Based on the value used for 'milestoneType',
            it is mandatory to fill either 'academicRole' or 'administrativeRole' property as well.
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
        deadline (datetime.date | None | Unset): The deadline date of the milestone.
        completion_state (ClassificationRefType0 | None | Unset): A reference to a classification value
        completed_date (datetime.date | None | Unset): The date when the milestone was completed. This can only be set
            when 'completionState' property value is 'completed'
        award (AwardRefType0 | None | Unset): A reference to an award
        application (ApplicationRefType0 | None | Unset): A reference to an application
        project (None | ProjectRefType0 | Unset): A reference to project
        ethical_review (EthicalReviewRefType0 | None | Unset): A reference to an ethical review
        contract (ContractRefType0 | None | Unset): A reference to a contract
        completed_by (None | Unset | UserRefType0): A reference to an user
        milestone_state (ClassificationRefType0 | None | Unset): A reference to a classification value
        reminders (list[MilestoneReminder] | Unset): List of reminders
        administrative_role (None | str | Unset): The user role for the milestone for administrative milestones
        academic_role (ClassificationRefType0 | None | Unset): A reference to a classification value
        description (FormattedLocalizedStringType0 | None | Unset): A set of localized strings that support formatting.
            Invalid locale values will be ignored. Example: {'en_GB': 'Some text'}.
        category (ClassificationRefType0 | None | Unset): A reference to a classification value
        documents (list[MilestoneDocument] | None | Unset): A collection of documents related to the milestone.
        responsible_users (list[None | UserRefType0] | Unset): The specific users chosen to be responsible for the
            content.
            When milestone type is 'Academic', responsible user can be one of the associated academic, that have a role on
            the content, that matches the responsible role.
            When the type is 'Administrative', responsible user must have an administrator role, that matches the selected
            role.
            When the milestone role is an editor role, the selected user must have an editorial role that matches the owner
            or related organizations of the milestone.
        identifiers (list[Identifier] | None | Unset): Identifiers related to the milestone.
        system_name (str | Unset): The content system name
    """

    title: LocalizedStringType0 | None
    milestone_type: MilestoneMilestoneType
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
    deadline: datetime.date | None | Unset = UNSET
    completion_state: ClassificationRefType0 | None | Unset = UNSET
    completed_date: datetime.date | None | Unset = UNSET
    award: AwardRefType0 | None | Unset = UNSET
    application: ApplicationRefType0 | None | Unset = UNSET
    project: None | ProjectRefType0 | Unset = UNSET
    ethical_review: EthicalReviewRefType0 | None | Unset = UNSET
    contract: ContractRefType0 | None | Unset = UNSET
    completed_by: None | Unset | UserRefType0 = UNSET
    milestone_state: ClassificationRefType0 | None | Unset = UNSET
    reminders: list[MilestoneReminder] | Unset = UNSET
    administrative_role: None | str | Unset = UNSET
    academic_role: ClassificationRefType0 | None | Unset = UNSET
    description: FormattedLocalizedStringType0 | None | Unset = UNSET
    category: ClassificationRefType0 | None | Unset = UNSET
    documents: list[MilestoneDocument] | None | Unset = UNSET
    responsible_users: list[None | UserRefType0] | Unset = UNSET
    identifiers: list[Identifier] | None | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.contract_ref_type_0 import ContractRefType0
        from ..models.ethical_review_ref_type_0 import EthicalReviewRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.project_ref_type_0 import ProjectRefType0
        from ..models.user_ref_type_0 import UserRefType0

        title: dict[str, Any] | None
        if isinstance(self.title, LocalizedStringType0):
            title = self.title.to_dict()
        else:
            title = self.title

        milestone_type = self.milestone_type.value

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

        deadline: None | str | Unset
        if isinstance(self.deadline, Unset):
            deadline = UNSET
        elif isinstance(self.deadline, datetime.date):
            deadline = self.deadline.isoformat()
        else:
            deadline = self.deadline

        completion_state: dict[str, Any] | None | Unset
        if isinstance(self.completion_state, Unset):
            completion_state = UNSET
        elif isinstance(self.completion_state, ClassificationRefType0):
            completion_state = self.completion_state.to_dict()
        else:
            completion_state = self.completion_state

        completed_date: None | str | Unset
        if isinstance(self.completed_date, Unset):
            completed_date = UNSET
        elif isinstance(self.completed_date, datetime.date):
            completed_date = self.completed_date.isoformat()
        else:
            completed_date = self.completed_date

        award: dict[str, Any] | None | Unset
        if isinstance(self.award, Unset):
            award = UNSET
        elif isinstance(self.award, AwardRefType0):
            award = self.award.to_dict()
        else:
            award = self.award

        application: dict[str, Any] | None | Unset
        if isinstance(self.application, Unset):
            application = UNSET
        elif isinstance(self.application, ApplicationRefType0):
            application = self.application.to_dict()
        else:
            application = self.application

        project: dict[str, Any] | None | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, ProjectRefType0):
            project = self.project.to_dict()
        else:
            project = self.project

        ethical_review: dict[str, Any] | None | Unset
        if isinstance(self.ethical_review, Unset):
            ethical_review = UNSET
        elif isinstance(self.ethical_review, EthicalReviewRefType0):
            ethical_review = self.ethical_review.to_dict()
        else:
            ethical_review = self.ethical_review

        contract: dict[str, Any] | None | Unset
        if isinstance(self.contract, Unset):
            contract = UNSET
        elif isinstance(self.contract, ContractRefType0):
            contract = self.contract.to_dict()
        else:
            contract = self.contract

        completed_by: dict[str, Any] | None | Unset
        if isinstance(self.completed_by, Unset):
            completed_by = UNSET
        elif isinstance(self.completed_by, UserRefType0):
            completed_by = self.completed_by.to_dict()
        else:
            completed_by = self.completed_by

        milestone_state: dict[str, Any] | None | Unset
        if isinstance(self.milestone_state, Unset):
            milestone_state = UNSET
        elif isinstance(self.milestone_state, ClassificationRefType0):
            milestone_state = self.milestone_state.to_dict()
        else:
            milestone_state = self.milestone_state

        reminders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = []
            for reminders_item_data in self.reminders:
                reminders_item = reminders_item_data.to_dict()
                reminders.append(reminders_item)

        administrative_role: None | str | Unset
        if isinstance(self.administrative_role, Unset):
            administrative_role = UNSET
        else:
            administrative_role = self.administrative_role

        academic_role: dict[str, Any] | None | Unset
        if isinstance(self.academic_role, Unset):
            academic_role = UNSET
        elif isinstance(self.academic_role, ClassificationRefType0):
            academic_role = self.academic_role.to_dict()
        else:
            academic_role = self.academic_role

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, FormattedLocalizedStringType0):
            description = self.description.to_dict()
        else:
            description = self.description

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ClassificationRefType0):
            category = self.category.to_dict()
        else:
            category = self.category

        documents: list[dict[str, Any]] | None | Unset
        if isinstance(self.documents, Unset):
            documents = UNSET
        elif isinstance(self.documents, list):
            documents = []
            for documents_type_0_item_data in self.documents:
                documents_type_0_item = documents_type_0_item_data.to_dict()
                documents.append(documents_type_0_item)

        else:
            documents = self.documents

        responsible_users: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.responsible_users, Unset):
            responsible_users = []
            for responsible_users_item_data in self.responsible_users:
                responsible_users_item: dict[str, Any] | None
                if isinstance(responsible_users_item_data, UserRefType0):
                    responsible_users_item = responsible_users_item_data.to_dict()
                else:
                    responsible_users_item = responsible_users_item_data
                responsible_users.append(responsible_users_item)

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

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "milestoneType": milestone_type,
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
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if completion_state is not UNSET:
            field_dict["completionState"] = completion_state
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if award is not UNSET:
            field_dict["award"] = award
        if application is not UNSET:
            field_dict["application"] = application
        if project is not UNSET:
            field_dict["project"] = project
        if ethical_review is not UNSET:
            field_dict["ethicalReview"] = ethical_review
        if contract is not UNSET:
            field_dict["contract"] = contract
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if milestone_state is not UNSET:
            field_dict["milestoneState"] = milestone_state
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if administrative_role is not UNSET:
            field_dict["administrativeRole"] = administrative_role
        if academic_role is not UNSET:
            field_dict["academicRole"] = academic_role
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if documents is not UNSET:
            field_dict["documents"] = documents
        if responsible_users is not UNSET:
            field_dict["responsibleUsers"] = responsible_users
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.classification_ref_type_0 import ClassificationRefType0
        from ..models.contract_ref_type_0 import ContractRefType0
        from ..models.ethical_review_ref_type_0 import EthicalReviewRefType0
        from ..models.formatted_localized_string_type_0 import (
            FormattedLocalizedStringType0,
        )
        from ..models.identifier import Identifier
        from ..models.localized_string_type_0 import LocalizedStringType0
        from ..models.milestone_document import MilestoneDocument
        from ..models.milestone_reminder import MilestoneReminder
        from ..models.project_ref_type_0 import ProjectRefType0
        from ..models.user_ref_type_0 import UserRefType0

        d = dict(src_dict)

        def _parse_title(data: object) -> LocalizedStringType0 | None:
            if data is None:
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
            return cast(LocalizedStringType0 | None, data)

        title = _parse_title(d.pop("title"))

        milestone_type = MilestoneMilestoneType(d.pop("milestoneType"))

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

        def _parse_deadline(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_type_0 = isoparse(data).date()

                return deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        deadline = _parse_deadline(d.pop("deadline", UNSET))

        def _parse_completion_state(
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

        completion_state = _parse_completion_state(d.pop("completionState", UNSET))

        def _parse_completed_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_date_type_0 = isoparse(data).date()

                return completed_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        completed_date = _parse_completed_date(d.pop("completedDate", UNSET))

        def _parse_award(data: object) -> AwardRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_award_ref_type_0 = AwardRefType0.from_dict(data)

                return componentsschemas_award_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwardRefType0 | None | Unset, data)

        award = _parse_award(d.pop("award", UNSET))

        def _parse_application(data: object) -> ApplicationRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_application_ref_type_0 = (
                    ApplicationRefType0.from_dict(data)
                )

                return componentsschemas_application_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicationRefType0 | None | Unset, data)

        application = _parse_application(d.pop("application", UNSET))

        def _parse_project(data: object) -> None | ProjectRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_project_ref_type_0 = ProjectRefType0.from_dict(data)

                return componentsschemas_project_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProjectRefType0 | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_ethical_review(data: object) -> EthicalReviewRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ethical_review_ref_type_0 = (
                    EthicalReviewRefType0.from_dict(data)
                )

                return componentsschemas_ethical_review_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EthicalReviewRefType0 | None | Unset, data)

        ethical_review = _parse_ethical_review(d.pop("ethicalReview", UNSET))

        def _parse_contract(data: object) -> ContractRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_contract_ref_type_0 = ContractRefType0.from_dict(data)

                return componentsschemas_contract_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContractRefType0 | None | Unset, data)

        contract = _parse_contract(d.pop("contract", UNSET))

        def _parse_completed_by(data: object) -> None | Unset | UserRefType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                return componentsschemas_user_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRefType0, data)

        completed_by = _parse_completed_by(d.pop("completedBy", UNSET))

        def _parse_milestone_state(
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

        milestone_state = _parse_milestone_state(d.pop("milestoneState", UNSET))

        _reminders = d.pop("reminders", UNSET)
        reminders: list[MilestoneReminder] | Unset = UNSET
        if _reminders is not UNSET:
            reminders = []
            for reminders_item_data in _reminders:
                reminders_item = MilestoneReminder.from_dict(reminders_item_data)

                reminders.append(reminders_item)

        def _parse_administrative_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        administrative_role = _parse_administrative_role(
            d.pop("administrativeRole", UNSET)
        )

        def _parse_academic_role(data: object) -> ClassificationRefType0 | None | Unset:
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

        academic_role = _parse_academic_role(d.pop("academicRole", UNSET))

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

        def _parse_category(data: object) -> ClassificationRefType0 | None | Unset:
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

        category = _parse_category(d.pop("category", UNSET))

        def _parse_documents(data: object) -> list[MilestoneDocument] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                documents_type_0 = []
                _documents_type_0 = data
                for documents_type_0_item_data in _documents_type_0:
                    documents_type_0_item = MilestoneDocument.from_dict(
                        documents_type_0_item_data
                    )

                    documents_type_0.append(documents_type_0_item)

                return documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MilestoneDocument] | None | Unset, data)

        documents = _parse_documents(d.pop("documents", UNSET))

        _responsible_users = d.pop("responsibleUsers", UNSET)
        responsible_users: list[None | UserRefType0] | Unset = UNSET
        if _responsible_users is not UNSET:
            responsible_users = []
            for responsible_users_item_data in _responsible_users:

                def _parse_responsible_users_item(data: object) -> None | UserRefType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_user_ref_type_0 = UserRefType0.from_dict(data)

                        return componentsschemas_user_ref_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UserRefType0, data)

                responsible_users_item = _parse_responsible_users_item(
                    responsible_users_item_data
                )

                responsible_users.append(responsible_users_item)

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

        system_name = d.pop("systemName", UNSET)

        milestone = cls(
            title=title,
            milestone_type=milestone_type,
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
            deadline=deadline,
            completion_state=completion_state,
            completed_date=completed_date,
            award=award,
            application=application,
            project=project,
            ethical_review=ethical_review,
            contract=contract,
            completed_by=completed_by,
            milestone_state=milestone_state,
            reminders=reminders,
            administrative_role=administrative_role,
            academic_role=academic_role,
            description=description,
            category=category,
            documents=documents,
            responsible_users=responsible_users,
            identifiers=identifiers,
            system_name=system_name,
        )

        milestone.additional_properties = d
        return milestone

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
