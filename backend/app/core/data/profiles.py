from typing import List

from app.core.domain import Profile

ALL_PROFILES: List[Profile] = [
    Profile("Profile 1"),
    Profile("Profile 2"),
    Profile("Profile 3"),
]


def get_profile_by_name(name: str) -> Profile:
    profile = None
    for p in ALL_PROFILES:
        if p.name == name:
            profile = p
            break
    if profile is None:
        raise ValueError(f"Profile '{name}' not found")
    return profile
