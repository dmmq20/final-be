from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.web import documents, users, comments, collaborations

from app.api import login_user
from app.models import User

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
app.include_router(documents.router_without_prefix)
app.include_router(comments.router)
app.include_router(collaborations.router)


@app.get('/')
async def index():
    return {'message': 'Welcome to the app!'}


@app.post('/login')
async def user_login(user: User):
    return login_user(user)

if __name__ == "__main__":

    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
