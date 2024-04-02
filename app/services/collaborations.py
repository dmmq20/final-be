from app.models import DocumentCollaboration, UserCollaboration
from app.crud import collaborations as service


def document_get_some(document_id) -> list[DocumentCollaboration]:
    return service.get_collaborations_by_document_id(document_id)

def user_get_some(user_id) -> list[UserCollaboration]:
    return service.get_collaborations_by_user_id(user_id)

def create(document_id, collaboration) -> DocumentCollaboration:
    return service.post_collaborations(document_id, collaboration)
