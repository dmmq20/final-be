from app.models import Collaboration
from app.crud import collaborations as service


def get_some(document_id) -> list[Collaboration]:
    return service.get_collaborations_by_document_id(document_id)


def create(document_id, collaboration) -> Collaboration:
    return service.post_collaborations(document_id, collaboration)