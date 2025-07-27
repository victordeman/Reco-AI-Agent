from fastapi import APIRouter, Depends
from api.models.vendor import Vendor
from api.services.vendor_service import get_all_vendors
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Vendor])
async def list_vendors(db: AsyncSession = Depends(get_db)):
    return await get_all_vendors(db)
