from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.services import collaborations as service
from app.models import DocumentCollaboration, UserCollaboration

router = APIRouter(prefix='')

@router.get('/documents/{document_id}/collaborations')
async def get_collaborations_by_document(document_id: int) -> list[DocumentCollaboration]:
    return service.document_get_some(document_id)

@router.get('/users/{user_id}/collaborations')
async def get_collaborations_by_users(user_id: int) -> list[UserCollaboration]:
    return service.user_get_some(user_id)


@router.post('/documents/{document_id}/collaborations')
async def add_collaboration(document_id, collaboration: DocumentCollaboration) -> DocumentCollaboration:
    return service.create(document_id, collaboration)