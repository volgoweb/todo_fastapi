from fastapi import status
from fastapi.testclient import TestClient
from tasks.main import app
from tasks.tests.utils import Anything

client = TestClient(app)
TEST_TITLE = "test title"
TEST_DESCRIPTION = "test description"


def test_happy_path():
    response = client.post(
        "/tasks", json={"title": TEST_TITLE, "description": TEST_DESCRIPTION}
    )
    assert response.status_code == status.HTTP_201_CREATED
    actual_data = response.json()

    assert actual_data == {
        "id": Anything(),
        "title": TEST_TITLE,
        "description": TEST_DESCRIPTION,
    }
