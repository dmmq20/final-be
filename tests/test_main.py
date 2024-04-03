import pytest
from main import app
from fastapi.testclient import TestClient
from app.db.tables_setup import drop_tables, create_tables, insert_test_documents, insert_test_users, insert_test_comments

client = TestClient(app)


@pytest.fixture(autouse=True)
def reseed_database():
    drop_tables()
    create_tables()
    insert_test_users()
    insert_test_documents()
    insert_test_comments()

    yield


def test_get_users():
    response = client.get("/users")
    users_data = response.json()
    expected_keys = ["id", "created_at", "username", "password"]
    assert response.status_code == 200
    assert len(users_data) == 2
    for user in users_data:
        assert all(key in user for key in expected_keys)


def test_get_user():
    response = client.get("/users/1")
    user_data = response.json()
    expected_keys = ["id", "created_at", "username", "password"]
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


def test_get_nonexistant_document():
    response = client.get("/documents/99999")
    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "Document not found"


def test_post_document():
    post_body = {"title": "doc3", "content": "more info", "author_id": 1, "author": "testuser"}
    response = client.post("/documents", json=post_body)
    posted_document = response.json()
    expected_keys = ["id", "title", "content", "created_at", "author", "author_id"]
    assert response.status_code == 201
    assert all(key in posted_document for key in expected_keys)


def test_create_user():
    post_body = {"username": "testuser3", "password": "password"}
    response = client.post("/users", json=post_body)
    posted_document = response.json()
    expected_keys = ["id", "username", "password", "created_at"]
    assert response.status_code == 200
    assert all(key in posted_document for key in expected_keys)


def test_user_login():
    post_body = {"username": "testuser2", "password": "secret123"}
    response = client.post("/login", json=post_body)
    posted_document = response.json()[0]
    expected_keys = ["username", "id"]
    assert response.status_code == 200
    assert all(key in posted_document for key in expected_keys)


def test_user_login_incorrect_username():
    post_body = {"username": "Paul", "password": "password"}
    response = client.post("/login", json=post_body)
    posted_document = response.json()
    assert response.status_code == 404
    assert posted_document["detail"] == "User not found"


def test_user_login_incorrect_password():
    post_body = {"username": "testuser2", "password": "secret"}
    response = client.post("/login", json=post_body)
    posted_document = response.json()
    assert response.status_code == 401
    assert posted_document["detail"] == "Incorrect password"
