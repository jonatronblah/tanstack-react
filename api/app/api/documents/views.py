from fastapi import APIRouter, Depends, Path, Request
from pgvector.sqlalchemy import Vector

from app.models import DocumentSchema

from .schema import (
    CreateDocumentRequest,
    CreateDocumentResponse,
    ReadAllDocumentResponse,
    ReadDocumentResponse,
    UpdateDocumentRequest,
    UpdateDocumentResponse,
)
from .use_cases import (
    CreateDocument,
    DeleteDocument,
    ReadAllDocument,
    ReadDocument,
    UpdateDocument,
)

router = APIRouter(prefix="/documents")


@router.post("", response_model=CreateDocumentResponse)
async def create(
    request: Request,
    data: CreateDocumentRequest,
    use_case: CreateDocument = Depends(CreateDocument),
) -> DocumentSchema:
    return await use_case.execute(data.collection_id, data.embedding, data.doc_text)


@router.get("", response_model=ReadAllDocumentResponse)
async def read_all(
    request: Request,
    use_case: ReadAllDocument = Depends(ReadAllDocument),
) -> ReadAllDocumentResponse:
    return ReadAllDocumentResponse(
        documents=[document async for document in use_case.execute()]
    )


@router.get("/{document_id}", response_model=ReadDocumentResponse)
async def read(
    request: Request,
    document_id: int = Path(..., description=""),
    use_case: ReadDocument = Depends(ReadDocument),
) -> DocumentSchema:
    return await use_case.execute(document_id)


@router.put(
    "/{document_id}",
    response_model=UpdateDocumentResponse,
)
async def update(
    request: Request,
    data: UpdateDocumentRequest,
    document_id: int = Path(..., description=""),
    use_case: UpdateDocument = Depends(UpdateDocument),
) -> DocumentSchema:
    return await use_case.execute(
        document_id, data.collection_id, data.embedding, data.doc_text
    )


@router.delete("/{document_id}", status_code=204)
async def delete(
    request: Request,
    document_id: int = Path(..., description=""),
    use_case: DeleteDocument = Depends(DeleteDocument),
) -> None:
    await use_case.execute(document_id)
