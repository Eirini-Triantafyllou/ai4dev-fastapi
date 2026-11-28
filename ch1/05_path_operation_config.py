"""
Path Operation Configuration
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post(
    "/items/",
    tags=["items"],
    summary="Create a new item",
    description="Creates an item",
    response_description="A new item",
    responses={
        404: {"description": "Not found"},
        422: {"description": "Validation Error"}
            },
    status_code=status.HTTP_201_CREATED
)

async def create_item(item: Item):
    return {"id": 1, "name": item.name, "price": item.price}