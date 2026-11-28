"""
Route Order
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def get_user_me():
    return {"username": "me!"}

@app.get("/users/{username}")
async def get_username(username: str):
    return {"username": username}

