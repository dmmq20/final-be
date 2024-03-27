from app.models import Comment
from app.crud import comments as service

def get_some(document_id) -> list[Comment]:
    return service.get_comments_by_document_id(document_id)

def create(document_id, comment) -> Comment:
    return service.post_comment_by_document_id(document_id, comment)