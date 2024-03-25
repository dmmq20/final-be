from . import init_db


def create_tables():
    with init_db as db:
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
    with init_db as db:
        db.cursor.execute(f"DROP TABLE IF EXISTS users CASCADE;")
        db.cursor.execute(f"DROP TABLE IF EXISTS documents CASCADE;")
        db.connection.commit()
        print("Tables are dropped...")


def insert_test_users():
    with init_db as db:
        users = [
            ("testuser", "john doe"), ("testuser2", "jane doe")]
        for user in users:
            db.cursor.execute(
                f"INSERT INTO users (username, first_name) VALUES (%s, %s)", user)
            db.connection.commit()


def insert_test_documents():
    with init_db as db:
        documents = [("my first doc", "hello world!"), ["my second doc", "some useful information"]]
        for doc in documents:
            db.cursor.execute(
                f"INSERT INTO documents (title, content) VALUES (%s, %s)", doc)
            db.connection.commit()
