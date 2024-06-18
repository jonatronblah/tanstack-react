from typing import AsyncIterator
from pgvector.sqlalchemy import Vector

from fastapi import HTTPException

from app.db import AsyncSession
from app.models import Document, Collection, DocumentSchema


class CreateDocument:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(
        self, collection_id: int, doc_text: str, embedding: Vector
    ) -> DocumentSchema:
        async with self.async_session.begin() as session:
            collection = await Collection.read_by_id(session, collection_id)
            if not collection:
                raise HTTPException(status_code=404)
            document = await Document.create(
                session, collection.id, doc_text, embedding
            )
            return DocumentSchema.model_validate(document)


class ReadAllDocument:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self) -> AsyncIterator[DocumentSchema]:
        async with self.async_session() as session:
            async for doc in Document.read_all(session):
                yield DocumentSchema.model_validate(doc)


class ReadDocument:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, document_id: int) -> DocumentSchema:
        async with self.async_session() as session:
            document = await Document.read_by_id(session, document_id)
            if not document:
                raise HTTPException(status_code=404)
            return DocumentSchema.model_validate(document)


class UpdateDocument:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(
        self, document_id: int, collection_id: int, doc_text: str, embedding: Vector
    ) -> DocumentSchema:
        async with self.async_session.begin() as session:
            document = await Document.read_by_id(session, document_id)
            if not document:
                raise HTTPException(status_code=404)

            if document.collection_id != collection_id:
                collection = await Collection.read_by_id(session, collection_id)
                if not collection:
                    raise HTTPException(status_code=404)
                collection_id = collection.id
            else:
                collection__id_ = document.collection_id

            await document.update(session, collection__id_, doc_text, embedding)
            await session.refresh(document)
            return DocumentSchema.model_validate(document)


class DeleteDocument:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, document_id: int) -> None:
        async with self.async_session.begin() as session:
            document = await Document.read_by_id(session, document_id)
            if not document:
                return
            await Document.delete(session, document)
