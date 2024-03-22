from app.database import PgDatabase


def format_response(cursor, data):
    columns = [col.name for col in cursor.description]
    return {column: value for column, value in zip(columns, data)}


def get_user_by_ID(id):
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user_data = db.cursor.fetchone()
        user_data = format_response(db.cursor, user_data)
        db.connection.commit()
    if user_data:
        return {"user": user_data}
    else:
        pass  # todo: handle non-existant id


def get_all_users():
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM users;")
        users_data = db.cursor.fetchall()
        users_dict = [format_response(db.cursor, user) for user in users_data]
        db.connection.commit()
    return {"users": users_dict}


def get_all_documents():
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM documents;")
        doc_data = db.cursor.fetchall()
        document_dict = [format_response(db.cursor, document)
                         for document in doc_data]
        db.connection.commit()
    return {"documents": document_dict}


def get_document_by_ID(id):
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM documents WHERE id = %s", (id,))
        document_data = db.cursor.fetchone()
        document_dict = format_response(db.cursor, document_data)
        db.connection.commit()
    if document_data:
        return {"document": document_dict}
    else:
        pass  # todo: handle non-existant id


def insert_document(document):
    data = dict(document)
    with PgDatabase() as db:
        db.cursor.execute(
            "INSERT INTO documents (title, content) VALUES (%s, %s) RETURNING *;", (data["title"], data["content"]))
        db.connection.commit()
        inserted_id = db.cursor.fetchone()[0]

        obj = get_document_by_ID(inserted_id)
    return obj
