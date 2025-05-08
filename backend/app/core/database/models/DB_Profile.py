from sqlalchemy import JSON, Column, Integer, String
from app.core.database.base import Base
from app.core.database.models import DB_Profile
from app.api.schemas.schemas import TopicTypes
from app.core.domain import Profile, Topic


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

    def __repr__(self):
        return f"DB_Profile(id={self.id}, name={self.name}, proficiencies={self.proficiencies})"