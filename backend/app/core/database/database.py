import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.core.database.base import Base
from app.core.database.seeds.TopicSeeder import TopicSeeder
from app.core.database.seeds.ProfileSeeder import ProfileSeeder
from app.core.database.seeds.ProblemSeeder import ProblemSeeder
from app.core.database.seeds.PlanSeeder import PlanSeeder

load_dotenv()

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from app.core.database.models import DB_Topic, DB_Profile, DB_Problem, DB_Plan

Base.metadata.create_all(bind=engine)


def seed_database():
    db = SessionLocal()

    try:
        TopicSeeder.run(db)
        ProfileSeeder.run(db)
        ProblemSeeder.run(db)
        PlanSeeder.run(db)
    finally:
        db.close()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
