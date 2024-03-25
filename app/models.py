from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int | None = None
    username: str
    password: str
    created_at: datetime | None = None


class Document(BaseModel):
    id: int | None = None
    title: str | None = None
    content: str
    created_at: datetime | None = None
