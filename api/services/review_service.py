from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.review import Review, ReviewCreate
from api.models.database import Review as ReviewDB
from datetime import datetime

async def create_review(review: ReviewCreate, db: AsyncSession):
    db_review = ReviewDB(
        product_id=review.product_id,
        rating=review.rating,
        comment=review.comment,
        created_at=datetime.utcnow()
    )
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return Review.from_orm(db_review)

async def get_product_reviews(product_id: int, db: AsyncSession):
    result = await db.execute(select(ReviewDB).where(ReviewDB.product_id == product_id))
    return [Review.from_orm(r) for r in result.scalars().all()]
