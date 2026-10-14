from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_ref_type_0 import ActivityRefType0
    from ..models.application_ref_type_0 import ApplicationRefType0
    from ..models.award_ref_type_0 import AwardRefType0
    from ..models.course_ref_type_0 import CourseRefType0
    from ..models.curriculum_vitae_ref_type_0 import CurriculumVitaeRefType0
    from ..models.data_set_ref_type_0 import DataSetRefType0
    from ..models.equipment_ref_type_0 import EquipmentRefType0
    from ..models.impact_ref_type_0 import ImpactRefType0
    from ..models.press_media_ref_type_0 import PressMediaRefType0
    from ..models.prize_ref_type_0 import PrizeRefType0
    from ..models.project_ref_type_0 import ProjectRefType0
    from ..models.research_output_ref_type_0 import ResearchOutputRefType0
    from ..models.student_thesis_ref_type_0 import StudentThesisRefType0


T = TypeVar("T", bound="HighlightedContent")


@_attrs_define
class HighlightedContent:
    """A person's highlighted content

    Attributes:
        courses (list[CourseRefType0 | None] | None | Unset): References to highlighted courses.
        curricula_vitae (list[CurriculumVitaeRefType0 | None] | None | Unset): References to highlighted curricula
            vitae.
        research_outputs (list[None | ResearchOutputRefType0] | None | Unset): References to highlighted research
            outputs.
        activities (list[ActivityRefType0 | None] | None | Unset): References to highlighted activities.
        applications (list[ApplicationRefType0 | None] | None | Unset): References to highlighted applications.
        awards (list[AwardRefType0 | None] | None | Unset): References to highlighted awards.
        prizes (list[None | PrizeRefType0] | None | Unset): References to highlighted prizes.
        projects (list[None | ProjectRefType0] | None | Unset): References to highlighted projects.
        press_media (list[None | PressMediaRefType0] | None | Unset): References to highlighted press media.
        impacts (list[ImpactRefType0 | None] | None | Unset): References to highlighted impacts.
        datasets (list[DataSetRefType0 | None] | None | Unset): References to highlighted datasets.
        student_theses (list[None | StudentThesisRefType0] | None | Unset): References to highlighted student theses.
        equipment (list[EquipmentRefType0 | None] | None | Unset): References to highlighted equipment.
    """

    courses: list[CourseRefType0 | None] | None | Unset = UNSET
    curricula_vitae: list[CurriculumVitaeRefType0 | None] | None | Unset = UNSET
    research_outputs: list[None | ResearchOutputRefType0] | None | Unset = UNSET
    activities: list[ActivityRefType0 | None] | None | Unset = UNSET
    applications: list[ApplicationRefType0 | None] | None | Unset = UNSET
    awards: list[AwardRefType0 | None] | None | Unset = UNSET
    prizes: list[None | PrizeRefType0] | None | Unset = UNSET
    projects: list[None | ProjectRefType0] | None | Unset = UNSET
    press_media: list[None | PressMediaRefType0] | None | Unset = UNSET
    impacts: list[ImpactRefType0 | None] | None | Unset = UNSET
    datasets: list[DataSetRefType0 | None] | None | Unset = UNSET
    student_theses: list[None | StudentThesisRefType0] | None | Unset = UNSET
    equipment: list[EquipmentRefType0 | None] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.course_ref_type_0 import CourseRefType0
        from ..models.curriculum_vitae_ref_type_0 import CurriculumVitaeRefType0
        from ..models.data_set_ref_type_0 import DataSetRefType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.press_media_ref_type_0 import PressMediaRefType0
        from ..models.prize_ref_type_0 import PrizeRefType0
        from ..models.project_ref_type_0 import ProjectRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0

        courses: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.courses, Unset):
            courses = UNSET
        elif isinstance(self.courses, list):
            courses = []
            for courses_type_0_item_data in self.courses:
                courses_type_0_item: dict[str, Any] | None
                if isinstance(courses_type_0_item_data, CourseRefType0):
                    courses_type_0_item = courses_type_0_item_data.to_dict()
                else:
                    courses_type_0_item = courses_type_0_item_data
                courses.append(courses_type_0_item)

        else:
            courses = self.courses

        curricula_vitae: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.curricula_vitae, Unset):
            curricula_vitae = UNSET
        elif isinstance(self.curricula_vitae, list):
            curricula_vitae = []
            for curricula_vitae_type_0_item_data in self.curricula_vitae:
                curricula_vitae_type_0_item: dict[str, Any] | None
                if isinstance(
                    curricula_vitae_type_0_item_data, CurriculumVitaeRefType0
                ):
                    curricula_vitae_type_0_item = (
                        curricula_vitae_type_0_item_data.to_dict()
                    )
                else:
                    curricula_vitae_type_0_item = curricula_vitae_type_0_item_data
                curricula_vitae.append(curricula_vitae_type_0_item)

        else:
            curricula_vitae = self.curricula_vitae

        research_outputs: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.research_outputs, Unset):
            research_outputs = UNSET
        elif isinstance(self.research_outputs, list):
            research_outputs = []
            for research_outputs_type_0_item_data in self.research_outputs:
                research_outputs_type_0_item: dict[str, Any] | None
                if isinstance(
                    research_outputs_type_0_item_data, ResearchOutputRefType0
                ):
                    research_outputs_type_0_item = (
                        research_outputs_type_0_item_data.to_dict()
                    )
                else:
                    research_outputs_type_0_item = research_outputs_type_0_item_data
                research_outputs.append(research_outputs_type_0_item)

        else:
            research_outputs = self.research_outputs

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

        applications: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.applications, Unset):
            applications = UNSET
        elif isinstance(self.applications, list):
            applications = []
            for applications_type_0_item_data in self.applications:
                applications_type_0_item: dict[str, Any] | None
                if isinstance(applications_type_0_item_data, ApplicationRefType0):
                    applications_type_0_item = applications_type_0_item_data.to_dict()
                else:
                    applications_type_0_item = applications_type_0_item_data
                applications.append(applications_type_0_item)

        else:
            applications = self.applications

        awards: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.awards, Unset):
            awards = UNSET
        elif isinstance(self.awards, list):
            awards = []
            for awards_type_0_item_data in self.awards:
                awards_type_0_item: dict[str, Any] | None
                if isinstance(awards_type_0_item_data, AwardRefType0):
                    awards_type_0_item = awards_type_0_item_data.to_dict()
                else:
                    awards_type_0_item = awards_type_0_item_data
                awards.append(awards_type_0_item)

        else:
            awards = self.awards

        prizes: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.prizes, Unset):
            prizes = UNSET
        elif isinstance(self.prizes, list):
            prizes = []
            for prizes_type_0_item_data in self.prizes:
                prizes_type_0_item: dict[str, Any] | None
                if isinstance(prizes_type_0_item_data, PrizeRefType0):
                    prizes_type_0_item = prizes_type_0_item_data.to_dict()
                else:
                    prizes_type_0_item = prizes_type_0_item_data
                prizes.append(prizes_type_0_item)

        else:
            prizes = self.prizes

        projects: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item: dict[str, Any] | None
                if isinstance(projects_type_0_item_data, ProjectRefType0):
                    projects_type_0_item = projects_type_0_item_data.to_dict()
                else:
                    projects_type_0_item = projects_type_0_item_data
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        press_media: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.press_media, Unset):
            press_media = UNSET
        elif isinstance(self.press_media, list):
            press_media = []
            for press_media_type_0_item_data in self.press_media:
                press_media_type_0_item: dict[str, Any] | None
                if isinstance(press_media_type_0_item_data, PressMediaRefType0):
                    press_media_type_0_item = press_media_type_0_item_data.to_dict()
                else:
                    press_media_type_0_item = press_media_type_0_item_data
                press_media.append(press_media_type_0_item)

        else:
            press_media = self.press_media

        impacts: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.impacts, Unset):
            impacts = UNSET
        elif isinstance(self.impacts, list):
            impacts = []
            for impacts_type_0_item_data in self.impacts:
                impacts_type_0_item: dict[str, Any] | None
                if isinstance(impacts_type_0_item_data, ImpactRefType0):
                    impacts_type_0_item = impacts_type_0_item_data.to_dict()
                else:
                    impacts_type_0_item = impacts_type_0_item_data
                impacts.append(impacts_type_0_item)

        else:
            impacts = self.impacts

        datasets: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.datasets, Unset):
            datasets = UNSET
        elif isinstance(self.datasets, list):
            datasets = []
            for datasets_type_0_item_data in self.datasets:
                datasets_type_0_item: dict[str, Any] | None
                if isinstance(datasets_type_0_item_data, DataSetRefType0):
                    datasets_type_0_item = datasets_type_0_item_data.to_dict()
                else:
                    datasets_type_0_item = datasets_type_0_item_data
                datasets.append(datasets_type_0_item)

        else:
            datasets = self.datasets

        student_theses: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.student_theses, Unset):
            student_theses = UNSET
        elif isinstance(self.student_theses, list):
            student_theses = []
            for student_theses_type_0_item_data in self.student_theses:
                student_theses_type_0_item: dict[str, Any] | None
                if isinstance(student_theses_type_0_item_data, StudentThesisRefType0):
                    student_theses_type_0_item = (
                        student_theses_type_0_item_data.to_dict()
                    )
                else:
                    student_theses_type_0_item = student_theses_type_0_item_data
                student_theses.append(student_theses_type_0_item)

        else:
            student_theses = self.student_theses

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if courses is not UNSET:
            field_dict["courses"] = courses
        if curricula_vitae is not UNSET:
            field_dict["curriculaVitae"] = curricula_vitae
        if research_outputs is not UNSET:
            field_dict["researchOutputs"] = research_outputs
        if activities is not UNSET:
            field_dict["activities"] = activities
        if applications is not UNSET:
            field_dict["applications"] = applications
        if awards is not UNSET:
            field_dict["awards"] = awards
        if prizes is not UNSET:
            field_dict["prizes"] = prizes
        if projects is not UNSET:
            field_dict["projects"] = projects
        if press_media is not UNSET:
            field_dict["pressMedia"] = press_media
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if datasets is not UNSET:
            field_dict["datasets"] = datasets
        if student_theses is not UNSET:
            field_dict["studentTheses"] = student_theses
        if equipment is not UNSET:
            field_dict["equipment"] = equipment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.activity_ref_type_0 import ActivityRefType0
        from ..models.application_ref_type_0 import ApplicationRefType0
        from ..models.award_ref_type_0 import AwardRefType0
        from ..models.course_ref_type_0 import CourseRefType0
        from ..models.curriculum_vitae_ref_type_0 import CurriculumVitaeRefType0
        from ..models.data_set_ref_type_0 import DataSetRefType0
        from ..models.equipment_ref_type_0 import EquipmentRefType0
        from ..models.impact_ref_type_0 import ImpactRefType0
        from ..models.press_media_ref_type_0 import PressMediaRefType0
        from ..models.prize_ref_type_0 import PrizeRefType0
        from ..models.project_ref_type_0 import ProjectRefType0
        from ..models.research_output_ref_type_0 import ResearchOutputRefType0
        from ..models.student_thesis_ref_type_0 import StudentThesisRefType0

        d = dict(src_dict)

        def _parse_courses(data: object) -> list[CourseRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                courses_type_0 = []
                _courses_type_0 = data
                for courses_type_0_item_data in _courses_type_0:

                    def _parse_courses_type_0_item(
                        data: object,
                    ) -> CourseRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_course_ref_type_0 = (
                                CourseRefType0.from_dict(data)
                            )

                            return componentsschemas_course_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(CourseRefType0 | None, data)

                    courses_type_0_item = _parse_courses_type_0_item(
                        courses_type_0_item_data
                    )

                    courses_type_0.append(courses_type_0_item)

                return courses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CourseRefType0 | None] | None | Unset, data)

        courses = _parse_courses(d.pop("courses", UNSET))

        def _parse_curricula_vitae(
            data: object,
        ) -> list[CurriculumVitaeRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                curricula_vitae_type_0 = []
                _curricula_vitae_type_0 = data
                for curricula_vitae_type_0_item_data in _curricula_vitae_type_0:

                    def _parse_curricula_vitae_type_0_item(
                        data: object,
                    ) -> CurriculumVitaeRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_curriculum_vitae_ref_type_0 = (
                                CurriculumVitaeRefType0.from_dict(data)
                            )

                            return componentsschemas_curriculum_vitae_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(CurriculumVitaeRefType0 | None, data)

                    curricula_vitae_type_0_item = _parse_curricula_vitae_type_0_item(
                        curricula_vitae_type_0_item_data
                    )

                    curricula_vitae_type_0.append(curricula_vitae_type_0_item)

                return curricula_vitae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CurriculumVitaeRefType0 | None] | None | Unset, data)

        curricula_vitae = _parse_curricula_vitae(d.pop("curriculaVitae", UNSET))

        def _parse_research_outputs(
            data: object,
        ) -> list[None | ResearchOutputRefType0] | None | Unset:
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
                    ) -> None | ResearchOutputRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_research_output_ref_type_0 = (
                                ResearchOutputRefType0.from_dict(data)
                            )

                            return componentsschemas_research_output_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ResearchOutputRefType0, data)

                    research_outputs_type_0_item = _parse_research_outputs_type_0_item(
                        research_outputs_type_0_item_data
                    )

                    research_outputs_type_0.append(research_outputs_type_0_item)

                return research_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | ResearchOutputRefType0] | None | Unset, data)

        research_outputs = _parse_research_outputs(d.pop("researchOutputs", UNSET))

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

        def _parse_applications(
            data: object,
        ) -> list[ApplicationRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applications_type_0 = []
                _applications_type_0 = data
                for applications_type_0_item_data in _applications_type_0:

                    def _parse_applications_type_0_item(
                        data: object,
                    ) -> ApplicationRefType0 | None:
                        if data is None:
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
                        return cast(ApplicationRefType0 | None, data)

                    applications_type_0_item = _parse_applications_type_0_item(
                        applications_type_0_item_data
                    )

                    applications_type_0.append(applications_type_0_item)

                return applications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplicationRefType0 | None] | None | Unset, data)

        applications = _parse_applications(d.pop("applications", UNSET))

        def _parse_awards(data: object) -> list[AwardRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                awards_type_0 = []
                _awards_type_0 = data
                for awards_type_0_item_data in _awards_type_0:

                    def _parse_awards_type_0_item(data: object) -> AwardRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_award_ref_type_0 = (
                                AwardRefType0.from_dict(data)
                            )

                            return componentsschemas_award_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(AwardRefType0 | None, data)

                    awards_type_0_item = _parse_awards_type_0_item(
                        awards_type_0_item_data
                    )

                    awards_type_0.append(awards_type_0_item)

                return awards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AwardRefType0 | None] | None | Unset, data)

        awards = _parse_awards(d.pop("awards", UNSET))

        def _parse_prizes(data: object) -> list[None | PrizeRefType0] | None | Unset:
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

                    def _parse_prizes_type_0_item(data: object) -> None | PrizeRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_prize_ref_type_0 = (
                                PrizeRefType0.from_dict(data)
                            )

                            return componentsschemas_prize_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | PrizeRefType0, data)

                    prizes_type_0_item = _parse_prizes_type_0_item(
                        prizes_type_0_item_data
                    )

                    prizes_type_0.append(prizes_type_0_item)

                return prizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | PrizeRefType0] | None | Unset, data)

        prizes = _parse_prizes(d.pop("prizes", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[None | ProjectRefType0] | None | Unset:
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
                    ) -> None | ProjectRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_project_ref_type_0 = (
                                ProjectRefType0.from_dict(data)
                            )

                            return componentsschemas_project_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | ProjectRefType0, data)

                    projects_type_0_item = _parse_projects_type_0_item(
                        projects_type_0_item_data
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | ProjectRefType0] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_press_media(
            data: object,
        ) -> list[None | PressMediaRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                press_media_type_0 = []
                _press_media_type_0 = data
                for press_media_type_0_item_data in _press_media_type_0:

                    def _parse_press_media_type_0_item(
                        data: object,
                    ) -> None | PressMediaRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_press_media_ref_type_0 = (
                                PressMediaRefType0.from_dict(data)
                            )

                            return componentsschemas_press_media_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | PressMediaRefType0, data)

                    press_media_type_0_item = _parse_press_media_type_0_item(
                        press_media_type_0_item_data
                    )

                    press_media_type_0.append(press_media_type_0_item)

                return press_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | PressMediaRefType0] | None | Unset, data)

        press_media = _parse_press_media(d.pop("pressMedia", UNSET))

        def _parse_impacts(data: object) -> list[ImpactRefType0 | None] | None | Unset:
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
                    ) -> ImpactRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_impact_ref_type_0 = (
                                ImpactRefType0.from_dict(data)
                            )

                            return componentsschemas_impact_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ImpactRefType0 | None, data)

                    impacts_type_0_item = _parse_impacts_type_0_item(
                        impacts_type_0_item_data
                    )

                    impacts_type_0.append(impacts_type_0_item)

                return impacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImpactRefType0 | None] | None | Unset, data)

        impacts = _parse_impacts(d.pop("impacts", UNSET))

        def _parse_datasets(
            data: object,
        ) -> list[DataSetRefType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                datasets_type_0 = []
                _datasets_type_0 = data
                for datasets_type_0_item_data in _datasets_type_0:

                    def _parse_datasets_type_0_item(
                        data: object,
                    ) -> DataSetRefType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_data_set_ref_type_0 = (
                                DataSetRefType0.from_dict(data)
                            )

                            return componentsschemas_data_set_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(DataSetRefType0 | None, data)

                    datasets_type_0_item = _parse_datasets_type_0_item(
                        datasets_type_0_item_data
                    )

                    datasets_type_0.append(datasets_type_0_item)

                return datasets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataSetRefType0 | None] | None | Unset, data)

        datasets = _parse_datasets(d.pop("datasets", UNSET))

        def _parse_student_theses(
            data: object,
        ) -> list[None | StudentThesisRefType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                student_theses_type_0 = []
                _student_theses_type_0 = data
                for student_theses_type_0_item_data in _student_theses_type_0:

                    def _parse_student_theses_type_0_item(
                        data: object,
                    ) -> None | StudentThesisRefType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_student_thesis_ref_type_0 = (
                                StudentThesisRefType0.from_dict(data)
                            )

                            return componentsschemas_student_thesis_ref_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | StudentThesisRefType0, data)

                    student_theses_type_0_item = _parse_student_theses_type_0_item(
                        student_theses_type_0_item_data
                    )

                    student_theses_type_0.append(student_theses_type_0_item)

                return student_theses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | StudentThesisRefType0] | None | Unset, data)

        student_theses = _parse_student_theses(d.pop("studentTheses", UNSET))

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

        highlighted_content = cls(
            courses=courses,
            curricula_vitae=curricula_vitae,
            research_outputs=research_outputs,
            activities=activities,
            applications=applications,
            awards=awards,
            prizes=prizes,
            projects=projects,
            press_media=press_media,
            impacts=impacts,
            datasets=datasets,
            student_theses=student_theses,
            equipment=equipment,
        )

        highlighted_content.additional_properties = d
        return highlighted_content

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
