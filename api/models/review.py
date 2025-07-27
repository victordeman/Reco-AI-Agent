from pydantic import BaseModel
from datetime import datetime

class ReviewCreate(BaseModel):
    product_id: int
    rating: int
    comment: str | None = None

class Review(ReviewCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
