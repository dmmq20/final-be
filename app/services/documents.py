from app.models import Document
from app.crud import documents as service


def get_all() -> list[Document]:
    return service.get_all_documents()


def get_one(id) -> Document:
    return service.get_document_by_ID(id)


def create(document) -> Document:
    return service.insert_document(document)
