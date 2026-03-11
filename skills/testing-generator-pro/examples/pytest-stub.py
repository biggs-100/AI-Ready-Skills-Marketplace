import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_feature_success(client: AsyncClient):
    """
    TODO: Implement successful scenario for {feature}
    """
    response = await client.get("/api/v1/endpoint")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_feature_unauthorized(client: AsyncClient):
    """
    TODO: Implement unauthorized scenario
    """
    response = await client.get("/api/v1/endpoint")
    assert response.status_code == 401
