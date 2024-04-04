from .db import init_db
from fastapi import HTTPException, status
from .utils import verify_password


def login_user(user):
    user = user.model_dump()
    username = user["username"]
    password = user["password"]
    avatar_url = user["avatar_url"]
    with init_db as db:
        query = "SELECT id, username, password, avatar_url FROM users WHERE username = %s;"
        db.cursor.execute(query, (username,))
        user_data = db.cursor.fetchone()
        db.connection.commit()
    if user_data:
        id, user_username, stored_pw, avatar_url = user_data
        if verify_password(stored_pw, password):
            return {"username": user_username, "id": id, "avatar_url": avatar_url}, status.HTTP_200_OK
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
