"""Contains all the data models used in inputs/outputs"""

from .abstract_activity_person_association import AbstractActivityPersonAssociation
from .abstract_applicant_association import AbstractApplicantAssociation
from .abstract_award_holder_association import AbstractAwardHolderAssociation
from .abstract_classified_contract_person_association import (
    AbstractClassifiedContractPersonAssociation,
)
from .abstract_classified_course_lecturer_association import (
    AbstractClassifiedCourseLecturerAssociation,
)
from .abstract_classified_ethical_review_person_association import (
    AbstractClassifiedEthicalReviewPersonAssociation,
)
from .abstract_contributor_association import AbstractContributorAssociation
from .abstract_data_set_contributor_association import (
    AbstractDataSetContributorAssociation,
)
from .abstract_data_set_person_association import AbstractDataSetPersonAssociation
from .abstract_editorial_work_association import AbstractEditorialWorkAssociation
from .abstract_equipment_person_association import AbstractEquipmentPersonAssociation
from .abstract_examinee_association_type_0 import AbstractExamineeAssociationType0
from .abstract_impact_classified_participant_association import (
    AbstractImpactClassifiedParticipantAssociation,
)
from .abstract_participant_association import AbstractParticipantAssociation
from .abstract_press_media_person_association import AbstractPressMediaPersonAssociation
from .abstract_prize_receiver_association import AbstractPrizeReceiverAssociation
from .abstract_student_thesis_contributor_association import (
    AbstractStudentThesisContributorAssociation,
)
from .academic_qualification import AcademicQualification
from .access_definition_ref_type_0 import AccessDefinitionRefType0
from .account import Account
from .account_entry import AccountEntry
from .activities_query import ActivitiesQuery
from .activity import Activity
from .activity_abstract_association import ActivityAbstractAssociation
from .activity_awardable_association import ActivityAwardableAssociation
from .activity_dataset_association import ActivityDatasetAssociation
from .activity_event_association import ActivityEventAssociation
from .activity_external_organization_association import (
    ActivityExternalOrganizationAssociation,
)
from .activity_list_result import ActivityListResult
from .activity_organization_association import ActivityOrganizationAssociation
from .activity_prize_association import ActivityPrizeAssociation
from .activity_project_association import ActivityProjectAssociation
from .activity_ref_type_0 import ActivityRefType0
from .activity_visitor_association import ActivityVisitorAssociation
from .additional_file_electronic_version import AdditionalFileElectronicVersion
from .additional_issn_type_0 import AdditionalISSNType0
from .address_type_0 import AddressType0
from .allowed_keyword_group_configuration import AllowedKeywordGroupConfiguration
from .allowed_keyword_group_configuration_list import (
    AllowedKeywordGroupConfigurationList,
)
from .allowed_template import AllowedTemplate
from .allowed_template_list_result import AllowedTemplateListResult
from .alternative_issn import AlternativeISSN
from .anzsrc_2008_field_of_research_ref_type_0 import Anzsrc2008FieldOfResearchRefType0
from .anzsrc_2020_field_of_research_ref_type_0 import Anzsrc2020FieldOfResearchRefType0
from .anzsrc_2020_socio_economic_objective_ref_type_0 import (
    Anzsrc2020SocioEconomicObjectiveRefType0,
)
from .anzsrc_2020_type_of_activity_ref_type_0 import Anzsrc2020TypeOfActivityRefType0
from .api_string_list_result import APIStringListResult
from .api_string_to_string_list_map_result import APIStringToStringListMapResult
from .api_string_to_string_list_map_result_items import (
    APIStringToStringListMapResultItems,
)
from .application import Application
from .application_budget import ApplicationBudget
from .application_budget_result import ApplicationBudgetResult
from .application_cluster import ApplicationCluster
from .application_cluster_list_result import ApplicationClusterListResult
from .application_cluster_ref_type_0 import ApplicationClusterRefType0
from .application_cluster_status import ApplicationClusterStatus
from .application_document import ApplicationDocument
from .application_document_file_store_locations import (
    ApplicationDocumentFileStoreLocations,
)
from .application_external_financial_funding_collaborator_association import (
    ApplicationExternalFinancialFundingCollaboratorAssociation,
)
from .application_external_non_financial_funding_collaborator_association import (
    ApplicationExternalNonFinancialFundingCollaboratorAssociation,
)
from .application_financial_funding_association import (
    ApplicationFinancialFundingAssociation,
)
from .application_financial_funding_collaborator_association import (
    ApplicationFinancialFundingCollaboratorAssociation,
)
from .application_funding_association import ApplicationFundingAssociation
from .application_funding_budget_association import ApplicationFundingBudgetAssociation
from .application_internal_financial_funding_collaborator_association import (
    ApplicationInternalFinancialFundingCollaboratorAssociation,
)
from .application_internal_non_financial_funding_collaborator_association import (
    ApplicationInternalNonFinancialFundingCollaboratorAssociation,
)
from .application_list_result import ApplicationListResult
from .application_non_financial_funding_association import (
    ApplicationNonFinancialFundingAssociation,
)
from .application_non_financial_funding_collaborator_association import (
    ApplicationNonFinancialFundingCollaboratorAssociation,
)
from .application_ref_type_0 import ApplicationRefType0
from .application_status import ApplicationStatus
from .applications_query import ApplicationsQuery
from .article_processing_charge import ArticleProcessingCharge
from .article_version import ArticleVersion
from .article_version_key import ArticleVersionKey
from .assignable_role import AssignableRole
from .assignable_role_ref import AssignableRoleRef
from .attendance import Attendance
from .author_collaboration import AuthorCollaboration
from .author_collaboration_contributor_association import (
    AuthorCollaborationContributorAssociation,
)
from .author_collaboration_list_result import AuthorCollaborationListResult
from .author_collaboration_query import AuthorCollaborationQuery
from .author_collaboration_ref_type_0 import AuthorCollaborationRefType0
from .award import Award
from .award_budget import AwardBudget
from .award_budget_result import AwardBudgetResult
from .award_cluster import AwardCluster
from .award_cluster_list_result import AwardClusterListResult
from .award_cluster_ref_type_0 import AwardClusterRefType0
from .award_document import AwardDocument
from .award_document_file_store_locations import AwardDocumentFileStoreLocations
from .award_external_financial_funding_collaborator_association import (
    AwardExternalFinancialFundingCollaboratorAssociation,
)
from .award_external_non_financial_funding_collaborator_association import (
    AwardExternalNonFinancialFundingCollaboratorAssociation,
)
from .award_financial_funding_association import AwardFinancialFundingAssociation
from .award_financial_funding_collaborator_association import (
    AwardFinancialFundingCollaboratorAssociation,
)
from .award_funding_association import AwardFundingAssociation
from .award_funding_budget_association import AwardFundingBudgetAssociation
from .award_internal_financial_funding_collaborator_association import (
    AwardInternalFinancialFundingCollaboratorAssociation,
)
from .award_internal_non_financial_funding_collaborator_association import (
    AwardInternalNonFinancialFundingCollaboratorAssociation,
)
from .award_list_result import AwardListResult
from .award_management_application import AwardManagementApplication
from .award_management_application_funder_reply import (
    AwardManagementApplicationFunderReply,
)
from .award_management_award import AwardManagementAward
from .award_management_project import AwardManagementProject
from .award_non_financial_funding_association import AwardNonFinancialFundingAssociation
from .award_non_financial_funding_collaborator_association import (
    AwardNonFinancialFundingCollaboratorAssociation,
)
from .award_ref_type_0 import AwardRefType0
from .award_status import AwardStatus
from .awards_query import AwardsQuery
from .basic_application import BasicApplication
from .basic_award import BasicAward
from .basic_project import BasicProject
from .book_anthology import BookAnthology
from .book_series_journal_association import BookSeriesJournalAssociation
from .case_note import CaseNote
from .cerif_address_type_0 import CERIFAddressType0
from .classification import Classification
from .classification_ref_list import ClassificationRefList
from .classification_ref_type_0 import ClassificationRefType0
from .classification_relation import ClassificationRelation
from .classification_scheme import ClassificationScheme
from .classification_scheme_list import ClassificationSchemeList
from .classification_scheme_ref_type_0 import ClassificationSchemeRefType0
from .classification_scheme_relation import ClassificationSchemeRelation
from .classifications_keyword_group import ClassificationsKeywordGroup
from .classified_address import ClassifiedAddress
from .classified_case_note_source import ClassifiedCaseNoteSource
from .classified_course_developed_by_association import (
    ClassifiedCourseDevelopedByAssociation,
)
from .classified_formatted_localized_value import ClassifiedFormattedLocalizedValue
from .classified_id import ClassifiedId
from .classified_localized_value import ClassifiedLocalizedValue
from .classified_name import ClassifiedName
from .classified_value import ClassifiedValue
from .collaborator_association import CollaboratorAssociation
from .compound_date_range import CompoundDateRange
from .compound_date_type_0 import CompoundDateType0
from .concept import Concept
from .concept_list_result import ConceptListResult
from .concept_query import ConceptQuery
from .concept_ref_type_0 import ConceptRefType0
from .conference_series import ConferenceSeries
from .conference_series_list_result import ConferenceSeriesListResult
from .conference_series_query import ConferenceSeriesQuery
from .conference_series_ref_type_0 import ConferenceSeriesRefType0
from .conflict_problem_details import ConflictProblemDetails
from .consultancy import Consultancy
from .content_ref_list_result import ContentRefListResult
from .content_ref_type_0 import ContentRefType0
from .contract import Contract
from .contract_application_association import ContractApplicationAssociation
from .contract_award_association import ContractAwardAssociation
from .contract_collaborator_association import ContractCollaboratorAssociation
from .contract_contract_association import ContractContractAssociation
from .contract_curtailed import ContractCurtailed
from .contract_document import ContractDocument
from .contract_document_file_store_locations import ContractDocumentFileStoreLocations
from .contract_extended import ContractExtended
from .contract_list_result import ContractListResult
from .contract_negotiation_award_status import ContractNegotiationAwardStatus
from .contract_priority import ContractPriority
from .contract_query import ContractQuery
from .contract_ref_type_0 import ContractRefType0
from .contribution_to_book_anthology import ContributionToBookAnthology
from .contribution_to_conference import ContributionToConference
from .contribution_to_journal import ContributionToJournal
from .contribution_to_memorandum import ContributionToMemorandum
from .contribution_to_periodical import ContributionToPeriodical
from .course import Course
from .course_file import CourseFile
from .course_file_file_store_locations import CourseFileFileStoreLocations
from .course_list_result import CourseListResult
from .course_occurrence import CourseOccurrence
from .course_ref_type_0 import CourseRefType0
from .courses_query import CoursesQuery
from .currency_amount import CurrencyAmount
from .curriculum_vitae_ref_type_0 import CurriculumVitaeRefType0
from .curtailed_award_status import CurtailedAwardStatus
from .custom_defined_field_boolean_type_0 import CustomDefinedFieldBooleanType0
from .custom_defined_field_classification_type_0 import (
    CustomDefinedFieldClassificationType0,
)
from .custom_defined_field_configuration_ref_type_0 import (
    CustomDefinedFieldConfigurationRefType0,
)
from .custom_defined_field_date_type_0 import CustomDefinedFieldDateType0
from .custom_defined_field_decimal_type_0 import CustomDefinedFieldDecimalType0
from .custom_defined_field_integer_type_0 import CustomDefinedFieldIntegerType0
from .custom_defined_field_string_type_0 import CustomDefinedFieldStringType0
from .custom_defined_field_type_0 import CustomDefinedFieldType0
from .custom_defined_fields_type_0 import CustomDefinedFieldsType0
from .data_set import DataSet
from .data_set_activity_association import DataSetActivityAssociation
from .data_set_association import DataSetAssociation
from .data_set_author_collaboration_contributor_association import (
    DataSetAuthorCollaborationContributorAssociation,
)
from .data_set_awardable_association import DataSetAwardableAssociation
from .data_set_document import DataSetDocument
from .data_set_document_file_store_locations import DataSetDocumentFileStoreLocations
from .data_set_doi import DataSetDoi
from .data_set_equipment_association import DataSetEquipmentAssociation
from .data_set_external_contributor_association import (
    DataSetExternalContributorAssociation,
)
from .data_set_geo_location import DataSetGeoLocation
from .data_set_impact_association import DataSetImpactAssociation
from .data_set_internal_contributor_association import (
    DataSetInternalContributorAssociation,
)
from .data_set_legal_condition import DataSetLegalCondition
from .data_set_list_result import DataSetListResult
from .data_set_physical_data import DataSetPhysicalData
from .data_set_press_media_association import DataSetPressMediaAssociation
from .data_set_prize_association import DataSetPrizeAssociation
from .data_set_project_association import DataSetProjectAssociation
from .data_set_ref_type_0 import DataSetRefType0
from .data_set_research_output_association import DataSetResearchOutputAssociation
from .data_set_student_thesis_association import DataSetStudentThesisAssociation
from .data_sets_query import DataSetsQuery
from .date_range import DateRange
from .declined_award_status_type_0 import DeclinedAwardStatusType0
from .dependency_violation_problem_details import DependencyViolationProblemDetails
from .deprecated_date_range import DeprecatedDateRange
from .deprecated_system_currency_amount import DeprecatedSystemCurrencyAmount
from .disciplines_association import DisciplinesAssociation
from .disciplines_association_list_result import DisciplinesAssociationListResult
from .disciplines_associations_query import DisciplinesAssociationsQuery
from .disciplines_discipline import DisciplinesDiscipline
from .disciplines_discipline_assignment import DisciplinesDisciplineAssignment
from .disciplines_discipline_list_result import DisciplinesDisciplineListResult
from .disciplines_discipline_scheme import DisciplinesDisciplineScheme
from .disciplines_discipline_scheme_list_result import (
    DisciplinesDisciplineSchemeListResult,
)
from .document import Document
from .document_file_store_locations import DocumentFileStoreLocations
from .doi_electronic_version import DoiElectronicVersion
from .editorial_work import EditorialWork
from .education import Education
from .education_association import EducationAssociation
from .education_list_result import EducationListResult
from .education_query import EducationQuery
from .education_ref_type_0 import EducationRefType0
from .electronic_issn import ElectronicISSN
from .electronic_version_file import ElectronicVersionFile
from .electronic_version_file_file_store_locations import (
    ElectronicVersionFileFileStoreLocations,
)
from .electronic_version_type_0 import ElectronicVersionType0
from .equipment import Equipment
from .equipment_awardable_association import EquipmentAwardableAssociation
from .equipment_data_set_association import EquipmentDataSetAssociation
from .equipment_details import EquipmentDetails
from .equipment_impact_association import EquipmentImpactAssociation
from .equipment_list_result import EquipmentListResult
from .equipment_press_media_association import EquipmentPressMediaAssociation
from .equipment_prize_association import EquipmentPrizeAssociation
from .equipment_project_association import EquipmentProjectAssociation
from .equipment_query import EquipmentQuery
from .equipment_ref_type_0 import EquipmentRefType0
from .ethical_review import EthicalReview
from .ethical_review_application_association import EthicalReviewApplicationAssociation
from .ethical_review_award_association import EthicalReviewAwardAssociation
from .ethical_review_document import EthicalReviewDocument
from .ethical_review_document_file_store_locations import (
    EthicalReviewDocumentFileStoreLocations,
)
from .ethical_review_ethical_review_reply import EthicalReviewEthicalReviewReply
from .ethical_review_list_result import EthicalReviewListResult
from .ethical_review_query import EthicalReviewQuery
from .ethical_review_ref_type_0 import EthicalReviewRefType0
from .event import Event
from .event_list_result import EventListResult
from .event_membership_association import EventMembershipAssociation
from .event_ref_type_0 import EventRefType0
from .events_query import EventsQuery
from .evidence_contact_information import EvidenceContactInformation
from .examination import Examination
from .extended_award_status import ExtendedAwardStatus
from .external_activity_person_association import ExternalActivityPersonAssociation
from .external_applicant_association import ExternalApplicantAssociation
from .external_appointment import ExternalAppointment
from .external_award_holder_association import ExternalAwardHolderAssociation
from .external_classified_contract_person_association import (
    ExternalClassifiedContractPersonAssociation,
)
from .external_classified_course_lecturer_association import (
    ExternalClassifiedCourseLecturerAssociation,
)
from .external_classified_ethical_review_person_association import (
    ExternalClassifiedEthicalReviewPersonAssociation,
)
from .external_collaborator_association import ExternalCollaboratorAssociation
from .external_contributor_association import ExternalContributorAssociation
from .external_data_set_person_association import ExternalDataSetPersonAssociation
from .external_equipment_person_association import ExternalEquipmentPersonAssociation
from .external_examinee_association import ExternalExamineeAssociation
from .external_funding_opportunity import ExternalFundingOpportunity
from .external_impact_classified_participant_association import (
    ExternalImpactClassifiedParticipantAssociation,
)
from .external_organization import ExternalOrganization
from .external_organization_list import ExternalOrganizationList
from .external_organization_list_result import ExternalOrganizationListResult
from .external_organization_ref_list import ExternalOrganizationRefList
from .external_organization_ref_type_0 import ExternalOrganizationRefType0
from .external_organizations_query import ExternalOrganizationsQuery
from .external_participant_association import ExternalParticipantAssociation
from .external_person import ExternalPerson
from .external_person_list_result import ExternalPersonListResult
from .external_person_ref_type_0 import ExternalPersonRefType0
from .external_persons_query import ExternalPersonsQuery
from .external_press_media_person_association import ExternalPressMediaPersonAssociation
from .external_prize_receiver_association import ExternalPrizeReceiverAssociation
from .external_student_thesis_contributor_association import (
    ExternalStudentThesisContributorAssociation,
)
from .file_electronic_version import FileElectronicVersion
from .fingerprint import Fingerprint
from .fingerprint_list_result import FingerprintListResult
from .fingerprint_query import FingerprintQuery
from .fingerprint_ref_type_0 import FingerprintRefType0
from .formatted_localized_string_type_0 import FormattedLocalizedStringType0
from .formatted_string import FormattedString
from .free_keywords_keyword_group import FreeKeywordsKeywordGroup
from .full_keyword_group import FullKeywordGroup
from .funding_details import FundingDetails
from .funding_opportunities_query import FundingOpportunitiesQuery
from .funding_opportunity import FundingOpportunity
from .funding_opportunity_academic_degree_eligibility import (
    FundingOpportunityAcademicDegreeEligibility,
)
from .funding_opportunity_academic_degree_eligibility_eligibility_fulfilment_type import (
    FundingOpportunityAcademicDegreeEligibilityEligibilityFulfilmentType,
)
from .funding_opportunity_contact_email import FundingOpportunityContactEmail
from .funding_opportunity_contact_person import FundingOpportunityContactPerson
from .funding_opportunity_document import FundingOpportunityDocument
from .funding_opportunity_document_file_store_locations import (
    FundingOpportunityDocumentFileStoreLocations,
)
from .funding_opportunity_eligibility import FundingOpportunityEligibility
from .funding_opportunity_eligibility_eligibility_fulfilment_type import (
    FundingOpportunityEligibilityEligibilityFulfilmentType,
)
from .funding_opportunity_list_result import FundingOpportunityListResult
from .funding_opportunity_ref_type_0 import FundingOpportunityRefType0
from .gender_type_0 import GenderType0
from .gender_type_0_key import GenderType0Key
from .generic_content_ref_type_0 import GenericContentRefType0
from .generic_problem_details import GenericProblemDetails
from .geo_location_type_0 import GeoLocationType0
from .global_role_assignment import GlobalRoleAssignment
from .highlighted_content import HighlightedContent
from .honorary_staff_organization_association import (
    HonoraryStaffOrganizationAssociation,
)
from .host_visitor import HostVisitor
from .id import Id
from .identifier import Identifier
from .image_file import ImageFile
from .image_file_file_store_locations import ImageFileFileStoreLocations
from .impact import Impact
from .impact_activity_association import ImpactActivityAssociation
from .impact_awardable_association import ImpactAwardableAssociation
from .impact_data_set_association import ImpactDataSetAssociation
from .impact_evidence import ImpactEvidence
from .impact_impact_association import ImpactImpactAssociation
from .impact_list_result import ImpactListResult
from .impact_press_media_association import ImpactPressMediaAssociation
from .impact_prize_association import ImpactPrizeAssociation
from .impact_project_association import ImpactProjectAssociation
from .impact_query import ImpactQuery
from .impact_ref_type_0 import ImpactRefType0
from .impact_research_output_association import ImpactResearchOutputAssociation
from .impact_student_thesis_association import ImpactStudentThesisAssociation
from .internal_activity_person_association import InternalActivityPersonAssociation
from .internal_applicant_association import InternalApplicantAssociation
from .internal_award_holder_association import InternalAwardHolderAssociation
from .internal_classified_contract_person_association import (
    InternalClassifiedContractPersonAssociation,
)
from .internal_classified_course_lecturer_association import (
    InternalClassifiedCourseLecturerAssociation,
)
from .internal_classified_ethical_review_person_association import (
    InternalClassifiedEthicalReviewPersonAssociation,
)
from .internal_collaborator_association import InternalCollaboratorAssociation
from .internal_contributor_association import InternalContributorAssociation
from .internal_data_set_person_association import InternalDataSetPersonAssociation
from .internal_equipment_person_association import InternalEquipmentPersonAssociation
from .internal_examinee_association import InternalExamineeAssociation
from .internal_funding_opportunity import InternalFundingOpportunity
from .internal_impact_classified_participant_association import (
    InternalImpactClassifiedParticipantAssociation,
)
from .internal_or_external_supervisor import InternalOrExternalSupervisor
from .internal_participant_association import InternalParticipantAssociation
from .internal_press_media_person_association import InternalPressMediaPersonAssociation
from .internal_prize_receiver_association import InternalPrizeReceiverAssociation
from .internal_student_thesis_contributor_association import (
    InternalStudentThesisContributorAssociation,
)
from .internally_approved_award_status import InternallyApprovedAwardStatus
from .issn import ISSN
from .issn_ref import ISSNRef
from .journal import Journal
from .journal_association_type_0 import JournalAssociationType0
from .journal_editorial_work_association import JournalEditorialWorkAssociation
from .journal_list_result import JournalListResult
from .journal_ref_type_0 import JournalRefType0
from .journal_title import JournalTitle
from .journal_title_ref import JournalTitleRef
from .journals_query import JournalsQuery
from .keyword import Keyword
from .keyword_container import KeywordContainer
from .keyword_group import KeywordGroup
from .keyword_group_configuration import KeywordGroupConfiguration
from .keyword_group_configuration_list import KeywordGroupConfigurationList
from .keyword_group_configuration_ref_type_0 import KeywordGroupConfigurationRefType0
from .keyword_group_configuration_selection_mode_sorting_order import (
    KeywordGroupConfigurationSelectionModeSortingOrder,
)
from .keyword_group_configuration_userdefined_keyword_edit_mode import (
    KeywordGroupConfigurationUserdefinedKeywordEditMode,
)
from .label import Label
from .link import Link
from .link_electronic_version import LinkElectronicVersion
from .link_identifier import LinkIdentifier
from .local_role_assignment import LocalRoleAssignment
from .locales_list import LocalesList
from .localized_string_type_0 import LocalizedStringType0
from .media_coverage import MediaCoverage
from .media_coverage_coverage_type import MediaCoverageCoverageType
from .membership import Membership
from .memorandum import Memorandum
from .metric_collection import MetricCollection
from .metric_collection_definition import MetricCollectionDefinition
from .metric_collection_definition_list import MetricCollectionDefinitionList
from .metric_collection_item import MetricCollectionItem
from .metric_definition import MetricDefinition
from .metric_value import MetricValue
from .milestone import Milestone
from .milestone_document import MilestoneDocument
from .milestone_document_file_store_locations import MilestoneDocumentFileStoreLocations
from .milestone_list_result import MilestoneListResult
from .milestone_milestone_type import MilestoneMilestoneType
from .milestone_query import MilestoneQuery
from .milestone_ref_type_0 import MilestoneRefType0
from .milestone_reminder import MilestoneReminder
from .milestone_reminder_time_unit import MilestoneReminderTimeUnit
from .name import Name
from .non_textual import NonTextual
from .note import Note
from .note_list_result import NoteListResult
from .open_access import OpenAccess
from .orderings_list import OrderingsList
from .organization import Organization
from .organization_list_result import OrganizationListResult
from .organization_or_external_organization_ref_type_0 import (
    OrganizationOrExternalOrganizationRefType0,
)
from .organization_ref_type_0 import OrganizationRefType0
from .organizations_query import OrganizationsQuery
from .other_activity import OtherActivity
from .other_contribution import OtherContribution
from .page_information import PageInformation
from .participant_time_spent import ParticipantTimeSpent
from .participant_time_tracking_association import ParticipantTimeTrackingAssociation
from .patent import Patent
from .person import Person
from .person_classified_leave_of_absence import PersonClassifiedLeaveOfAbsence
from .person_expertise import PersonExpertise
from .person_expertise_list_result import PersonExpertiseListResult
from .person_expertise_query import PersonExpertiseQuery
from .person_expertise_ref_type_0 import PersonExpertiseRefType0
from .person_list_result import PersonListResult
from .person_organization_association_type_0 import PersonOrganizationAssociationType0
from .person_ref_type_0 import PersonRefType0
from .person_supervisee_association import PersonSuperviseeAssociation
from .person_supervisee_association_list_result import (
    PersonSuperviseeAssociationListResult,
)
from .person_supervisor_association import PersonSupervisorAssociation
from .persons_query import PersonsQuery
from .press_media import PressMedia
from .press_media_activity_association import PressMediaActivityAssociation
from .press_media_awardable_association import PressMediaAwardableAssociation
from .press_media_data_set_association import PressMediaDataSetAssociation
from .press_media_equipment_association import PressMediaEquipmentAssociation
from .press_media_impact_association import PressMediaImpactAssociation
from .press_media_list_result import PressMediaListResult
from .press_media_press_media_association import PressMediaPressMediaAssociation
from .press_media_prize_association import PressMediaPrizeAssociation
from .press_media_project_association import PressMediaProjectAssociation
from .press_media_query import PressMediaQuery
from .press_media_ref_type_0 import PressMediaRefType0
from .press_media_research_output_association import PressMediaResearchOutputAssociation
from .press_media_student_thesis_association import PressMediaStudentThesisAssociation
from .primary_id import PrimaryId
from .prize import Prize
from .prize_activity_association import PrizeActivityAssociation
from .prize_association import PrizeAssociation
from .prize_awardable_association import PrizeAwardableAssociation
from .prize_data_set_association import PrizeDataSetAssociation
from .prize_equipment_association import PrizeEquipmentAssociation
from .prize_impact_association import PrizeImpactAssociation
from .prize_list_result import PrizeListResult
from .prize_press_media_association import PrizePressMediaAssociation
from .prize_project_association import PrizeProjectAssociation
from .prize_ref_type_0 import PrizeRefType0
from .prize_research_output_association import PrizeResearchOutputAssociation
from .prize_student_thesis_association import PrizeStudentThesisAssociation
from .prizes_query import PrizesQuery
from .problem_details import ProblemDetails
from .professional_qualification import ProfessionalQualification
from .project import Project
from .project_association import ProjectAssociation
from .project_awardable_association_type_0 import ProjectAwardableAssociationType0
from .project_curtailed import ProjectCurtailed
from .project_list_result import ProjectListResult
from .project_ref_type_0 import ProjectRefType0
from .projects_query import ProjectsQuery
from .publication_series import PublicationSeries
from .publication_status import PublicationStatus
from .publisher import Publisher
from .publisher_editorial_work_association import PublisherEditorialWorkAssociation
from .publisher_list_result import PublisherListResult
from .publisher_ref_type_0 import PublisherRefType0
from .publishers_query import PublishersQuery
from .ranked_concept import RankedConcept
from .ref_2014_unit_of_assessment_ref_type_0 import Ref2014UnitOfAssessmentRefType0
from .ref_2020_unit_of_assessment_ref_type_0 import Ref2020UnitOfAssessmentRefType0
from .remote_file import RemoteFile
from .remote_file_file_state import RemoteFileFileState
from .research_output import ResearchOutput
from .research_output_association_type_0 import ResearchOutputAssociationType0
from .research_output_awardable_association import ResearchOutputAwardableAssociation
from .research_output_data_set_association_type_0 import (
    ResearchOutputDataSetAssociationType0,
)
from .research_output_impact_association_type_0 import (
    ResearchOutputImpactAssociationType0,
)
from .research_output_list_result import ResearchOutputListResult
from .research_output_peer_review_configuration import (
    ResearchOutputPeerReviewConfiguration,
)
from .research_output_peer_review_configuration_combination import (
    ResearchOutputPeerReviewConfigurationCombination,
)
from .research_output_peer_review_configuration_combination_peer_reviewable import (
    ResearchOutputPeerReviewConfigurationCombinationPeerReviewable,
)
from .research_output_peer_review_configuration_list_result import (
    ResearchOutputPeerReviewConfigurationListResult,
)
from .research_output_press_media_association_type_0 import (
    ResearchOutputPressMediaAssociationType0,
)
from .research_output_prize_association_type_0 import (
    ResearchOutputPrizeAssociationType0,
)
from .research_output_ref_type_0 import ResearchOutputRefType0
from .research_output_student_thesis_association_type_0 import (
    ResearchOutputStudentThesisAssociationType0,
)
from .research_outputs_query import ResearchOutputsQuery
from .researcher_commitment import ResearcherCommitment
from .review_ref_type_0 import ReviewRefType0
from .semester import Semester
from .semester_list_result import SemesterListResult
from .semester_query import SemesterQuery
from .semester_ref_type_0 import SemesterRefType0
from .sherpa_romeo_open_access_permission_type_0 import (
    SherpaRomeoOpenAccessPermissionType0,
)
from .sherpa_romeo_policy import SherpaRomeoPolicy
from .specialization import Specialization
from .specialization_list_result import SpecializationListResult
from .specialization_query import SpecializationQuery
from .specialization_ref_type_0 import SpecializationRefType0
from .staff_organization_association import StaffOrganizationAssociation
from .student_organization_association import StudentOrganizationAssociation
from .student_organization_association_student_residency_flag import (
    StudentOrganizationAssociationStudentResidencyFlag,
)
from .student_project import StudentProject
from .student_project_appendix_document import StudentProjectAppendixDocument
from .student_project_appendix_document_file_store_locations import (
    StudentProjectAppendixDocumentFileStoreLocations,
)
from .student_project_author import StudentProjectAuthor
from .student_project_document import StudentProjectDocument
from .student_project_document_file_store_locations import (
    StudentProjectDocumentFileStoreLocations,
)
from .student_project_external_collaborator import StudentProjectExternalCollaborator
from .student_project_list_result import StudentProjectListResult
from .student_project_notification_recipient import StudentProjectNotificationRecipient
from .student_project_query import StudentProjectQuery
from .student_project_ref_type_0 import StudentProjectRefType0
from .student_project_supervisor import StudentProjectSupervisor
from .student_theses_query import StudentThesesQuery
from .student_thesis import StudentThesis
from .student_thesis_awardable_association import StudentThesisAwardableAssociation
from .student_thesis_document import StudentThesisDocument
from .student_thesis_document_file_store_locations import (
    StudentThesisDocumentFileStoreLocations,
)
from .student_thesis_list_result import StudentThesisListResult
from .student_thesis_ref_type_0 import StudentThesisRefType0
from .supervisor_association import SupervisorAssociation
from .system_currency_amount import SystemCurrencyAmount
from .system_localized_string_type_0 import SystemLocalizedStringType0
from .talk import Talk
from .term import Term
from .terminated_award_status import TerminatedAwardStatus
from .thesaurus import Thesaurus
from .thesaurus_list_result import ThesaurusListResult
from .thesaurus_query import ThesaurusQuery
from .thesaurus_ref_type_0 import ThesaurusRefType0
from .thesis import Thesis
from .uploaded_file import UploadedFile
from .user import User
from .user_list_result import UserListResult
from .user_profile_ref_type_0 import UserProfileRefType0
from .user_ref_type_0 import UserRefType0
from .user_roles import UserRoles
from .validation_error import ValidationError
from .validation_problem_details import ValidationProblemDetails
from .visibility import Visibility
from .visibility_key import VisibilityKey
from .visit_other import VisitOther
from .visiting_scholar_organization_association import (
    VisitingScholarOrganizationAssociation,
)
from .workflow import Workflow
from .workflow_list_result import WorkflowListResult
from .working_paper import WorkingPaper
from .year_month_type_0 import YearMonthType0
from .yearly_budget import YearlyBudget

