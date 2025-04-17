from fastapi import FastAPI
from app.api.routes.plans import router as plans_router
app = FastAPI()
app.include_router(plans_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}