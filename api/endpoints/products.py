from fastapi import APIRouter, Depends
from api.models.product import Product
from api.services.product_service import get_all_products, get_vendor_products
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Product])
async def list_products(db: AsyncSession = Depends(get_db)):
    return await get_all_products(db)

@router.get("/{vendor_id}", response_model=list[Product])
async def list_vendor_products(vendor_id: int, db: AsyncSession = Depends(get_db)):
    return await get_vendor_products(vendor_id, db)
