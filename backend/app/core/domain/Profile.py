from typing import Dict

from app.api.schemas.schemas import ProfileJSON
from app.core.data.topics import ALL_TOPICS
from app.core.domain import Topic


class Profile:
    def __init__(self, name: str):
        self._name = name
        self._proficiencies: Dict[Topic, int] = self._create_default_proficiencies()

    @property
    def name(self) -> str:
        return self._name

    @property
    def proficiencies(self) -> Dict[Topic, int]:
        return self._proficiencies

    def to_json(self) -> ProfileJSON:
        return ProfileJSON(
            name=self._name,
            proficiencies=[
                (topic.to_json(), value) for topic, value in self._proficiencies.items()
            ],
        )

    @classmethod
    def from_json(self, json: ProfileJSON) -> "Profile":
        if not json.name:
            raise ValueError("Invalid Profile JSON")

        profile = self(json.name)

        if json.proficiencies:
            profile._proficiencies = {
                Topic.from_json(topic_json): value
                for topic_json, value in json.proficiencies
            }

        return profile

    def _create_default_proficiencies(self) -> Dict[Topic, int]:
        return {topic: 0 for topic in ALL_TOPICS}
