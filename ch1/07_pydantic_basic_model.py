from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float| None = None

item = Item(name="Laptop", price=999.99, tax =10.54)
# item = Item(name="Ram", price="abc") #returns validation error
print(item.model_dump())