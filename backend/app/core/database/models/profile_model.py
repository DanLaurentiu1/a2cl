from sqlalchemy import JSON, create_engine, SQLEnum, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from backend.app.api.schemas.schemas import TopicTypes
from backend.app.core.domain import Profile, Topic

Base = declarative_base()

class DB_Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    proficiencies = Column(JSON, nullable=False, default={})
    
    def to_entity(self) -> 'Profile':
        profile = Profile(self.name)
        
        profile._proficiencies = {
            Topic(name=topic_name, topic_type=TopicTypes(topic_data["type"])): topic_data["proficiency"]
            for topic_name, topic_data in self.proficiencies.items()
        }
        return profile
    
    @classmethod
    def from_entity(self, profile: 'Profile') -> 'DB_Profile':
        proficiencies_json = {
            topic.name: {
                "type": topic.type.value,
                "proficiency": level
            }
            for topic, level in profile.proficiencies.items()
        }
        
        return self(
            name=profile.name,
            proficiencies=proficiencies_json
        )