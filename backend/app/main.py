from fastapi import FastAPI
from app.api.routes.plans import router as plans_router
app = FastAPI()
app.include_router(plans_router)