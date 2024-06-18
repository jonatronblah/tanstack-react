from typing import AsyncIterator
from datetime import datetime
from fastapi import HTTPException

from app.db import AsyncSession
from app.models import Document, Collection, CollectionSchema


class CreateCollection:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, date: datetime, documents: list[int]) -> CollectionSchema:
        async with self.async_session.begin() as session:
            exist_documents = [
                d async for d in Document.read_by_ids(session, note_ids=documents)
            ]
            if len(exist_documents) != len(documents):
                raise HTTPException(status_code=404)
            collection = await Collection.create(session, date, exist_documents)
            return CollectionSchema.model_validate(collection)


class ReadAllCollection:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self) -> AsyncIterator[CollectionSchema]:
        async with self.async_session() as session:
            async for collection in Collection.read_all(
                session, include_documents=True
            ):
                yield CollectionSchema.model_validate(collection)


class ReadCollection:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, collection_id: int) -> CollectionSchema:
        async with self.async_session() as session:
            collection = await Collection.read_by_id(
                session, collection_id, include_documents=True
            )
            if not collection:
                raise HTTPException(status_code=404)
            return CollectionSchema.model_validate(collection)


class UpdateCollection:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(
        self, collection_id: int, date: str, documents: list[int]
    ) -> CollectionSchema:
        async with self.async_session.begin() as session:
            collection = await Collection.read_by_id(
                session, collection_id, include_documents=True
            )
            if not collection:
                raise HTTPException(status_code=404)

            exist_documents = [
                d async for d in Document.read_by_ids(session, document_ids=documents)
            ]
            if len(exist_documents) != len(documents):
                raise HTTPException(status_code=404)
            await collection.update(session, date, exist_documents)
            await session.refresh(collection)
            return CollectionSchema.model_validate(collection)


class DeleteCollection:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, collection_id: int) -> None:
        async with self.async_session.begin() as session:
            collection = await Collection.read_by_id(session, collection_id)
            if not collection:
                return
            await Collection.delete(session, collection)
