from sqlalchemy import  Enum, Column, Integer, String
from sqlalchemy.orm import declarative_base

from backend.app.api.schemas.schemas import TopicTypes
from backend.app.core.domain import Topic

Base = declarative_base()

class DB_Topic(Base):
    __tablename__ = 'topics'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(Enum(TopicTypes), nullable=False)

    def to_entity(self) -> 'Topic':
        return Topic(name=self.name, topic_type=self.type)
    
    @classmethod
    def from_entity(self, topic: 'Topic') -> 'DB_Topic':
        return self(name=topic.name, type=topic.type)