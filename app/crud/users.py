from app.db import init_db
from fastapi import HTTPException, status
from app.models import User
from app.utils import hash_password


def row_to_model(row) -> User:
    id, username, password, avatar_url, created_at = row
    return User(id=id, username=username,
                password=password, avatar_url=avatar_url, created_at=created_at)


def insert_user(user):
    user = user.model_dump()
    username = user["username"]
    password = user["password"]
    hashed_pw = hash_password(password)
    default_avatar_url = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png"
    with init_db as db:
        query = "INSERT INTO users (username, password, avatar_url) VALUES (%s, %s, %s) RETURNING *;"
        params = (username, hashed_pw, default_avatar_url)
        db.cursor.execute(query, params)
        inserted_id = db.cursor.fetchone()[0]
        db.connection.commit()
        new_user = get_user_by_ID(inserted_id)
        return new_user


def get_user_by_ID(id):
    with init_db as db:
        db.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user_data = db.cursor.fetchone()
        db.connection.commit()
        if user_data:
            return row_to_model(user_data)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


def get_all_users():
    with init_db as db:
        db.cursor.execute("SELECT * FROM users;")
        users_data = db.cursor.fetchall()
        db.connection.commit()
        if users_data:
            return [row_to_model(user) for user in users_data]
        return None

