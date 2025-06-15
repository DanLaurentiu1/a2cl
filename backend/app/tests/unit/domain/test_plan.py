import pytest

from app.core.domain import Plan
from app.core.domain import Profile
from app.api.schemas.schemas import PlanJSON, TopicTypes
from app.core.domain import Problem, Topic


@pytest.fixture
def sample_plan_no_problems() -> Plan:
    return Plan(id=1, title="test", profile=Profile(name="test"), problems=[])


@pytest.fixture
def sample_plan_valid() -> Plan:
    return Plan(
        id=1,
        title="test",
        profile=Profile(name="test"),
        problems=[
            [
                0,
                Problem(
                    id=1,
                    name="test",
                    topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)],
                    difficulty=1,
                    acceptance_rate=55.1,
                ),
            ]
        ],
    )


@pytest.fixture
def sample_plan_invalid() -> Plan:
    return Plan(
        id=1,
        title="",
        profile=Profile(name="test"),
        problems=[
            [
                0,
                Problem(
                    id=1,
                    name="test",
                    topics=[Topic(name="test", topic_type=TopicTypes.CONCEPTS)],
                    difficulty=1,
                    acceptance_rate=55.1,
                ),
            ]
        ],
    )


def test_plan_object_creation(sample_plan_valid: Plan):
    assert sample_plan_valid is not None


def test_plan_id_valid(sample_plan_valid: Plan):
    assert sample_plan_valid.id == 1


def test_plan_title_valid(sample_plan_valid: Plan):
    assert sample_plan_valid.title == "test"


def test_plan_title_setter_valid(sample_plan_valid: Plan):
    plan = sample_plan_valid
    plan.title = "newTitle"
    assert plan.title == "newTitle"


def test_plan_title_setter_invalid(sample_plan_valid: Plan):
    plan = sample_plan_valid
    with pytest.raises(ValueError) as e:
        plan.title = 123
    assert str(e.value) == "Title must be a non-empty string"


def test_plan_profile_valid(sample_plan_valid: Plan):
    assert sample_plan_valid.profile.name == "test"


def test_plan_problems_valid(sample_plan_valid: Plan):
    assert len(sample_plan_valid.problems) == 1
    assert isinstance(sample_plan_valid.problems[0][0], int)
    assert isinstance(sample_plan_valid.problems[0][1], Problem)


def test_plan_topics_valid(sample_plan_valid: Plan):
    assert isinstance(sample_plan_valid.topics, set)


def test_plan_get_problem_by_id_valid(sample_plan_valid: Plan):
    assert isinstance(sample_plan_valid.get_problem_by_id(1)[1], Problem)


def test_plan_get_problem_by_id_invalid(sample_plan_valid: Plan):
    with pytest.raises(ValueError) as e:
        sample_plan_valid.get_problem_by_id(2)
    assert str(e.value) == "Problem 2 not found in plan"


def test_plan_toggle_problem_completion_valid(sample_plan_valid: Plan):
    plan = sample_plan_valid
    plan.toggle_problem_completion(1)
    assert plan.problems[0][0] == 1


def test_plan_toggle_problem_completion_invalid(sample_plan_valid: Plan):
    with pytest.raises(ValueError) as e:
        plan = sample_plan_valid
        plan.toggle_problem_completion(2)
    assert str(e.value) == "Problem 2 not found in plan"


def test_plan_get_percentage_completed_valid(sample_plan_valid: Plan):
    assert sample_plan_valid.get_percentage_completed() == 0.0


def test_plan_get_percentage_completed_no_problems_valid(sample_plan_no_problems: Plan):
    assert sample_plan_no_problems.get_percentage_completed() == 100.0


def test_plan_to_json_valid(sample_plan_valid: Plan):
    json_object = sample_plan_valid.to_json()
    assert isinstance(json_object, PlanJSON)
    assert json_object.title == "test"


def test_plan_from_json_valid(sample_plan_valid: Plan):
    json_object = sample_plan_valid.to_json()
    plan_new = Plan.from_json(json_object)
    assert isinstance(plan_new, Plan)
    assert plan_new.title == sample_plan_valid.title


def test_plan_from_json_invalid(sample_plan_invalid: Plan):
    json_object = sample_plan_invalid.to_json()
    with pytest.raises(ValueError) as e:
        Plan.from_json(json_object)
    assert str(e.value) == "Invalid Plan JSON"
