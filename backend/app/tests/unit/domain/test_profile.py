import pytest
from app.core.domain import Profile
from app.core.data.topics import ALL_TOPICS
from app.api.schemas.schemas import ProfileJSON

@pytest.fixture
def sample_proficiencies():
    return {topic: 0 for topic in ALL_TOPICS}

@pytest.fixture
def sample_profile_valid():
    return Profile(name="test")

@pytest.fixture
def sample_profile_invalid():
    return Profile(name="")

def test_profile_object_creation(sample_profile_valid):
    assert sample_profile_valid is not None

def test_profile_name_valid(sample_profile_valid):
    assert sample_profile_valid.name == "test"

def test_profile_proficiencies_valid(sample_profile_valid, sample_proficiencies):
    assert sample_profile_valid.proficiencies == sample_proficiencies

def test_profile_to_json_valid(sample_profile_valid):
    json_object = sample_profile_valid.to_json()
    assert isinstance(json_object, ProfileJSON)
    assert json_object.name == "test"

def test_profile_from_json_valid(sample_profile_valid, sample_proficiencies):
    json_object = sample_profile_valid.to_json()
    profile_new = Profile.from_json(json_object)
    assert isinstance(profile_new, Profile)
    assert profile_new.name == sample_profile_valid.name

def test_profile_from_json_invalid(sample_profile_invalid):
    json_object = sample_profile_invalid.to_json()
    with pytest.raises(ValueError) as e:
        Profile.from_json(json_object)
    assert str(e.value) == "Invalid Profile JSON"