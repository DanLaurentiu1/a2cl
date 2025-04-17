from app.api.schemas.schemas import TopicJSON, TopicTypes

class Topic:
    def __init__(self, name: str, topic_type: TopicTypes):
        self._name = name
        self._type = topic_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> TopicTypes:
        return self._type

    def to_json(self) -> TopicJSON:
        return TopicJSON(
            name=self._name,
            type=self._type.value,
        )

    @classmethod
    def from_json(self, json: TopicJSON) -> 'Topic':
        if not json.name or not json.type:
            raise ValueError("Invalid Topic JSON")
        return self(json.name, TopicTypes(json.type))