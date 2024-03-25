from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from .api import get_user_by_ID, get_all_users, get_all_documents, insert_document, get_document_by_ID
from .models import User, Document

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Welcome to the app!'}


@app.get('/users')
async def get_users() -> list[User]:
    return get_all_users()


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    try:
        return get_user_by_ID(user_id)
    except HTTPException as e:
        return {"msg": e.detail, "status": e.status_code}


@app.get('/documents')
async def get_documents() -> list[Document]:
    return get_all_documents()


@app.get('/documents/{document_id}')
async def get_document(document_id: int) -> Document:
    return get_document_by_ID(document_id)


@app.post('/documents', status_code=status.HTTP_201_CREATED)
async def post_document(document: Document) -> Document:
    return insert_document(document)
