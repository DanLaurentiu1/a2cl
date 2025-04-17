from typing import List, Tuple
from app.core.data.plans import INITIAL_PLANS
from app.core.domain import Plan, Problem
from app.core.repository.PlanStore import PlanStore
from app.core.validation import plan_validator

class PlanServerRepository:    
    def __init__(self):
        self._store = PlanStore(INITIAL_PLANS)
        
    def get_all_plans(self) -> List[Plan]:
        return self._store.get_all_plans()
    
    def get_plan(self, plan_id: int) -> Plan:
        if not isinstance(plan_id, int) or plan_id < 1:
            raise ValueError("Plan ID must be a positive integer")
        return self._store.get(plan_id)
    
    def add_plan(self, plan_data: Plan) -> Plan:
        plan_validator.validate_plan(plan_data)
        return self._store.add(plan_data)
    
    def update_plan_problems(
        self, 
        plan_id: int, 
        problems: List[Tuple[bool, Problem]]
    ) -> Plan:
        self.get_plan(plan_id)
        if not problems:
            raise ValueError("Problems list cannot be empty")
        return self._store.update_problems(plan_id, problems)
    
    def delete_plan(self, plan_id: int) -> Plan:
        return self._store.remove(plan_id)