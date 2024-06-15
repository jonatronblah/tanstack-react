from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator

from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from pgvector.sqlalchemy import Vector

from .base import Base

if TYPE_CHECKING:
    from .docs import Doc


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    embedding = mapped_column(Vector(384))

    upload_filename: Mapped[str] = mapped_column("upload_filename", String(length=64), nullable=False)

    user_filename: Mapped[str] = mapped_column("user_filename", String(length=64), nullable=False)

    doc_text: Mapped[str] = mapped_column("doc_text", String(length=64), nullable=False)

    @classmethod
    async def create(cls, session: AsyncSession, title: str, notes: list[Doc]) -> Document:
        document = Document(
            title=title,
            notes=notes,
        )
        session.add(document)
        await session.flush()
        # To fetch notes
        new = await cls.read_by_id(session, document.id, include_notes=True)
        if not new:
            raise RuntimeError()
        return new

    # @classmethod
    # async def read_all(cls, session: AsyncSession, include_notes: bool) -> AsyncIterator[Document]:
    #     stmt = select(cls)
    #     if include_notes:
    #         stmt = stmt.options(selectinload(cls.notes))
    #     stream = await session.stream_scalars(stmt.order_by(cls.id))
    #     async for row in stream:
    #         yield row

    # @classmethod
    # async def read_by_id(
    #     cls, session: AsyncSession, document_id: int, include_notes: bool = False
    # ) -> Document | None:
    #     stmt = select(cls).where(cls.id == document_id)
    #     if include_notes:
    #         stmt = stmt.options(selectinload(cls.notes))
    #     return await session.scalar(stmt.order_by(cls.id))



    # async def update(self, session: AsyncSession, title: str, notes: list[Doc]) -> None:
    #     self.title = title
    #     self.notes = notes
    #     await session.flush()

    # @classmethod
    # async def delete(cls, session: AsyncSession, document: Document) -> None:
    #     await session.delete(document)
    #     await session.flush()