__all__ = (
    "ISSN",
    "APIStringListResult",
    "APIStringToStringListMapResult",
    "APIStringToStringListMapResultItems",
    "AbstractActivityPersonAssociation",
    "AbstractApplicantAssociation",
    "AbstractAwardHolderAssociation",
    "AbstractClassifiedContractPersonAssociation",
    "AbstractClassifiedCourseLecturerAssociation",
    "AbstractClassifiedEthicalReviewPersonAssociation",
    "AbstractContributorAssociation",
    "AbstractDataSetContributorAssociation",
    "AbstractDataSetPersonAssociation",
    "AbstractEditorialWorkAssociation",
    "AbstractEquipmentPersonAssociation",
    "AbstractExamineeAssociationType0",
    "AbstractImpactClassifiedParticipantAssociation",
    "AbstractParticipantAssociation",
    "AbstractPressMediaPersonAssociation",
    "AbstractPrizeReceiverAssociation",
    "AbstractStudentThesisContributorAssociation",
    "AcademicQualification",
    "AccessDefinitionRefType0",
    "Account",
    "AccountEntry",
    "ActivitiesQuery",
    "Activity",
    "ActivityAbstractAssociation",
    "ActivityAwardableAssociation",
    "ActivityDatasetAssociation",
    "ActivityEventAssociation",
    "ActivityExternalOrganizationAssociation",
    "ActivityListResult",
    "ActivityOrganizationAssociation",
    "ActivityPrizeAssociation",
    "ActivityProjectAssociation",
    "ActivityRefType0",
    "ActivityVisitorAssociation",
    "AdditionalFileElectronicVersion",
    "AdditionalISSNType0",
    "AddressType0",
    "AllowedKeywordGroupConfiguration",
    "AllowedKeywordGroupConfigurationList",
    "AllowedTemplate",
    "AllowedTemplateListResult",
    "AlternativeISSN",
    "Anzsrc2008FieldOfResearchRefType0",
    "Anzsrc2020FieldOfResearchRefType0",
    "Anzsrc2020SocioEconomicObjectiveRefType0",
    "Anzsrc2020TypeOfActivityRefType0",
    "Application",
    "ApplicationBudget",
    "ApplicationBudgetResult",
    "ApplicationCluster",
    "ApplicationClusterListResult",
    "ApplicationClusterRefType0",
    "ApplicationClusterStatus",
    "ApplicationDocument",
    "ApplicationDocumentFileStoreLocations",
    "ApplicationExternalFinancialFundingCollaboratorAssociation",
    "ApplicationExternalNonFinancialFundingCollaboratorAssociation",
    "ApplicationFinancialFundingAssociation",
    "ApplicationFinancialFundingCollaboratorAssociation",
    "ApplicationFundingAssociation",
    "ApplicationFundingBudgetAssociation",
    "ApplicationInternalFinancialFundingCollaboratorAssociation",
    "ApplicationInternalNonFinancialFundingCollaboratorAssociation",
    "ApplicationListResult",
    "ApplicationNonFinancialFundingAssociation",
    "ApplicationNonFinancialFundingCollaboratorAssociation",
    "ApplicationRefType0",
    "ApplicationStatus",
    "ApplicationsQuery",
    "ArticleProcessingCharge",
    "ArticleVersion",
    "ArticleVersionKey",
    "AssignableRole",
    "AssignableRoleRef",
    "Attendance",
    "AuthorCollaboration",
    "AuthorCollaborationContributorAssociation",
    "AuthorCollaborationListResult",
    "AuthorCollaborationQuery",
    "AuthorCollaborationRefType0",
    "Award",
    "AwardBudget",
    "AwardBudgetResult",
    "AwardCluster",
    "AwardClusterListResult",
    "AwardClusterRefType0",
    "AwardDocument",
    "AwardDocumentFileStoreLocations",
    "AwardExternalFinancialFundingCollaboratorAssociation",
    "AwardExternalNonFinancialFundingCollaboratorAssociation",
    "AwardFinancialFundingAssociation",
    "AwardFinancialFundingCollaboratorAssociation",
    "AwardFundingAssociation",
    "AwardFundingBudgetAssociation",
    "AwardInternalFinancialFundingCollaboratorAssociation",
    "AwardInternalNonFinancialFundingCollaboratorAssociation",
    "AwardListResult",
    "AwardManagementApplication",
    "AwardManagementApplicationFunderReply",
    "AwardManagementAward",
    "AwardManagementProject",
    "AwardNonFinancialFundingAssociation",
    "AwardNonFinancialFundingCollaboratorAssociation",
    "AwardRefType0",
    "AwardStatus",
    "AwardsQuery",
    "BasicApplication",
    "BasicAward",
    "BasicProject",
    "BookAnthology",
    "BookSeriesJournalAssociation",
    "CERIFAddressType0",
    "CaseNote",
    "Classification",
    "ClassificationRefList",
    "ClassificationRefType0",
    "ClassificationRelation",
    "ClassificationScheme",
    "ClassificationSchemeList",
    "ClassificationSchemeRefType0",
    "ClassificationSchemeRelation",
    "ClassificationsKeywordGroup",
    "ClassifiedAddress",
    "ClassifiedCaseNoteSource",
    "ClassifiedCourseDevelopedByAssociation",
    "ClassifiedFormattedLocalizedValue",
    "ClassifiedId",
    "ClassifiedLocalizedValue",
    "ClassifiedName",
    "ClassifiedValue",
    "CollaboratorAssociation",
    "CompoundDateRange",
    "CompoundDateType0",
    "Concept",
    "ConceptListResult",
    "ConceptQuery",
    "ConceptRefType0",
    "ConferenceSeries",
    "ConferenceSeriesListResult",
    "ConferenceSeriesQuery",
    "ConferenceSeriesRefType0",
    "ConflictProblemDetails",
    "Consultancy",
    "ContentRefListResult",
    "ContentRefType0",
    "Contract",
    "ContractApplicationAssociation",
    "ContractAwardAssociation",
    "ContractCollaboratorAssociation",
    "ContractContractAssociation",
    "ContractCurtailed",
    "ContractDocument",
    "ContractDocumentFileStoreLocations",
    "ContractExtended",
    "ContractListResult",
    "ContractNegotiationAwardStatus",
    "ContractPriority",
    "ContractQuery",
    "ContractRefType0",
    "ContributionToBookAnthology",
    "ContributionToConference",
    "ContributionToJournal",
    "ContributionToMemorandum",
    "ContributionToPeriodical",
    "Course",
    "CourseFile",
    "CourseFileFileStoreLocations",
    "CourseListResult",
    "CourseOccurrence",
    "CourseRefType0",
    "CoursesQuery",
    "CurrencyAmount",
    "CurriculumVitaeRefType0",
    "CurtailedAwardStatus",
    "CustomDefinedFieldBooleanType0",
    "CustomDefinedFieldClassificationType0",
    "CustomDefinedFieldConfigurationRefType0",
    "CustomDefinedFieldDateType0",
    "CustomDefinedFieldDecimalType0",
    "CustomDefinedFieldIntegerType0",
    "CustomDefinedFieldStringType0",
    "CustomDefinedFieldType0",
    "CustomDefinedFieldsType0",
    "DataSet",
    "DataSetActivityAssociation",
    "DataSetAssociation",
    "DataSetAuthorCollaborationContributorAssociation",
    "DataSetAwardableAssociation",
    "DataSetDocument",
    "DataSetDocumentFileStoreLocations",
    "DataSetDoi",
    "DataSetEquipmentAssociation",
    "DataSetExternalContributorAssociation",
    "DataSetGeoLocation",
    "DataSetImpactAssociation",
    "DataSetInternalContributorAssociation",
    "DataSetLegalCondition",
    "DataSetListResult",
    "DataSetPhysicalData",
    "DataSetPressMediaAssociation",
    "DataSetPrizeAssociation",
    "DataSetProjectAssociation",
    "DataSetRefType0",
    "DataSetResearchOutputAssociation",
    "DataSetStudentThesisAssociation",
    "DataSetsQuery",
    "DateRange",
    "DeclinedAwardStatusType0",
    "DependencyViolationProblemDetails",
    "DeprecatedDateRange",
    "DeprecatedSystemCurrencyAmount",
    "DisciplinesAssociation",
    "DisciplinesAssociationListResult",
    "DisciplinesAssociationsQuery",
    "DisciplinesDiscipline",
    "DisciplinesDisciplineAssignment",
    "DisciplinesDisciplineListResult",
    "DisciplinesDisciplineScheme",
    "DisciplinesDisciplineSchemeListResult",
    "Document",
    "DocumentFileStoreLocations",
    "DoiElectronicVersion",
    "EditorialWork",
    "Education",
    "EducationAssociation",
    "EducationListResult",
    "EducationQuery",
    "EducationRefType0",
    "ElectronicISSN",
    "ElectronicVersionFile",
    "ElectronicVersionFileFileStoreLocations",
    "ElectronicVersionType0",
    "Equipment",
    "EquipmentAwardableAssociation",
    "EquipmentDataSetAssociation",
    "EquipmentDetails",
    "EquipmentImpactAssociation",
    "EquipmentListResult",
    "EquipmentPressMediaAssociation",
    "EquipmentPrizeAssociation",
    "EquipmentProjectAssociation",
    "EquipmentQuery",
    "EquipmentRefType0",
    "EthicalReview",
    "EthicalReviewApplicationAssociation",
    "EthicalReviewAwardAssociation",
    "EthicalReviewDocument",
    "EthicalReviewDocumentFileStoreLocations",
    "EthicalReviewEthicalReviewReply",
    "EthicalReviewListResult",
    "EthicalReviewQuery",
    "EthicalReviewRefType0",
    "Event",
    "EventListResult",
    "EventMembershipAssociation",
    "EventRefType0",
    "EventsQuery",
    "EvidenceContactInformation",
    "Examination",
    "ExtendedAwardStatus",
    "ExternalActivityPersonAssociation",
    "ExternalApplicantAssociation",
    "ExternalAppointment",
    "ExternalAwardHolderAssociation",
    "ExternalClassifiedContractPersonAssociation",
    "ExternalClassifiedCourseLecturerAssociation",
    "ExternalClassifiedEthicalReviewPersonAssociation",
    "ExternalCollaboratorAssociation",
    "ExternalContributorAssociation",
    "ExternalDataSetPersonAssociation",
    "ExternalEquipmentPersonAssociation",
    "ExternalExamineeAssociation",
    "ExternalFundingOpportunity",
    "ExternalImpactClassifiedParticipantAssociation",
    "ExternalOrganization",
    "ExternalOrganizationList",
    "ExternalOrganizationListResult",
    "ExternalOrganizationRefList",
    "ExternalOrganizationRefType0",
    "ExternalOrganizationsQuery",
    "ExternalParticipantAssociation",
    "ExternalPerson",
    "ExternalPersonListResult",
    "ExternalPersonRefType0",
    "ExternalPersonsQuery",
    "ExternalPressMediaPersonAssociation",
    "ExternalPrizeReceiverAssociation",
    "ExternalStudentThesisContributorAssociation",
    "FileElectronicVersion",
    "Fingerprint",
    "FingerprintListResult",
    "FingerprintQuery",
    "FingerprintRefType0",
    "FormattedLocalizedStringType0",
    "FormattedString",
    "FreeKeywordsKeywordGroup",
    "FullKeywordGroup",
    "FundingDetails",
    "FundingOpportunitiesQuery",
    "FundingOpportunity",
    "FundingOpportunityAcademicDegreeEligibility",
    "FundingOpportunityAcademicDegreeEligibilityEligibilityFulfilmentType",
    "FundingOpportunityContactEmail",
    "FundingOpportunityContactPerson",
    "FundingOpportunityDocument",
    "FundingOpportunityDocumentFileStoreLocations",
    "FundingOpportunityEligibility",
    "FundingOpportunityEligibilityEligibilityFulfilmentType",
    "FundingOpportunityListResult",
    "FundingOpportunityRefType0",
    "GenderType0",
    "GenderType0Key",
    "GenericContentRefType0",
    "GenericProblemDetails",
    "GeoLocationType0",
    "GlobalRoleAssignment",
    "HighlightedContent",
    "HonoraryStaffOrganizationAssociation",
    "HostVisitor",
    "ISSNRef",
    "Id",
    "Identifier",
    "ImageFile",
    "ImageFileFileStoreLocations",
    "Impact",
    "ImpactActivityAssociation",
    "ImpactAwardableAssociation",
    "ImpactDataSetAssociation",
    "ImpactEvidence",
    "ImpactImpactAssociation",
    "ImpactListResult",
    "ImpactPressMediaAssociation",
    "ImpactPrizeAssociation",
    "ImpactProjectAssociation",
    "ImpactQuery",
    "ImpactRefType0",
    "ImpactResearchOutputAssociation",
    "ImpactStudentThesisAssociation",
    "InternalActivityPersonAssociation",
    "InternalApplicantAssociation",
    "InternalAwardHolderAssociation",
    "InternalClassifiedContractPersonAssociation",
    "InternalClassifiedCourseLecturerAssociation",
    "InternalClassifiedEthicalReviewPersonAssociation",
    "InternalCollaboratorAssociation",
    "InternalContributorAssociation",
    "InternalDataSetPersonAssociation",
    "InternalEquipmentPersonAssociation",
    "InternalExamineeAssociation",
    "InternalFundingOpportunity",
    "InternalImpactClassifiedParticipantAssociation",
    "InternalOrExternalSupervisor",
    "InternalParticipantAssociation",
    "InternalPressMediaPersonAssociation",
    "InternalPrizeReceiverAssociation",
    "InternalStudentThesisContributorAssociation",
    "InternallyApprovedAwardStatus",
    "Journal",
    "JournalAssociationType0",
    "JournalEditorialWorkAssociation",
    "JournalListResult",
    "JournalRefType0",
    "JournalTitle",
    "JournalTitleRef",
    "JournalsQuery",
    "Keyword",
    "KeywordContainer",
    "KeywordGroup",
    "KeywordGroupConfiguration",
    "KeywordGroupConfigurationList",
    "KeywordGroupConfigurationRefType0",
    "KeywordGroupConfigurationSelectionModeSortingOrder",
    "KeywordGroupConfigurationUserdefinedKeywordEditMode",
    "Label",
    "Link",
    "LinkElectronicVersion",
    "LinkIdentifier",
    "LocalRoleAssignment",
    "LocalesList",
    "LocalizedStringType0",
    "MediaCoverage",
    "MediaCoverageCoverageType",
    "Membership",
    "Memorandum",
    "MetricCollection",
    "MetricCollectionDefinition",
    "MetricCollectionDefinitionList",
    "MetricCollectionItem",
    "MetricDefinition",
    "MetricValue",
    "Milestone",
    "MilestoneDocument",
    "MilestoneDocumentFileStoreLocations",
    "MilestoneListResult",
    "MilestoneMilestoneType",
    "MilestoneQuery",
    "MilestoneRefType0",
    "MilestoneReminder",
    "MilestoneReminderTimeUnit",
    "Name",
    "NonTextual",
    "Note",
    "NoteListResult",
    "OpenAccess",
    "OrderingsList",
    "Organization",
    "OrganizationListResult",
    "OrganizationOrExternalOrganizationRefType0",
    "OrganizationRefType0",
    "OrganizationsQuery",
    "OtherActivity",
    "OtherContribution",
    "PageInformation",
    "ParticipantTimeSpent",
    "ParticipantTimeTrackingAssociation",
    "Patent",
    "Person",
    "PersonClassifiedLeaveOfAbsence",
    "PersonExpertise",
    "PersonExpertiseListResult",
    "PersonExpertiseQuery",
    "PersonExpertiseRefType0",
    "PersonListResult",
    "PersonOrganizationAssociationType0",
    "PersonRefType0",
    "PersonSuperviseeAssociation",
    "PersonSuperviseeAssociationListResult",
    "PersonSupervisorAssociation",
    "PersonsQuery",
    "PressMedia",
    "PressMediaActivityAssociation",
    "PressMediaAwardableAssociation",
    "PressMediaDataSetAssociation",
    "PressMediaEquipmentAssociation",
    "PressMediaImpactAssociation",
    "PressMediaListResult",
    "PressMediaPressMediaAssociation",
    "PressMediaPrizeAssociation",
    "PressMediaProjectAssociation",
    "PressMediaQuery",
    "PressMediaRefType0",
    "PressMediaResearchOutputAssociation",
    "PressMediaStudentThesisAssociation",
    "PrimaryId",
    "Prize",
    "PrizeActivityAssociation",
    "PrizeAssociation",
    "PrizeAwardableAssociation",
    "PrizeDataSetAssociation",
    "PrizeEquipmentAssociation",
    "PrizeImpactAssociation",
    "PrizeListResult",
    "PrizePressMediaAssociation",
    "PrizeProjectAssociation",
    "PrizeRefType0",
    "PrizeResearchOutputAssociation",
    "PrizeStudentThesisAssociation",
    "PrizesQuery",
    "ProblemDetails",
    "ProfessionalQualification",
    "Project",
    "ProjectAssociation",
    "ProjectAwardableAssociationType0",
    "ProjectCurtailed",
    "ProjectListResult",
    "ProjectRefType0",
    "ProjectsQuery",
    "PublicationSeries",
    "PublicationStatus",
    "Publisher",
    "PublisherEditorialWorkAssociation",
    "PublisherListResult",
    "PublisherRefType0",
    "PublishersQuery",
    "RankedConcept",
    "Ref2014UnitOfAssessmentRefType0",
    "Ref2020UnitOfAssessmentRefType0",
    "RemoteFile",
    "RemoteFileFileState",
    "ResearchOutput",
    "ResearchOutputAssociationType0",
    "ResearchOutputAwardableAssociation",
    "ResearchOutputDataSetAssociationType0",
    "ResearchOutputImpactAssociationType0",
    "ResearchOutputListResult",
    "ResearchOutputPeerReviewConfiguration",
    "ResearchOutputPeerReviewConfigurationCombination",
    "ResearchOutputPeerReviewConfigurationCombinationPeerReviewable",
    "ResearchOutputPeerReviewConfigurationListResult",
    "ResearchOutputPressMediaAssociationType0",
    "ResearchOutputPrizeAssociationType0",
    "ResearchOutputRefType0",
    "ResearchOutputStudentThesisAssociationType0",
    "ResearchOutputsQuery",
    "ResearcherCommitment",
    "ReviewRefType0",
    "Semester",
    "SemesterListResult",
    "SemesterQuery",
    "SemesterRefType0",
    "SherpaRomeoOpenAccessPermissionType0",
    "SherpaRomeoPolicy",
    "Specialization",
    "SpecializationListResult",
    "SpecializationQuery",
    "SpecializationRefType0",
    "StaffOrganizationAssociation",
    "StudentOrganizationAssociation",
    "StudentOrganizationAssociationStudentResidencyFlag",
    "StudentProject",
    "StudentProjectAppendixDocument",
    "StudentProjectAppendixDocumentFileStoreLocations",
    "StudentProjectAuthor",
    "StudentProjectDocument",
    "StudentProjectDocumentFileStoreLocations",
    "StudentProjectExternalCollaborator",
    "StudentProjectListResult",
    "StudentProjectNotificationRecipient",
    "StudentProjectQuery",
    "StudentProjectRefType0",
    "StudentProjectSupervisor",
    "StudentThesesQuery",
    "StudentThesis",
    "StudentThesisAwardableAssociation",
    "StudentThesisDocument",
    "StudentThesisDocumentFileStoreLocations",
    "StudentThesisListResult",
    "StudentThesisRefType0",
    "SupervisorAssociation",
    "SystemCurrencyAmount",
    "SystemLocalizedStringType0",
    "Talk",
    "Term",
    "TerminatedAwardStatus",
    "Thesaurus",
    "ThesaurusListResult",
    "ThesaurusQuery",
    "ThesaurusRefType0",
    "Thesis",
    "UploadedFile",
    "User",
    "UserListResult",
    "UserProfileRefType0",
    "UserRefType0",
    "UserRoles",
    "ValidationError",
    "ValidationProblemDetails",
    "Visibility",
    "VisibilityKey",
    "VisitOther",
    "VisitingScholarOrganizationAssociation",
    "Workflow",
    "WorkflowListResult",
    "WorkingPaper",
    "YearMonthType0",
    "YearlyBudget",
)
