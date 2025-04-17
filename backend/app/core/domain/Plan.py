from typing import List, Set, Tuple

from app.api.schemas.schemas import PlanJSON
from app.core.domain import Problem, Profile, Topic


class Plan:
    def __init__(
        self,
        id: int,
        title: str,
        profile: Profile,
        problems: List[Tuple[bool, Problem]] = []
    ):
        self._id = id
        self._title = title
        self._profile = profile
        self._problems = problems
        self._topics = self._calculate_topics()

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def profile(self) -> Profile:
        return self._profile

    @property
    def problems(self) -> List[Tuple[bool, Problem]]:
        return self._problems.copy()

    @property
    def topics(self) -> Set[Topic]:
        return self._topics.copy()

    def get_problem_by_id(self, problem_id: int) -> Tuple[bool, Problem]:
        problem = next(
            (p for p in self._problems if p[1].id == problem_id),
            None
        )
        if problem is None:
            raise ValueError(f"Problem {problem_id} not found in plan")
        return problem

    def toggle_problem_completion(self, problem_id: int):
        for i, (completed, problem) in enumerate(self._problems):
            if problem.id == problem_id:
                self._problems[i] = (not completed, problem)
                return
        raise ValueError(f"Problem {problem_id} not found in plan")

    def get_percentage_completed(self) -> float:
        if not self._problems:
            return 100.0
        completed = sum(1 for done, _ in self._problems if done)
        return round((completed / len(self._problems)) * 100)

    def to_json(self) -> PlanJSON:
        return PlanJSON(
            id=self._id,
            title=self._title,
            profile=self._profile.to_json(),
            problems=[(done, prob.to_json()) for done, prob in self._problems],
            topics=[t.to_json() for t in self._topics] if self._topics else None
        )

    @classmethod
    def from_json(self, json_data: PlanJSON) -> 'Plan':
        try:
            if not json_data.id or not json_data.title or not json_data.profile:
                raise ValueError("Invalid Plan JSON - missing required fields")
            problems = [
                (bool(done), Problem.from_json(prob))
                for done, prob in json_data.problems
            ]
            plan = self(
                id=json_data.id,
                title=json_data.title,
                profile=Profile.from_json(json_data.profile),
                problems=problems
            )
            if json_data.topics:
                plan._topics = {Topic.from_json(t) for t in json_data.topics}
            return plan
        except Exception as e:
            raise ValueError(f"Invalid Plan JSON")
    
    def _calculate_topics(self) -> Set[Topic]:
        topics = set()
        for _, problem in self._problems:
            for topic in problem.topics:
                topics.add(topic)
        return topics