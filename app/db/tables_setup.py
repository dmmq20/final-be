from . import init_db
from app.utils import hash_password


def create_tables():
    with init_db as db:
        db.cursor.execute(f"""CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)
        db.cursor.execute(f"""CREATE TABLE documents (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)
        db.cursor.execute(f"""Create Table comments (
            id SERIAL PRIMARY KEY,
            author INTEGER REFERENCES users(id),
            document_id INTEGER REFERENCES documents(id),
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()             
            );
        """)
        db.connection.commit()
        print("Tables are created successfully...")


def drop_tables():
    with init_db as db:
        db.cursor.execute(f"DROP TABLE IF EXISTS users CASCADE;")
        db.cursor.execute(f"DROP TABLE IF EXISTS documents CASCADE;")
        db.connection.commit()
        print("Tables are dropped...")


def insert_test_users():
    with init_db as db:
        users = [
            ("testuser", hash_password("password123")), ("testuser2", hash_password("secret123"))]
        for user in users:
            db.cursor.execute(
                f"INSERT INTO users (username, password) VALUES (%s, %s)", user)
            db.connection.commit()


def insert_test_documents():
    with init_db as db:
        documents = [("my first doc", "hello world!"), [
            "my second doc", "some useful information"]]
        for doc in documents:
            db.cursor.execute(
                f"INSERT INTO documents (title, content) VALUES (%s, %s)", doc)
            db.connection.commit()

def insert_test_comments():
    with init_db as db:
        comments = [("My first comment", 1, 2), ("my second comment", 2, 1)]
        for comment in comments:
            db.cursor.execute(
                f"INSERT INTO comments (content, author, document_id) VALUES (%s, %s, %s)", comment)
            db.connection.commit()
