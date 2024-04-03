from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int | None = None
    username: str
    password: str
    avatar_url: str = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png"
    created_at: datetime | None = None


class Document(BaseModel):
    id: int | None = None
    title: str | None = None
    content: str
    author_id: int
    author: str
    created_at: datetime | None = None

class UpdatedDocument(BaseModel):
    document_id: int | None = None
    content: str

class OwnerDocument(BaseModel):
    id: int | None = None
    title: str | None = None
    created_at: datetime | None = None

class Comment(BaseModel):
    id: int | None = None
    author: str | None = None
    document_id: int | None = None
    content: str
    created_at: datetime | None = None

class DocumentCollaboration(BaseModel):
    id: int | None = None
    document_id: int
    user_id: int
    username: str | None = None

class UserCollaboration(BaseModel):
    id: int | None = None
    document_id: int
    user_id: int
    title: str | None = None