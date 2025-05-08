import pytest
from app.core.domain import Problem
from app.core.domain import Topic
from app.api.schemas.schemas import ProblemJSON, TopicTypes

@pytest.fixture
def sample_problem_valid():
    return Problem(id=1, name="test", topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)], difficulty=1, acceptance_rate=55.1)

@pytest.fixture
def sample_problem_invalid():
    return Problem(id=1, name="", topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)], difficulty=1, acceptance_rate=55.1)

def test_problem_object_creation(sample_problem_valid):
    assert sample_problem_valid is not None

def test_problem_name_valid(sample_problem_valid):
    assert sample_problem_valid.name == "test"

def test_problem_id_valid(sample_problem_valid):
    assert sample_problem_valid.id == 1

def test_problem_topics_valid(sample_problem_valid):
    assert isinstance(sample_problem_valid.topics[0], Topic)    

def test_problem_difficulty_valid(sample_problem_valid):
    assert sample_problem_valid.difficulty == 1

def test_problem_acceptance_rate_valid(sample_problem_valid):
    assert sample_problem_valid.acceptanceRate == 55.1

def test_problem_to_json_valid(sample_problem_valid):
    json_object = sample_problem_valid.to_json()
    assert isinstance(json_object, ProblemJSON)
    assert json_object.id == 1
    assert json_object.name == "test"
    assert json_object.acceptanceRate == 55.1
    assert json_object.difficulty == 1

def test_problem_from_json_valid(sample_problem_valid):
    json_object = sample_problem_valid.to_json()
    problem_new = Problem.from_json(json_object)
    assert isinstance(problem_new, Problem)
    assert problem_new.id == sample_problem_valid.id
    assert problem_new.name == sample_problem_valid.name
    assert problem_new.acceptanceRate == sample_problem_valid.acceptanceRate
    assert problem_new.difficulty == sample_problem_valid.difficulty
    assert problem_new.topics[0].name == sample_problem_valid.topics[0].name
    assert problem_new.topics[0].type == sample_problem_valid.topics[0].type


def test_problem_from_json_invalid(sample_problem_invalid):
    json_object = sample_problem_invalid.to_json()
    with pytest.raises(ValueError) as e:
        Problem.from_json(json_object)
    assert str(e.value) == "Invalid Problem JSON"