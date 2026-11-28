"""
HTTPException Example
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {1: "Laptop", 2: "Mouse"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=404,  # status.HTTP_404_NOT_FOUND
            detail=f'Item with id {item_id} not found'
        )

    return {"item_id": item_id, "name": items[item_id]}