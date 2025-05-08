from sqlalchemy import JSON, Column, Float, Integer, String
from app.core.database.base import Base
from app.api.schemas.schemas import TopicTypes
from app.core.database.models import DB_Problem
from app.core.domain import Problem
from app.core.domain import Topic


class DB_Problem(Base):
    __tablename__ = 'problems'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    difficulty = Column(Integer, nullable=False)
    acceptance_rate = Column(Float, nullable=False)
    topics = Column(JSON, nullable=True, default={})
    
    def to_entity(self) -> 'Problem':
        return Problem(
            id=self.id,
            name=self.name,
            topics=[Topic(name=topic['name'], type=TopicTypes(topic['type'])) 
                    for topic in self.topics],
            difficulty=self.difficulty,
            acceptance_rate=self.acceptance_rate
        )
    
    @classmethod
    def from_entity(self, problem: 'Problem') -> 'DB_Problem':
        return self(
            id=problem.id,
            name=problem.name,
            difficulty=problem.difficulty,
            acceptance_rate=problem.acceptanceRate,
            topics=[{
                'name': topic.name,
                'type': topic.type.value
            } for topic in problem.topics]
        )
