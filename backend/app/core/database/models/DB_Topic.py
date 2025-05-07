from sqlalchemy import Column, Enum, Integer, String
from app.core.database.base import Base
from app.api.schemas.schemas import TopicTypes
from app.core.domain import Topic

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