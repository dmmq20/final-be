import os
import dotenv
import psycopg
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(BASE_DIR / ".env")


class PgDatabase():
    """PostgreSQL Database context manager"""

    def __init__(self) -> None:
        self.driver = psycopg

    def connect_to_database(self):
        return self.driver.connect(
            os.getenv("DATABASE_URL")
        )

    def __enter__(self):
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exception_type, exc_val, traceback):
        self.cursor.close()
        self.connection.close()


def create_tables():
    with PgDatabase() as db:
        db.cursor.execute(f"""CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            first_name VARCHAR(20),
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
        db.connection.commit()
        print("Tables are created successfully...")


def drop_tables():
    with PgDatabase() as db:
        db.cursor.execute(f"DROP TABLE IF EXISTS users CASCADE;")
        db.cursor.execute(f"DROP TABLE IF EXISTS documents CASCADE;")
        db.connection.commit()
        print("Tables are dropped...")


def insert_test_users():
    with PgDatabase() as db:
        users = [
            ("testuser", "john doe"), ("testuser2", "jane doe")]
        for user in users:
            db.cursor.execute(
                f"INSERT INTO users (username, first_name) VALUES (%s, %s)", user)
            db.connection.commit()


def insert_test_documents():
    with PgDatabase() as db:
        documents = [("my first doc", "hello world!")]
        for doc in documents:
            db.cursor.execute(
                f"INSERT INTO documents (title, content) VALUES (%s, %s)", doc)
            db.connection.commit()
