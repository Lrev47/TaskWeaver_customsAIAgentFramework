import pytest
from httpx import AsyncClient
from api.main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AgentHiveMind API!"}

@pytest.mark.asyncio
async def test_deconstruct():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/deconstruct/", json={"input": "Analyze my business plan"})
    assert response.status_code == 200
    assert "tasks" in response.json()
