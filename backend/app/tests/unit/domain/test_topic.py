from app.api.schemas.schemas import TopicJSON, TopicTypes
from app.core.domain.Topic import Topic
import pytest

@pytest.fixture
def sample_topic_valid():
    return Topic(name="test", topic_type=TopicTypes.CONCEPTS)

@pytest.fixture
def sample_topic_invalid():
    return Topic(name="", topic_type=TopicTypes.CONCEPTS)

def test_topic_object_creation(sample_topic_valid):
    assert sample_topic_valid is not None

def test_topic_name_creation_valid(sample_topic_valid):
    assert sample_topic_valid.name == "test"

def test_topic_type_creation_valid(sample_topic_valid):
    assert sample_topic_valid.type == TopicTypes.CONCEPTS

def test_topic_to_json_valid(sample_topic_valid):
    json_object = sample_topic_valid.to_json()
    assert isinstance(json_object, TopicJSON)
    assert json_object.name == "test"
    assert json_object.type == TopicTypes.CONCEPTS

def test_topic_from_json_valid(sample_topic_valid):
    json_object = sample_topic_valid.to_json()
    topic_new = Topic.from_json(json_object)
    assert isinstance(topic_new, Topic)
    assert topic_new.name == sample_topic_valid.name
    assert topic_new.type == sample_topic_valid.type

def test_topic_from_json_invalid(sample_topic_invalid):
    json_object = sample_topic_invalid.to_json()
    with pytest.raises(ValueError) as e:
        Topic.from_json(json_object)
    assert str(e.value == "Invalid Topic JSON")