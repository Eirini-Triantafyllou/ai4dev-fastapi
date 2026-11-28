"""
Validation with Fields
"""

from pydantic import BaseModel, Field, ValidationError


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float=Field(gt=0, description="Item price")
    tax: float| None = Field(default=None, ge=0, description="Item tax")
    tags: list[str] = Field(default=[], max_length=10)

try:
    item = Item(name="Ram", price="2")
    print(item.model_dump())
except ValidationError as e:
    print(e)