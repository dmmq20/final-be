from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.services import documents as service
from app.models import Document, OwnerDocument, UpdatedDocument

router = APIRouter(prefix='/documents')
router_without_prefix = APIRouter()


@router.get('')
@router.get('/')
async def get_documents() -> list[Document]:
    return service.get_all()


@router.get('/{document_id}')
async def get_document(document_id: int) -> Document:
    try:
        return service.get_one(document_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router_without_prefix.get('/users/{user_id}/owned_documents')
async def get_user_documents(user_id: int) -> list[OwnerDocument]:
    return service.get_some(user_id)

@router.patch('/{document_id}')
async def patch_document_by_id(document_id:int , document: UpdatedDocument) -> Document:
    return service.update(document_id, document)


@router.post('/', status_code=status.HTTP_201_CREATED)
@router.post('', status_code=status.HTTP_201_CREATED)
async def post_document(document: Document) -> Document:
    return service.create(document)
