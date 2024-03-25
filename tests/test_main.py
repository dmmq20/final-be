import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.db.tables_setup import drop_tables, create_tables, insert_test_documents, insert_test_users

client = TestClient(app)


@pytest.fixture(autouse=True)
def reseed_database():
    drop_tables()
    create_tables()
    insert_test_documents()
    insert_test_users()

    yield


def test_get_users():
    response = client.get("/users")
    users_data = response.json()
    # not currently testing for instances where the first_name is not present
    expected_keys = ["id", "created_at", "username", "first_name"]
    assert response.status_code == 200
    assert len(users_data) == 2
    for user in users_data:
        assert all(key in user for key in expected_keys)


def test_get_user():
    response = client.get("/users/1")
    user_data = response.json()
    # not currently testing for instances where the first_name is not present
    expected_keys = ["id", "created_at", "username", "first_name"]
    assert response.status_code == 200
    assert all(key in user_data for key in expected_keys)


def test_get_documents():
    response = client.get("/documents")
    documents_data = response.json()
    expected_keys = ["id", "title", "content", "created_at"]
    assert response.status_code == 200
    assert len(documents_data) == 2
    for document in documents_data:
        assert all(key in document for key in expected_keys)


def test_get_document():
    response = client.get("/documents/1")
    document_data = response.json()
    expected_keys = ["id", "title", "content", "created_at"]
    assert response.status_code == 200
    assert all(key in document_data for key in expected_keys)


def test_post_document():
    post_body = {"title": "doc3", "content": "more info"}
    response = client.post("/documents", json=post_body)
    posted_document = response.json()
    expected_keys = ["id", "title", "content", "created_at"]
    assert response.status_code == 201
    assert all(key in posted_document for key in expected_keys)
    
