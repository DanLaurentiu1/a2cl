import pytest

from app.core.domain import Profile
from app.core.validation import plan_validator
from app.api.schemas.schemas import TopicTypes
from app.core.domain import Plan, Problem, Topic


@pytest.fixture
def plan_valid():
    return Plan(id=1, title="test", profile=Profile(name="test"), problems=[[0, Problem(id=1, name="test", topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)], difficulty=1, acceptanceRate=55.1)]])

@pytest.fixture
def plan_empty_title_not_string():
    return Plan(id=1, title=123, profile=Profile(name="test"), problems=[[0, Problem(id=1, name="test", topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)], difficulty=1, acceptanceRate=55.1)]])

@pytest.fixture
def plan_title_length_over_cap():
    return Plan(id=1, title="testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest", profile=Profile(name="test"), problems=[[0, Problem(id=1, name="test", topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)], difficulty=1, acceptanceRate=55.1)]])

@pytest.fixture
def plan_title_with_special_characters():
    return Plan(id=1, title="test!!", profile=Profile(name="test"), problems=[[0, Problem(id=1, name="test", topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)], difficulty=1, acceptanceRate=55.1)]])

def test_validate_plan_valid(plan_valid):
    assert plan_validator.validate_plan(plan_valid) is None

def test_validate_plan_invalid_title(plan_empty_title_not_string):
    with pytest.raises(ValueError) as e:
        plan_validator.validate_plan(plan_empty_title_not_string)
    assert str(e.value) == "Title must be a string"

def test_validate_plan_invalid_title_over_cap(plan_title_length_over_cap):
    with pytest.raises(ValueError) as e:
        plan_validator.validate_plan(plan_title_length_over_cap)
    assert str(e.value) == "Plan title must be <= 100 characters"

def test_validate_plan_title_has_special_characters(plan_title_with_special_characters):
    with pytest.raises(ValueError) as e:
        plan_validator.validate_plan(plan_title_with_special_characters)
    assert str(e.value) == "Title contains invalid characters"