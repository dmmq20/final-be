from fastapi import HTTPException, status
from app.db import init_db

from app.models import Comment


def row_to_model(row) -> Comment:
    id, author, document_id, content, created_at, avatar_url = row
    return Comment(id=id, author=author, document_id=document_id, content=content,
                   created_at=created_at, avatar_url=avatar_url)


def get_comment_by_id(id):
    with init_db as db:
        db.cursor.execute("SELECT * FROM comments WHERE id = %s", (id,))
        comment_data = db.cursor.fetchone()
        db.connection.commit()
    return row_to_model(comment_data)


def get_comments_by_document_id(document_id):
    with init_db as db:
        db.cursor.execute("""SELECT comments.*, users.avatar_url
        FROM comments
        JOIN users ON comments.author = users.username
        WHERE comments.document_id = %s;""", (document_id,))
        comment_data = db.cursor.fetchall()
        db.connection.commit()
    return [row_to_model(comment) for comment in comment_data]


def post_comment_by_document_id(document_id, comment: Comment) -> Comment:
    data = comment.model_dump()
    with init_db as db:
        query = "INSERT INTO comments (author, document_id, content) VALUES (%s, %s, %s) RETURNING *;"
        params = (data["author"], document_id, data["content"])
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_comment = get_comment_by_id(inserted_id)
        return new_comment


def delete_comment_by_id(comment_id):
    with init_db as db:
        db.cursor.execute(
            "DELETE FROM comments WHERE id = %s RETURNING *;", (comment_id,))
        db.connection.commit()
    return {"message": "comment successfully deleted"}
