from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.services import collaborations as service
from app.models import Collaboration

router = APIRouter(prefix='/documents')

@router.get('/{document_id}/collaborations')
async def get_collaborations_by_document(document_id: int) -> list[Collaboration]:
    return service.get_some(document_id)

@router.post('/{document_id}/collaborations')
async def add_collaboration(document_id, collaboration: Collaboration) -> Collaboration:
    return service.create(document_id, collaboration)