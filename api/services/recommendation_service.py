from sqlalchemy.ext.asyncio import AsyncSession
from llama_index.core import Document, VectorStoreIndex
from api.models.database import Product as ProductDB
from sqlalchemy.future import select

async def generate_recommendation(product_id: int, vendor_id: int, db: AsyncSession):
    # Fetch product
    result = await db.execute(select(ProductDB).where(ProductDB.id == product_id))
    product = result.scalars().first()
    if not product:
        return "Product not found."
    
    # Mock recommendation logic (replace with LlamaIndex + Mem0)
    document = Document(text=product.description)
    index = VectorStoreIndex.from_documents([document])
    query_engine = index.as_query_engine()
    recommendation = query_engine.query(f"Recommend a product similar to {product.name}")
    return str(recommendation)
