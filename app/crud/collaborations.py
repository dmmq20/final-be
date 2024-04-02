from fastapi import HTTPException, status
from app.db import init_db

from app.models import Collaboration


def row_to_model(row) -> Collaboration:
    id, document_id, user_id, username = row
    return Collaboration(id=id, document_id=document_id, user_id=user_id, username=username)


def get_collaborations_by_document_id(document_id):
    with init_db as db:
        db.cursor.execute(
            "SELECT collaborations.*, users.username FROM collaborations JOIN users ON collaborations.user_id = users.id WHERE collaborations.document_id = %s;", (document_id,))
        collaborations_data = db.cursor.fetchall()
        print(collaborations_data)
        db.connection.commit()
    return [row_to_model(collaboration) for collaboration in collaborations_data]
