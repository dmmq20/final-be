from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from app.api import get_user_by_ID, get_all_users, get_all_documents, insert_document
from .models import User, Document

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Welcome to the app!'}


@app.get('/users')
def get_users():
    return {"users": get_all_users()}


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return get_user_by_ID(user_id)


@app.get('/documents')
def get_documents():
    return get_all_documents()

@app.post('/documents')
def post_document(document: Document):
    return insert_document(document)

# @app.post('/initdb')
# async def initdb():
#     try:
#         drop_tables()
#         create_tables()
#         insert_test_users()
#         insert_test_documents()
#         return {"message": "Tables dropped and created!"}
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f"Error {e}"
#         )
