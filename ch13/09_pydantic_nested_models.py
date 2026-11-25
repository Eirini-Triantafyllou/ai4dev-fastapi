from pydantic import BaseModel

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    price: float
    images: list[Image] = []

item = Item(
    name="Laptop",
    price=5.50,
    images=[
        Image(url="https://example.com/image.jpg", name="front"),
        Image(url="https://example.com/image.jpg", name="back")
    ]
)

print(item.model_dump())