from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.services import comments as service
from app.models import Comment

router = APIRouter(prefix='/documents')

@router.get('/{document_id}/comments')
async def get_comments_by_document(document_id: int) -> list[Comment]:
    return service.get_some(document_id)

@router.post("/{document_id}/comments", status_code=status.HTTP_201_CREATED)
async def post_comment(document_id: int, comment: Comment) -> Comment:
    return service.create(document_id, comment)