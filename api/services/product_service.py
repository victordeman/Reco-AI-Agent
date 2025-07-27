from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.product import Product
from api.models.database import Product as ProductDB

async def get_all_products(db: AsyncSession):
    result = await db.execute(select(ProductDB))
    return [Product.from_orm(p) for p in result.scalars().all()]

async def get_vendor_products(vendor_id: int, db: AsyncSession):
    result = await db.execute(
        select(ProductDB).join(VendorProduct).where(VendorProduct.vendor_id == vendor_id)
    )
    return [Product.from_orm(p) for p in result.scalars().all()]
