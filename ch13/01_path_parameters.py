"""
Path parameters example

fastapi dev ch13/01_path_parameters.py
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}