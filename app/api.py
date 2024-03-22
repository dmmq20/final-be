from app.database import PgDatabase


def get_user_by_ID(id):
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user_data = db.cursor.fetchone()
        db.connection.commit()
    if user_data:
        return {"user": user_data}
    else:
        pass  # todo: handle non-existant id


def get_all_users():
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM users;")
        users_data = db.cursor.fetchall()
        db.connection.commit()
    return {"users": users_data}


def get_all_documents():
    with PgDatabase() as db:
        db.cursor.execute("SELECT * FROM documents;")
        doc_data = db.cursor.fetchall()
        print("HERE: ", doc_data)
        db.connection.commit()
    return {"documents": doc_data}
