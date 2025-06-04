import os
from pathlib import Path
from typing import List, Tuple, Optional
from sqlalchemy.orm import Session
from app.core.domain import Plan, Problem, Profile
from app.core.validation import plan_validator
from app.core.database.models.DB_Plan import DB_Plan
from app.core.database.models.DB_Problem import DB_Problem
from app.core.database.models.DB_Profile import DB_Profile
from app.core.database.models.DB_Topic import DB_Topic
from app.model.Trainer import LeetcodeTrainer


class PlanServerRepository:
    def __init__(self, db: Session):
        self._db = db
        self._trainer: LeetcodeTrainer = LeetcodeTrainer()
    
    def get_all_plans(self) -> List[Plan]:
        db_plans: DB_Plan = self._db.query(DB_Plan).all()
        return [plan.to_entity(self._db) for plan in db_plans]
    
    def get_plan(self, plan_id: int) -> Optional[Plan]:
        if not isinstance(plan_id, int) or plan_id < 1:
            raise ValueError("Plan ID must be a positive integer")
        
        db_plan: DB_Plan = self._db.query(DB_Plan).filter(DB_Plan.id == plan_id).first()
        return db_plan.to_entity(self._db)
    
    def create_plan_with_recommendations(self, plan_data: Plan) -> Plan:
        plan_validator.validate_plan(plan_data)
        plan_with_problems = self.add_problems_to_plan(plan_data)
        return self.add_plan(plan_with_problems)

    def add_plan(self, plan_data: Plan) -> Plan:
        db_plan = DB_Plan.from_entity(plan_data, self._db, adding=True)
        self._db.add(db_plan)
        self._db.commit()
        self._db.refresh(db_plan)
        return db_plan.to_entity(self._db)
    
    def add_problems_to_plan(self, plan_data: Plan) -> Plan:
        model_path = Path(__file__).parent.parent.parent / 'model' / 'checkpoints' / 'final_model_200000.zip'
        topic_names = [topic.name for topic in plan_data.given_topics]
        recommended_problem_ids = self._trainer.evaluate(env_targets=topic_names, load_path=model_path)
        problems = []
        for problem_id in recommended_problem_ids:
            db_problem: DB_Problem = self._db.query(DB_Problem).get(problem_id)
            if db_problem:
                problems.append((False, db_problem.to_entity()))
        plan_data.problems = problems
        return plan_data
    
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
        plan.problems = problems
        db_plan = DB_Plan.from_entity(plan, self._db)
        self._db.merge(db_plan)
        self._db.commit()
        return self.get_plan(plan_id)
    
    def delete_plan(self, plan_id: int) -> Optional[Plan]:
        plan = self.get_plan(plan_id)
        if plan:
            self._db.query(DB_Plan).filter(DB_Plan.id == plan_id).delete()
            self._db.commit()
        return plan