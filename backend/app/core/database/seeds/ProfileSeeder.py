from typing import Dict
from sqlalchemy.orm import Session
from app.core.database.models.DB_Profile import DB_Profile
from app.core.database.models.DB_Topic import DB_Topic

class ProfileSeeder:
    @staticmethod
    def get_all_topic_names(db: Session) -> list[str]:
        return [topic.name for topic in db.query(DB_Topic).all()]

    @staticmethod
    def seed_data(db: Session) -> list[Dict]:
        all_topics = ProfileSeeder.get_all_topic_names(db)
        return [
            {
                "name": "profile1",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile2",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile3",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile4",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile5",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile6",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile7",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile8",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile9",
                "proficiencies": {topic: 0 for topic in all_topics}
            },
            {
                "name": "profile10",
                "proficiencies": {topic: 0 for topic in all_topics}
            }
        ]

    @staticmethod
    def run(db: Session):
        existing_profiles = {p.name for p in db.query(DB_Profile).all()}
        
        for profile_data in ProfileSeeder.seed_data(db):
            if profile_data["name"] not in existing_profiles:
                db.add(DB_Profile(
                    name=profile_data["name"],
                    proficiencies=profile_data["proficiencies"]
                ))
        
        db.commit()