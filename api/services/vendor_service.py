from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.vendor import Vendor
from api.models.database import Vendor as VendorDB

async def get_all_vendors(db: AsyncSession):
    result = await db.execute(select(VendorDB))
    return [Vendor.from_orm(v) for v in result.scalars().all()]
