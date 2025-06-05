import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.plans import router as plans_router
from app.core.database.database import seed_database
import logging

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()
app.include_router(plans_router)

origins = os.getenv("CORS_ORIGINS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    seed_database()
