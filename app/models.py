from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class User(BaseModel):
    id: Optional[int]
    username: str
    first_name: Optional[str]
    created_at: Optional[datetime]


class Document(BaseModel):
    id: Optional[int]
    title: Optional[str]
    content: str
    created_at: Optional[datetime]
