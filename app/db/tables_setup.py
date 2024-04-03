from . import init_db
from app.utils import hash_password
from app.db.data.users import userData
from app.db.data.documents import documentData
from app.db.data.comments import commentData
from app.db.data.collaborations import collaborationData


def create_tables():
    with init_db as db:
        db.cursor.execute(f"""CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            avatar_url VARCHAR(255),
            created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)
        db.cursor.execute(f"""CREATE TABLE documents (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            content TEXT NOT NULL,
            author_id INTEGER REFERENCES users(id),
            author VARCHAR(50) REFERENCES users(username),
            created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)
        db.cursor.execute(f"""CREATE TABLE comments (
            id SERIAL PRIMARY KEY,
            author VARCHAR(50) REFERENCES users(username),
            document_id INTEGER REFERENCES documents(id),
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()             
            );
        """)
        db.cursor.execute(f"""CREATE TABLE collaborations (
            id SERIAL PRIMARY KEY,
            document_id INTEGER REFERENCES documents(id),
            user_id INT REFERENCES users(id)
        )""")
        db.connection.commit()
        print("Tables are created successfully...")


def drop_tables():
    with init_db as db:
        db.cursor.execute(f"DROP TABLE IF EXISTS users CASCADE;")
        db.cursor.execute(f"DROP TABLE IF EXISTS documents CASCADE;")
        db.cursor.execute(f"DROP TABLE IF EXISTS comments CASCADE;")
        db.cursor.execute(f"DROP TABLE IF EXISTS collaborations CASCADE;")
        db.connection.commit()
        print("Tables are dropped...")


def insert_test_users():
    with init_db as db:
        for user in userData:
            db.cursor.execute(
                f"INSERT INTO users (username, password, avatar_url) VALUES (%s, %s, %s)", user)
            db.connection.commit()


def insert_test_documents():
    with init_db as db:
        for doc in documentData:
            db.cursor.execute(
                f"INSERT INTO documents (title, content, author_id, author) VALUES (%s, %s, %s, %s)", doc)
            db.connection.commit()

def insert_test_comments():
    with init_db as db:
        for comment in commentData:
            db.cursor.execute(
                f"INSERT INTO comments (content, author, document_id) VALUES (%s, %s, %s)", comment)
            db.connection.commit()

def insert_test_collaborations():
    with init_db as db:
        for collaboration in collaborationData:
            db.cursor.execute(
                f"INSERT INTO collaborations (document_id, user_id) VALUES (%s, %s)", collaboration)
            db.connection.commit()