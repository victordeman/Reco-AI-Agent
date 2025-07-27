from fastapi import APIRouter, Depends
from api.models.review import ReviewCreate, Review
from api.services.review_service import create_review, get_product_reviews
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=Review)
async def add_review(review: ReviewCreate, db: AsyncSession = Depends(get_db)):
    return await create_review(review, db)

@router.get("/{product_id}", response_model=list[Review])
async def list_reviews(product_id: int, db: AsyncSession = Depends(get_db)):
    return await get_product_reviews(product_id, db)
