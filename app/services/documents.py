from app.models import Document, OwnerDocument
from app.crud import documents as service


def get_all() -> list[Document]:
    return service.get_all_documents()


def get_one(id) -> Document:
    return service.get_document_by_ID(id)


def create(document) -> Document:
    return service.insert_document(document)

def get_some(user_id) -> list[OwnerDocument]:
    return service.get_documents_by_user_id(user_id)