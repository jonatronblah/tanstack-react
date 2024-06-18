from pydantic import BaseModel, ConfigDict
from datetime import date
from pgvector.sqlalchemy import Vector


class DocumentSchema(BaseModel):
    id: int
    embedding: Vector
    doc_text: str
    collection_id: int
    # collection_filename: str

    model_config = ConfigDict(from_attributes=True)


class CollectionSchema(BaseModel):
    id: int
    date: date
    documents: list[DocumentSchema]

    model_config = ConfigDict(from_attributes=True)
