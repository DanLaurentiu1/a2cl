import pytest

from app.core.domain import Profile
from app.core.validation import profile_validator


@pytest.fixture
def profile_valid():
    return Profile(name="test")

@pytest.fixture
def profile_empty_name():
    return Profile(name="")

@pytest.fixture
def profile_invalid_name_characters():
    return Profile(name="test!!")

@pytest.fixture
def profile_name_too_long():
    return Profile(name="nametoolongnametoolongnametoolong")

@pytest.fixture
def profile_proficiencies_over_cap():
    profile = Profile(name="test")
    profile.proficiencies["Array"] = 101
    return profile

def test_validate_profile_valid(profile_valid):
    assert profile_validator.validate_profile(profile_valid) is None

def test_validate_profile_invalid_empty_name(profile_empty_name):
    with pytest.raises(ValueError) as e:
        profile_validator.validate_profile(profile_empty_name)
    assert str(e.value) == "Profile name cannot be empty"

def test_validate_profile_invalid_name_too_long(profile_name_too_long):
    with pytest.raises(ValueError) as e:
        profile_validator.validate_profile(profile_name_too_long)
    assert str(e.value) == "Profile name must be <= 30 characters"

def test_validate_profile_invalid_proficiency_name_special_characters(profile_invalid_name_characters):
    with pytest.raises(ValueError) as e:
        profile_validator.validate_profile(profile_invalid_name_characters)
    assert str(e.value) == "Profile name contains invalid characters"

def test_validate_profile_invalid_proficiency_value_over_cap(profile_proficiencies_over_cap):
    with pytest.raises(ValueError) as e:
        profile_validator.validate_profile(profile_proficiencies_over_cap)
    assert str(e.value) == "Proficiency must be an integer between 0-100"