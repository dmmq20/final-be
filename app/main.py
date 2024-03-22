from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from app.api import get_user_by_ID, get_all_users

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Welcome to news app!'}


@app.get('/users')
def get_users():
    return get_all_users()


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return get_user_by_ID(user_id)


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
