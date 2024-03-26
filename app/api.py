from .db import init_db
from fastapi import HTTPException, status
from .models import Document, User
import bcrypt


def hash_password(password):
    hashed_password_bytes = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt())
    hashed_password_str = hashed_password_bytes.decode('utf-8')
    return hashed_password_str

def verify_password(hashed_password, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

def insert_user(user):
    user = user.model_dump()
    username = user["username"]
    password = user["password"]
    hashed_pw = hash_password(password)
    with init_db as db:
        query = "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING *;"
        params = (username, hashed_pw)
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_user = get_user_by_ID(inserted_id)
        return new_user


def login_user(user):
    user = user.model_dump()
    username = user["username"]
    password = user["password"]
    with init_db as db:
        query = "SELECT username, password FROM users WHERE username = %s;"
        db.cursor.execute(query, (username,))
        user_data = db.cursor.fetchone()
        db.connection.commit()
    if user_data:
        user_username, stored_pw = user_data
        if verify_password(stored_pw, password):
            return {"message": "Login successful", "username": user_username}, status.HTTP_200_OK
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


def get_user_by_ID(id):
    with init_db as db:
        db.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user_data = db.cursor.fetchone()
        db.connection.commit()
        if user_data:
            id, username, password, created_at = user_data
            user = User(id=id, username=username,
                        password=password, created_at=created_at)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


def get_all_users():
    with init_db as db:
        db.cursor.execute("SELECT * FROM users;")
        users_data = db.cursor.fetchall()
        db.connection.commit()
        if users_data:
            users = [User(id=id, username=username, password=password, created_at=created_at)
                     for id, username, password, created_at in users_data]
            return users
        return None


def get_all_documents():
    with init_db as db:
        db.cursor.execute("SELECT * FROM documents;")
        doc_data = db.cursor.fetchall()
        documents = [Document(id=id, title=title, content=content,
                              created_at=created_at) for id, title, content, created_at in doc_data]
        db.connection.commit()
    return documents


def get_document_by_ID(id):
    with init_db as db:
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
    with init_db as db:
        query = "INSERT INTO documents (title, content) VALUES (%s, %s) RETURNING *;"
        params = (data["title"], data["content"])
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_document = get_document_by_ID(inserted_id)
        return new_document
