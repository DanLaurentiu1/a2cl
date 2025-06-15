import re

from app.core.domain import Profile


class ProfileValidator:
    def validate_profile(self, profile: Profile) -> None:
        self.validate_profile_name(profile)
        self.validate_profile_proficiencies(profile)

    def validate_profile_proficiencies(self, profile: Profile) -> None:
        for _, value in profile.proficiencies.items():
            if not isinstance(value, int) or value < 0 or value > 100:
                raise ValueError("Proficiency must be an integer between 0-100")

    def validate_profile_name(self, profile: Profile) -> None:
        if not profile.name:
            raise ValueError("Profile name cannot be empty")

        if not re.match(r"^(?! )[A-Za-z0-9]+$", profile.name):
            raise ValueError("Profile name contains invalid characters")

        if len(profile.name) > 30:
            raise ValueError("Profile name must be <= 30 characters")


profile_validator = ProfileValidator()
