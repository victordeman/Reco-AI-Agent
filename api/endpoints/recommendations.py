from fastapi import APIRouter, Depends
from api.services.recommendation_service import generate_recommendation
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db

router = APIRouter()

@router.get("/{product_id}/{vendor_id}", response_model=dict)
async def get_recommendation(product_id: int, vendor_id: int, db: AsyncSession = Depends(get_db)):
    recommendation = await generate_recommendation(product_id, vendor_id, db)
    return {"recommendation": recommendation}
