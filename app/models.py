from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int | None
    username: str
    first_name: str | None
    created_at: datetime | None


class Document(BaseModel):
    id: int | None = None
    title: str | None = None
    content: str
    created_at: datetime | None = None
