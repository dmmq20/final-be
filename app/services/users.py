from app.models import User, Document
from app.crud import users as service


def get_all() -> list[User]:
    return service.get_all_users()


def get_one(id) -> User:
    return service.get_user_by_ID(id)


def create(user) -> User:
    return service.insert_user(user)

