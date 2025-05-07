from typing import List, Tuple, Optional
from sqlalchemy.orm import Session
from app.core.domain import Plan, Problem, Profile
from app.core.validation import plan_validator
from app.core.database.models.DB_Plan import DB_Plan
from app.core.database.models.DB_Problem import DB_Problem
from app.core.database.models.DB_Profile import DB_Profile
from app.core.database.models.DB_Topic import DB_Topic


class PlanServerRepository:
    def __init__(self, db: Session):
        self._db = db
    
    def get_all_plans(self) -> List[Plan]:
        db_plans: DB_Plan = self._db.query(DB_Plan).all()
        return [plan.to_entity(self._db) for plan in db_plans]
    
    def get_plan(self, plan_id: int) -> Optional[Plan]:
        if not isinstance(plan_id, int) or plan_id < 1:
            raise ValueError("Plan ID must be a positive integer")
        
        db_plan: DB_Plan = self._db.query(DB_Plan).filter(DB_Plan.id == plan_id).first()
        return db_plan.to_entity(self._db)
    
    def add_plan(self, plan_data: Plan) -> Plan:
        plan_validator.validate_plan(plan_data)
        
        db_plan = DB_Plan.from_entity(plan_data, self._db)
        self._db.add(db_plan)
        self._db.commit()
        self._db.refresh(db_plan)
        return db_plan.to_entity(self._db)
    
    def update_plan_problems(
        self, 
        plan_id: int, 
        problems: List[Tuple[bool, Problem]]
    ) -> Plan:
        plan = self.get_plan(plan_id)
        if not plan:
            raise ValueError(f"Plan with ID {plan_id} not found")
        if not problems:
            raise ValueError("Problems list cannot be empty")
        
        # Update the problems in the plan
        plan.problems = problems
        db_plan = DB_Plan.from_entity(plan, self._db)
        
        # Merge changes back into the session
        self._db.merge(db_plan)
        self._db.commit()
        return self.get_plan(plan_id)
    
    def delete_plan(self, plan_id: int) -> Optional[Plan]:
        plan = self.get_plan(plan_id)
        if plan:
            self._db.query(DB_Plan).filter(DB_Plan.id == plan_id).delete()
            self._db.commit()
        return plan
    
    def get_all_profiles(self) -> List[Profile]:
        db_profiles = self._db.query(DB_Profile).all()
        return [profile.to_entity() for profile in db_profiles]
    
    def get_profile(self, profile_id: int) -> Optional[Profile]:
        db_profile = self._db.query(DB_Profile).filter(DB_Profile.id == profile_id).first()
        return db_profile.to_entity() if db_profile else None
    
    def get_all_problems(self) -> List[Problem]:
        db_problems = self._db.query(DB_Problem).all()
        return [problem.to_entity() for problem in db_problems]
    
    def get_problem(self, problem_id: int) -> Optional[Problem]:
        db_problem = self._db.query(DB_Problem).filter(DB_Problem.id == problem_id).first()
        return db_problem.to_entity() if db_problem else None