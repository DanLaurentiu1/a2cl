from sqlalchemy.orm import Session
from app.core.database.models.DB_Profile import DB_Profile
from app.core.database.models.DB_Plan import DB_Plan
from app.core.database.models.DB_Problem import DB_Problem

from typing import List, Dict

class PlanSeeder:
    @staticmethod
    def seed_data() -> List[Dict]:
        return [
            {
                "id": 1,
                "title": "Beginner Array Practice",
                "profile_id": 1,
                "problems": [
                    [True, 1],
                    [True, 2],
                    [True, 3],
                    [True, 4],
                    [True, 5],
                    [True, 8],
                    [False, 12],
                    [False, 18]
                ]
            },
            {
                "id": 2,
                "title": "recursion prep",
                "profile_id": 2, 
                "problems": [
                    [True, 11],
                    [True, 12],
                    [False, 13],
                    [False, 14],
                    [False, 15],
                    [False, 16],
                    [False, 17],
                    [False, 18]
                ]
            },
            {
                "id": 3,
                "title": "graph important algorithms",
                "profile_id": 3,
                "problems": [
                    [True, 18],
                    [True, 19],
                    [False, 20],
                    [False, 21],
                    [False, 22],
                    [False, 23],
                    [False, 24],
                    [False, 25],
                    [False, 26],
                    [False, 27],
                    [False, 28],
                    [False, 29]
                ]
            },
            {
                "id": 4,
                "title": "dp mediums",
                "profile_id": 4,
                "problems": [
                    [True, 12],
                    [True, 25],
                    [False, 26],
                    [False, 29]
                ]
            }
        ]

    @staticmethod
    def run(db: Session):
        existing_plan_ids = {plan.id for plan in db.query(DB_Plan).all()}
        existing_problems_ids = {problem.id for problem in db.query(DB_Problem).all()}

        for plan_data in PlanSeeder.seed_data():
            if plan_data["id"] not in existing_plan_ids:
                profile = db.query(DB_Profile).get(plan_data["profile_id"])
                if not profile:
                    print(f"Profile {plan_data['profile_name']} not found, skipping plan {plan_data['id']}")
                    continue
                
                valid_problems = []
                for completed, problem_id in plan_data["problems"]:
                    if problem_id not in existing_problems_ids:
                        print(f"Problem {problem_id} not found, skipping from plan {plan_data['id']}")
                        continue
                    valid_problems.append([completed, problem_id])
                
                db_plan = DB_Plan(
                    id=plan_data["id"],
                    title=plan_data["title"],
                    profile_id=profile.id,
                    problems=valid_problems
                )
                db.add(db_plan)
        db.commit()