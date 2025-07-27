import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_products():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/products/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
