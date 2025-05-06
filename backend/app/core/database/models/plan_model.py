from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

from app.core.domain import Plan
from backend.app.core.database.models.problem_model import DB_Problem
from backend.app.core.database.models.profile_model import DB_Profile

Base = declarative_base()

class DB_Plan(Base):
    __tablename__ = 'plans'
   
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    profile_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)
    problems = Column(JSON, nullable=False, default=[])

    def to_entity(self, session: Session) -> 'Plan':
        db_profile = session.query(DB_Profile).filter_by(id=self.profile_id).first()
        if db_profile:
            profile = db_profile.to_entity()

        problems_list = []
        for problem_data in self.problems:
            problem_id = problem_data[0]
            completed = problem_data[1]
            db_problem: DB_Problem = session.query(DB_Problem).get(problem_id)
            if db_problem:
                problems_list.append((completed, db_problem.to_entity()))
        
        return Plan(
            id=self.id,
            title=self.title,
            profile=profile,
            problems=problems_list
        )
    
    @classmethod
    def from_entity(self, plan: 'Plan', session: Session) -> 'DB_Plan':
        db_profile = session.query(DB_Profile).filter_by(name=plan.profile.name).first()
        if not db_profile:
            db_profile = DB_Profile.from_entity(plan.profile)
            session.add(db_profile)
            session.commit()
        
        problems_json = [
            [problem.id, completed] 
            for completed, problem in plan.problems
        ]
        
        return self(
            id=plan.id,
            title=plan.title,
            profile_id=db_profile.id,
            problems=problems_json
        )