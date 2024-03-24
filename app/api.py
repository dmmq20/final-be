from app.database import PgDatabase
from fastapi import HTTPException, status
from .models import Document, User


def get_user_by_ID(id):
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user_data = db.cursor.fetchone()
        db.connection.commit()
        if user_data:
            id, username, first_name, created_at = user_data
            user = User(id=id, username=username,
                        first_name=first_name, created_at=created_at)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


def get_all_users():
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM users;")
        users_data = db.cursor.fetchall()
        db.connection.commit()
        if users_data:
            # since first_name is optional it may not always exist - need to handle
            users = [User(id=id, username=username, first_name=first_name, created_at=created_at)
                     for id, username, first_name, created_at in users_data]
            return users
        return None


def get_all_documents():
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM documents;")
        doc_data = db.cursor.fetchall()
        documents = [Document(id=id, title=title, content=content,
                              created_at=created_at) for id, title, content, created_at in doc_data]
        db.connection.commit()
    return documents


def get_document_by_ID(id):
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM documents WHERE id = %s", (id,))
        document_data = db.cursor.fetchone()
        db.connection.commit()
    if document_data:
        id, title, content, created_at = document_data
        doc = Document(id=id, title=title, content=content,
                       created_at=created_at)
        return doc
    else:
        pass  # todo: handle non-existant id


def insert_document(document: Document) -> Document:
    data = document.model_dump()
    with PgDatabase() as db:
        query = "INSERT INTO documents (title, content) VALUES (%s, %s) RETURNING *;"
        params = (data["title"], data["content"])
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_document = get_document_by_ID(inserted_id)
        return new_document
