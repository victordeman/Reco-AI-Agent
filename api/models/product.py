from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    quantity: int

    class Config:
        from_attributes = True
