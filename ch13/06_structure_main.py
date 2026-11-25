"""
Project Structure with APIRouter
"""

#main.py file
from fastapi import FastAPI
from routers.items import router as items_router

app = FastAPI()

app.include_router(
    items_router,
    prefix="/api/v1",
)

#routers/items.py file
from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_item(skip: int = 0, limit: int = 20):
    return {"skip": skip, "limit": limit}

@router.get("/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}