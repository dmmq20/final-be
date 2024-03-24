import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    users_data = response.json()
    assert len(users_data) == 2
    expected_keys = ["id", "created_at", "username", "first_name"] # not currently testing for instances where the first_name is not present
    for user in users_data:
        assert all(key in user for key in expected_keys)


def test_get_user():
    response = client.get("/users/1")
    user_data = response.json()
    assert response.status_code == 200
    expected_keys = ["id", "created_at", "username", "first_name"] # not currently testing for instances where the first_name is not present
    assert all(key in user_data for key in expected_keys)



