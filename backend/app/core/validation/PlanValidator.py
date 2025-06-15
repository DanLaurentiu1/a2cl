import re

from app.core.domain import Plan
from app.core.validation.ProfileValidator import profile_validator


class PlanValidator:
    def validate_plan(self, plan: Plan) -> None:
        self.validate_plan_title(plan)
        self.validate_plan_profile(plan)

    def validate_plan_profile(self, plan: Plan) -> None:
        profile_validator.validate_profile(plan.profile)

    def validate_plan_title(self, plan: Plan) -> None:
        if not isinstance(plan.title, str):
            raise ValueError("Title must be a string")

        if not re.match(r"^(?! )[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$", plan.title):
            raise ValueError("Title contains invalid characters")

        if len(plan.title) > 100:
            raise ValueError("Plan title must be <= 100 characters")


plan_validator = PlanValidator()
