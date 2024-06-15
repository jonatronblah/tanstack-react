from pydantic import BaseModel, ConfigDict
from pgvector.sqlalchemy import Vector



class DocSchema(BaseModel):
    id: int
    embedding: Vector
    content: str
    notebook_id: int
    notebook_title: str

    model_config = ConfigDict(from_attributes=True)
