from fastapi import FastAPI
from api.endpoints import products, vendors, recommendations, reviews
from config.database import init_db

app = FastAPI(title="Reco-AI-Agent API")

# Include routers
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(vendors.router, prefix="/vendors", tags=["vendors"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

@app.on_event("startup")
async def startup_event():
    await init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
