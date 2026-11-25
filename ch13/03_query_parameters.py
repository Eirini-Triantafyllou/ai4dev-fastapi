"""
Query Parameters
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(
        skip: int = 0,
        limit: int = 100,
        q: str | None = None,
):
    return {"skip": skip, "limit": limit, "q": q}
