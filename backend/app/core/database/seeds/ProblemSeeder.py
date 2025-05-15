from pathlib import Path
from sqlalchemy.orm import Session
from app.core.database.models.DB_Problem import DB_Problem
from app.core.database.models.DB_Topic import DB_Topic
from typing import List, Dict

from backend.app.model.utils.conversion.convert_csv_to_json import convert_csv_to_json

class ProblemSeeder:
    @staticmethod
    def seed_data() -> List[Dict]:
        current_dir = Path(__file__).parent
        base_dir = current_dir.parent.parent.parent
        csv_path = base_dir / "model" / "data" / "leetcode_questions.csv"
        return convert_csv_to_json(csv_path)

    @staticmethod
    def run(db: Session):
        existing_ids = {p.id for p in db.query(DB_Problem).all()}
        for problem_data in ProblemSeeder.seed_data():
            if problem_data["id"] not in existing_ids:
                db_problem = DB_Problem(
                    id=problem_data["id"],
                    name=problem_data["name"],
                    difficulty=problem_data["difficulty"],
                    acceptance_rate=problem_data["acceptance_rate"],
                    topics=problem_data["topics"]
                )
                db.add(db_problem)
        
        db.commit()