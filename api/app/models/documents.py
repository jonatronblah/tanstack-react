from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator

from sqlalchemy import ForeignKey, String, select
from sqlalchemy.ext.asyncio import AsyncSession

# from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, joinedload, mapped_column, relationship
from pgvector.sqlalchemy import Vector

if TYPE_CHECKING:
    from .collections import Collection

from .base import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    embedding: Mapped[Vector] = mapped_column("embedding", Vector(384))

    doc_text = mapped_column("doc_text", String())

    collection_id: Mapped[int] = mapped_column(
        "collection_id", ForeignKey("collection.id"), nullable=False
    )

    collection: Mapped[Collection] = relationship(
        "Collection", back_populates="documents"
    )

    # @hybrid_property
    # def collection_filename(self) -> str:
    #     return self.collection.filename

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[Document]:
        stmt = select(cls).options(joinedload(cls.collection, innerjoin=True))
        stream = await session.stream_scalars(stmt.order_by(cls.id))
        async for row in stream:
            yield row

    @classmethod
    async def read_by_id(
        cls, session: AsyncSession, document_id: int
    ) -> Document | None:
        stmt = (
            select(cls).where(cls.id == document_id).options(joinedload(cls.collection))
        )
        return await session.scalar(stmt.order_by(cls.id))

    @classmethod
    async def read_by_ids(
        cls, session: AsyncSession, document_ids: list[int]
    ) -> AsyncIterator[Document]:
        stmt = (
            select(cls)
            .where(cls.id.in_(document_ids))  # type: ignore
            .options(joinedload(cls.collection))
        )
        stream = await session.stream_scalars(stmt.order_by(cls.id))
        async for row in stream:
            yield row

    @classmethod
    async def create(
        cls, session: AsyncSession, collection_id: int, embedding, doc_text: str
    ) -> Document:
        document = Document(
            embedding=embedding, doc_text=doc_text, collection_id=collection_id
        )
        session.add(document)
        await session.flush()

        # To fetch collection
        new = await cls.read_by_id(session, document.id)
        if not new:
            raise RuntimeError()
        return new

    async def update(
        self, session: AsyncSession, collection_id: int, embedding, doc_text: str
    ) -> None:
        self.collection_id = collection_id
        self.embedding = embedding
        self.doc_text = doc_text
        await session.flush()

    @classmethod
    async def delete(cls, session: AsyncSession, document: Document) -> None:
        await session.delete(document)
        await session.flush()
