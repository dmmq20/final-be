from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from app.api import get_user_by_ID, get_all_users, get_all_documents, insert_document, get_document_by_ID
from .models import User, Document

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Welcome to the app!'}


@app.get('/users')
def get_users():
    return get_all_users()


@app.get('/users/{user_id}')
def get_user(user_id: int):
    try:
        return get_user_by_ID(user_id)
    except HTTPException as e:
        return {"msg": e.detail, "status": e.status_code}


@app.get('/documents')
def get_documents():
    return get_all_documents()


@app.get('/documents/{document_id}')
def get_document(document_id: int):
    return get_document_by_ID(document_id)


@app.post('/documents')
def post_document(document: Document):
    return insert_document(document)
