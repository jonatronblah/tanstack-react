from pydantic import Field
from pgvector.sqlalchemy import Vector

from app.models import DocumentSchema
from app.basemodel import BaseModel


class CreateDocumentRequest(BaseModel):
    embedding: Vector = Field(...)
    doc_text: str = Field("", min_length=0, max_length=5000)
    collection_id: int


class CreateDocumentResponse(DocumentSchema):
    pass


class ReadDocumentResponse(DocumentSchema):
    pass


class ReadAllDocumentResponse(BaseModel):
    documents: list[DocumentSchema]


class UpdateDocumentRequest(BaseModel):
    embedding: Vector = Field(...)
    doc_text: str = Field("", min_length=0, max_length=5000)
    collection_id: int


class UpdateDocumentResponse(DocumentSchema):
    pass
