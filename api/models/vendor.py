from pydantic import BaseModel

class Vendor(BaseModel):
    id: int
    name: str
    contact_info: str | None = None

    class Config:
        from_attributes = True
