from pydantic import BaseModel, Field
from datetime import datetime
from app.models import CollectionSchema


class CreateCollectionRequest(BaseModel):
    date: datetime = Field(...)
    documents: list[int] = Field(min_length=0)


class CreateCollectionResponse(CollectionSchema):
    pass


class ReadCollectionResponse(CollectionSchema):
    pass


class ReadAllCollectionResponse(BaseModel):
    notebooks: list[CollectionSchema]


class UpdateCollectionRequest(BaseModel):
    date: datetime = Field(...)
    documents: list[int] = Field(min_length=0)


class UpdateCollectionResponse(CollectionSchema):
    pass
