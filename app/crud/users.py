from app.db import init_db
from fastapi import HTTPException, status
from app.models import User
from app.utils import hash_password


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
