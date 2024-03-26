from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.services import documents as service
from app.models import Document

router = APIRouter(prefix='/documents')


@router.get('')
@router.get('/')
async def get_documents() -> list[Document]:
    return service.get_all()


@router.get('/{document_id}')
async def get_document(document_id: int) -> Document:
    return service.get_one(document_id)


@router.post('/', status_code=status.HTTP_201_CREATED)
@router.post('', status_code=status.HTTP_201_CREATED)
async def post_document(document: Document) -> Document:
    return service.create(document)
