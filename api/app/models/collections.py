from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator

from sqlalchemy import String, Date, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload

from .base import Base

if TYPE_CHECKING:
    from .documents import Document


class Collection(Base):
    __tablename__ = "collections"

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    date: Mapped[str] = mapped_column("date", Date(), nullable=False)

    documents: Mapped[list[Document]] = relationship(
        "Document",
        back_populates="document",
        order_by="Document.id",
        cascade="save-update, merge, refresh-expire, expunge, delete, delete-orphan",
    )

    @classmethod
    async def read_all(
        cls, session: AsyncSession, include_documents: bool
    ) -> AsyncIterator[Collection]:
        stmt = select(cls)
        if include_documents:
            stmt = stmt.options(selectinload(cls.documents))
        stream = await session.stream_scalars(stmt.order_by(cls.id))
        async for row in stream:
            yield row

    @classmethod
    async def read_by_id(
        cls, session: AsyncSession, collection_id: int, include_documents: bool = False
    ) -> Document | None:
        stmt = select(cls).where(cls.id == collection_id)
        if include_documents:
            stmt = stmt.options(selectinload(cls.documents))
        return await session.scalar(stmt.order_by(cls.id))

    @classmethod
    async def create(
        cls, session: AsyncSession, date: Date, documents: list[Document]
    ) -> Document:
        document = Document(
            date=date,
            documents=documents,
        )
        session.add(document)
        await session.flush()
        # To fetch documents
        new = await cls.read_by_id(session, document.id, include_documents=True)
        if not new:
            raise RuntimeError()
        return new

    async def update(
        self, session: AsyncSession, date, documents: list[Document]
    ) -> None:
        self.date = date
        self.documents = documents
        await session.flush()

    @classmethod
    async def delete(cls, session: AsyncSession, collection: Collection) -> None:
        await session.delete(collection)
        await session.flush()
