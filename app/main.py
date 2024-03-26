from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .api import get_user_by_ID, get_all_users, get_all_documents, insert_document, get_document_by_ID, insert_user, login_user
from .models import User, Document

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.post('/users', status_code=status.HTTP_200_OK)
async def create_user(user: User) -> User:
    return insert_user(user)


@app.get('/documents')
async def get_documents() -> list[Document]:
    return get_all_documents()


@app.get('/documents/{document_id}')
async def get_document(document_id: int) -> Document:
    return get_document_by_ID(document_id)


@app.post('/documents', status_code=status.HTTP_201_CREATED)
async def post_document(document: Document) -> Document:
    return insert_document(document)


@app.post('/login')
async def user_login(user: User):
    return login_user(user)