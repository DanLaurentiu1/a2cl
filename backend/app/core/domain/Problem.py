from dataclasses import dataclass
from typing import List
from app.api.schemas.schemas import DifficultyLevel, ProblemJSON
from app.core.domain import Topic

@dataclass
class Problem:
    def __init__(
        self,
        id: int,
        name: str,
        topics: List[Topic],
        difficulty: DifficultyLevel,
        acceptance_rate: float
    ):
        self._id = id
        self._name = name
        self._topics = topics
        self._difficulty = difficulty
        self._acceptanceRate = acceptance_rate

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def topics(self) -> List[Topic]:
        return self._topics.copy()

    @property
    def difficulty(self) -> DifficultyLevel:
        return self._difficulty

    @property
    def acceptanceRate(self) -> float:
        return self._acceptanceRate

    def to_json(self) -> ProblemJSON:
        return ProblemJSON(
            id=self._id,
            name=self._name,
            topics=[topic.to_json() for topic in self._topics],
            difficulty=self._difficulty,
            acceptanceRate=self._acceptanceRate
        )

    @classmethod
    def from_json(self, json: ProblemJSON) -> 'Problem':
        if not json.id or not json.name:
            raise ValueError("Invalid Problem JSON")
        return self(
            id=json.id,
            name=json.name,
            topics=[Topic.from_json(topic) for topic in json.topics],
            difficulty=json.difficulty,
            acceptance_rate=json.acceptanceRate
        ) 