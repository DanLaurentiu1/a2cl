from sqlalchemy import ARRAY, JSON, Enum, Float, create_engine, SQLEnum, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from backend.app.api.schemas.schemas import DifficultyLevel, TopicTypes
from backend.app.core.domain import Problem, Profile, Topic

Base = declarative_base()

class DB_Problem(Base):
    __tablename__ = 'problems'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    acceptance_rate = Column(Float, nullable=False)
    topics = Column(JSON, nullable=True, default={})
    
    def to_entity(self) -> 'Problem':
        return Problem(
            id=self.id,
            name=self.name,
            topics=[Topic(name=topic['name'], type=TopicTypes(topic['type'])) 
                    for topic in self.topics],
            difficulty=self.difficulty,
            acceptanceRate=self.acceptance_rate
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