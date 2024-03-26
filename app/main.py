from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .web import documents
from .web import users

from .api import login_user
from .models import User

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

app.include_router(users.router)
app.include_router(documents.router)


@app.get('/')
async def index():
    return {'message': 'Welcome to the app!'}


@app.post('/login')
async def user_login(user: User):
    return login_user(user)
