"""
Separate models
"""

from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

class ItemUpdate(BaseModel):
    name: str | None = None
    price: float | None = Field(default=0, gt=0)

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float