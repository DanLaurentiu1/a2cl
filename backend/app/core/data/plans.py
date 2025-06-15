from typing import List
from app.core.data.problems import get_problem_by_id
from app.core.data.profiles import get_profile_by_name
from app.core.domain import Plan

INITIAL_PLANS: List[Plan] = [
    Plan(
        1,
        "Plan 1",
        get_profile_by_name("Profile 1"),
        [
            [True, get_problem_by_id(1)],
            [True, get_problem_by_id(2)],
            [True, get_problem_by_id(3)],
            [True, get_problem_by_id(4)],
            [False, get_problem_by_id(5)],
            [False, get_problem_by_id(8)],
            [False, get_problem_by_id(12)],
            [False, get_problem_by_id(18)],
        ],
    ),
    Plan(
        2,
        "Plan 2",
        get_profile_by_name("Profile 2"),
        [
            [True, get_problem_by_id(11)],
            [True, get_problem_by_id(12)],
            [False, get_problem_by_id(13)],
            [False, get_problem_by_id(14)],
            [False, get_problem_by_id(15)],
            [False, get_problem_by_id(16)],
            [False, get_problem_by_id(17)],
            [False, get_problem_by_id(18)],
        ],
    ),
    Plan(
        3,
        "Plan 3",
        get_profile_by_name("Profile 2"),
        [
            [True, get_problem_by_id(18)],
            [True, get_problem_by_id(19)],
            [False, get_problem_by_id(20)],
            [False, get_problem_by_id(21)],
            [False, get_problem_by_id(22)],
            [False, get_problem_by_id(23)],
            [False, get_problem_by_id(24)],
            [False, get_problem_by_id(25)],
            [False, get_problem_by_id(26)],
            [False, get_problem_by_id(27)],
            [False, get_problem_by_id(28)],
            [False, get_problem_by_id(29)],
        ],
    ),
    Plan(
        4,
        "Plan 4",
        get_profile_by_name("Profile 1"),
        [
            [True, get_problem_by_id(4)],
            [True, get_problem_by_id(5)],
        ],
    ),
    Plan(
        5,
        "Plan 5",
        get_profile_by_name("Profile 2"),
        [
            [True, get_problem_by_id(18)],
            [True, get_problem_by_id(19)],
            [True, get_problem_by_id(20)],
            [False, get_problem_by_id(21)],
            [False, get_problem_by_id(29)],
        ],
    ),
    Plan(
        6,
        "Plan 6",
        get_profile_by_name("Profile 1"),
        [
            [False, get_problem_by_id(26)],
            [False, get_problem_by_id(27)],
            [False, get_problem_by_id(28)],
            [False, get_problem_by_id(29)],
        ],
    ),
    Plan(
        7,
        "Plan 7",
        get_profile_by_name("Profile 1"),
        [
            [True, get_problem_by_id(1)],
            [True, get_problem_by_id(2)],
            [True, get_problem_by_id(8)],
            [True, get_problem_by_id(9)],
        ],
    ),
    Plan(
        8,
        "Plan 8",
        get_profile_by_name("Profile 1"),
        [
            [True, get_problem_by_id(12)],
            [True, get_problem_by_id(25)],
            [True, get_problem_by_id(26)],
            [False, get_problem_by_id(29)],
        ],
    ),
    Plan(
        9,
        "Plan 9",
        get_profile_by_name("Profile 2"),
        [
            [True, get_problem_by_id(12)],
            [True, get_problem_by_id(25)],
            [True, get_problem_by_id(26)],
            [False, get_problem_by_id(29)],
        ],
    ),
    Plan(
        10,
        "Plan 10",
        get_profile_by_name("Profile 2"),
        [
            [True, get_problem_by_id(12)],
            [True, get_problem_by_id(25)],
            [False, get_problem_by_id(26)],
            [False, get_problem_by_id(29)],
        ],
    ),
]


def get_plan_by_id(id: int) -> Plan:
    for plan in INITIAL_PLANS:
        if plan.id == id:
            return plan
    raise ValueError(f"No plan found with id={id}")
