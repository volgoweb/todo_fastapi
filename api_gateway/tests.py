import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio()
async def test_tasks_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/tasks")
    response_data = response.json()
    assert response.status_code == 200
    assert response_data[0]["title"] == "task-1"
    print("======================")
    print(response)
    print(response.json())


def test_tasks():
    client = TestClient(app, raise_server_exceptions=False)
    response = client.get("/tasks")
    response_data = response.json()
    assert response.status_code == 200
    assert response_data[0]["title"] == "task-1"
