from fastapi import HTTPException, status
from app.db import init_db

from app.models import Document, OwnerDocument, UpdatedDocument


def row_to_model(row) -> Document:
    id, title, content, author_id, author, created_at = row
    return Document(id=id, title=title, content=content, author_id=author_id, author=author,
                    created_at=created_at)


def owner_document_row_to_model(row) -> OwnerDocument:
    id, title, created_at = row
    return OwnerDocument(id=id, title=title,
                    created_at=created_at)


def get_all_documents():
    with init_db as db:
        db.cursor.execute("SELECT * FROM documents;")
        doc_data = db.cursor.fetchall()
        print(doc_data)
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
        query = "INSERT INTO documents (title, content, author_id, author) VALUES (%s, %s, %s, %s) RETURNING *;"
        params = (data["title"], data["content"],
                  data["author_id"], data["author"])
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_document = get_document_by_ID(inserted_id)
        return new_document


def get_documents_by_user_id(user_id):
    with init_db as db:
        db.cursor.execute(
            "SELECT documents.id, documents.title, documents.created_at FROM documents WHERE author_id = %s;", (user_id,))
        document_data = db.cursor.fetchall()
        db.connection.commit()
    return [owner_document_row_to_model(document) for document in document_data]

def update_document_by_id(document_id, document: UpdatedDocument) -> Document:
    data = document.model_dump()
    with init_db as db:
        query = "UPDATE documents SET title = %s, content = %s WHERE documents.id = %s;"
        params = (data["title"], data["content"], document_id)
        db.cursor.execute(query, params)
        db.connection.commit()
        updated_document = get_document_by_ID(document_id)
        return updated_document