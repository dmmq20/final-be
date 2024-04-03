from fastapi import HTTPException, status
from app.db import init_db

from app.models import DocumentCollaboration, UserCollaboration


def document_row_to_model(row) -> DocumentCollaboration:
    id, document_id, user_id, username, avatar_url = row
    return DocumentCollaboration(id=id, document_id=document_id, user_id=user_id, username=username, avatar_url=avatar_url)

def user_row_to_model(row) -> UserCollaboration:
    id, document_id, user_id, title = row
    return UserCollaboration(id=id, document_id=document_id, user_id=user_id, title=title)


def get_collaborations_by_id(id):
    with init_db as db:
        db.cursor.execute(
            "SELECT collaborations.*, users.username FROM collaborations JOIN users ON collaborations.user_id = users.id WHERE collaborations.id = %s;", (id,))
        collaborations_data = db.cursor.fetchone()
        db.connection.commit()
    return document_row_to_model(collaborations_data)


def get_collaborations_by_document_id(document_id):
    with init_db as db:
        db.cursor.execute(
            "SELECT collaborations.*, users.username, users.avatar_url FROM collaborations JOIN users ON collaborations.user_id = users.id WHERE collaborations.document_id = %s;", (document_id,))
        collaborations_data = db.cursor.fetchall()
        db.connection.commit()
    return [document_row_to_model(collaboration) for collaboration in collaborations_data]


def post_collaborations(document_id, collaboration: DocumentCollaboration) -> DocumentCollaboration:
    data = collaboration.model_dump()
    with init_db as db:
        query = "INSERT INTO collaborations (document_id, user_id) VALUES (%s, %s) RETURNING *;"
        params = (document_id, data["user_id"])
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_collaboration = get_collaborations_by_id(inserted_id)
        return new_collaboration


def get_collaborations_by_user_id(user_id):
    with init_db as db:
        db.cursor.execute(
            "SELECT collaborations.*, documents.title FROM collaborations JOIN documents ON collaborations.document_id = documents.id WHERE collaborations.user_id = %s;", (
                user_id,))
        collaborations_data = db.cursor.fetchall()
        print(collaborations_data)
        db.connection.commit()
    return [user_row_to_model(collaboration) for collaboration in collaborations_data]
