from sqlalchemy.orm import Session
from app.core.database.models.DB_Profile import DB_Profile
from app.core.database.models.DB_Plan import DB_Plan
from app.core.database.models.DB_Problem import DB_Problem
from app.core.database.models.DB_Topic import DB_Topic

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
                    {"completed": True, "problem_id": 1},
                    {"completed": True, "problem_id": 2},
                    {"completed": True, "problem_id": 3},
                    {"completed": True, "problem_id": 4},
                    {"completed": True, "problem_id": 5},
                    {"completed": True, "problem_id": 8},
                    {"completed": False, "problem_id": 12},
                    {"completed": False, "problem_id": 18},
                ],
                "given_topics": [
                    {"topic_name": "Array"},
                ],
            },
            {
                "id": 2,
                "title": "recursion prep",
                "profile_id": 2,
                "problems": [
                    {"completed": True, "problem_id": 11},
                    {"completed": True, "problem_id": 12},
                    {"completed": False, "problem_id": 13},
                    {"completed": False, "problem_id": 14},
                    {"completed": False, "problem_id": 15},
                    {"completed": False, "problem_id": 16},
                    {"completed": False, "problem_id": 17},
                    {"completed": False, "problem_id": 18},
                ],
                "given_topics": [
                    {"topic_name": "Recursion"},
                ],
            },
            {
                "id": 3,
                "title": "graph important algorithms",
                "profile_id": 3,
                "problems": [
                    {"completed": True, "problem_id": 18},
                    {"completed": True, "problem_id": 19},
                    {"completed": False, "problem_id": 20},
                    {"completed": False, "problem_id": 21},
                    {"completed": False, "problem_id": 22},
                    {"completed": False, "problem_id": 23},
                    {"completed": False, "problem_id": 24},
                    {"completed": False, "problem_id": 25},
                    {"completed": False, "problem_id": 26},
                    {"completed": False, "problem_id": 27},
                    {"completed": False, "problem_id": 28},
                    {"completed": False, "problem_id": 29},
                ],
                "given_topics": [
                    {"topic_name": "Graph"},
                ],
            },
            {
                "id": 4,
                "title": "dp mediums",
                "profile_id": 4,
                "problems": [
                    {"completed": True, "problem_id": 12},
                    {"completed": True, "problem_id": 25},
                    {"completed": False, "problem_id": 26},
                    {"completed": False, "problem_id": 29},
                ],
                "given_topics": [
                    {"topic_name": "Dynamic Programming"},
                ],
            },
        ]

    @staticmethod
    def run(db: Session):
        existing_plan_ids = {plan.id for plan in db.query(DB_Plan).all()}
        existing_problems_ids = {problem.id for problem in db.query(DB_Problem).all()}
        existing_topics_names = {topic.name for topic in db.query(DB_Topic).all()}

        for plan_data in PlanSeeder.seed_data():
            if plan_data["id"] not in existing_plan_ids:
                profile: DB_Profile = db.query(DB_Profile).get(plan_data["profile_id"])
                if not profile:
                    continue

                valid_problems = []
                for problem_data in plan_data["problems"]:
                    if problem_data["problem_id"] not in existing_problems_ids:
                        continue
                    valid_problems.append(
                        [problem_data["completed"], problem_data["problem_id"]]
                    )

                valid_topics = []
                for topic_data in plan_data["given_topics"]:
                    if topic_data["topic_name"] not in existing_topics_names:
                        continue
                    valid_topics.append(topic_data["topic_name"])

                db_plan = DB_Plan(
                    id=plan_data["id"],
                    title=plan_data["title"],
                    profile_id=profile.id,
                    problems=valid_problems,
                    given_topics=valid_topics,
                )
                db.add(db_plan)
        db.commit()
