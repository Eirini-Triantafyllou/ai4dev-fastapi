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