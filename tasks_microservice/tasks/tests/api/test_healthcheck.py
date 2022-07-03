from fastapi.testclient import TestClient
from fastapi import status
from tasks.main import app

client = TestClient(app)


def test_happy_path():
    response = client.get("/healthcheck")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "pong"}
