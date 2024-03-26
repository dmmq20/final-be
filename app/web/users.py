from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.services import users as service
from app.models import User

router = APIRouter(prefix='/users')


@router.get('')
@router.get('/')
async def get_users() -> list[User]:
    return service.get_all()


@router.get('/{user_id}')
async def get_user(user_id: int):
    try:
        return service.get_one(user_id)
    except HTTPException as e:
        return {"msg": e.detail, "status": e.status_code}


@router.post('/', status_code=status.HTTP_200_OK)
@router.post('', status_code=status.HTTP_200_OK)
async def create_user(user: User) -> User:
    return service.create(user)
