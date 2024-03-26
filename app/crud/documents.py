from fastapi import HTTPException, status
from app.db import init_db

from app.models import Document


def row_to_model(row) -> Document:
    id, title, content, created_at = row
    return Document(id=id, title=title, content=content,
                    created_at=created_at)


def get_all_documents():
    with init_db as db:
        db.cursor.execute("SELECT * FROM documents;")
        doc_data = db.cursor.fetchall()
        db.connection.commit()
    return [row_to_model(doc) for doc in doc_data]


def get_document_by_ID(id):
    with init_db as db:
        db.cursor.execute("SELECT * FROM documents WHERE id = %s", (id,))
        document_data = db.cursor.fetchone()
        db.connection.commit()
        if document_data:
            return row_to_model(document_data)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")


def insert_document(document: Document) -> Document:
    data = document.model_dump()
    with init_db as db:
        query = "INSERT INTO documents (title, content) VALUES (%s, %s) RETURNING *;"
        params = (data["title"], data["content"])
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_document = get_document_by_ID(inserted_id)
        return new_document
