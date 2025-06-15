from typing import List, Dict, Tuple
from dataclasses import dataclass

from app.core.domain import Plan, Problem


@dataclass
class PlanStore:
    _plans: Dict[int, Plan]
    _next_id: int = 1

    def __init__(self, initial_plans: List[Plan]):
        self._plans = {plan.id: plan for plan in initial_plans}
        self.update_id()

    def update_id(self) -> int:
        self._next_id = max(self._plans.keys(), default=0) + 1

    def get_all_plans(self) -> List[Plan]:
        return list(self._plans.values())

    def get(self, plan_id: int) -> Plan:
        if plan_id not in self._plans:
            raise KeyError(f"Plan {plan_id} not found")
        return self._plans.get(plan_id)

    def add(self, plan: Plan) -> Plan:
        new_plan = Plan(
            id=self._next_id,
            title=plan.title,
            profile=plan.profile,
            problems=plan.problems,
        )

        self._plans[self._next_id] = new_plan
        self._next_id += 1
        return self._plans[self._next_id - 1]

    def update_problems(
        self, plan_id: int, problems: List[Tuple[bool, Problem]]
    ) -> Plan:
        if plan_id not in self._plans:
            raise KeyError(f"Plan {plan_id} not found")
        else:
            plan = self._plans.get(plan_id)

        updated = Plan(
            id=plan.id, title=plan.title, profile=plan.profile, problems=problems
        )

        self._plans[plan_id] = updated
        return updated

    def remove(self, plan_id: int) -> Plan:
        if plan_id not in self._plans:
            raise KeyError(f"Plan {plan_id} not found")

        popped = self._plans.pop(plan_id)
        if popped:
            self.update_id()
        return popped
