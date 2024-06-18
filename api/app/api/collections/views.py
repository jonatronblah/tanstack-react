from fastapi import APIRouter, Depends, Path, Request

from app.models import CollectionSchema

from .schema import (
    CreateCollectionRequest,
    CreateCollectionResponse,
    ReadAllCollectionResponse,
    ReadCollectionResponse,
    UpdateCollectionRequest,
    UpdateCollectionResponse,
)
from .use_cases import (
    CreateCollection,
    DeleteCollection,
    ReadAllCollection,
    ReadCollection,
    UpdateCollection,
)

router = APIRouter(prefix="/collections")


@router.post("", response_model=CreateCollectionResponse)
async def create(
    request: Request,
    data: CreateCollectionRequest,
    use_case: CreateCollection = Depends(CreateCollection),
) -> CollectionSchema:
    return await use_case.execute(data.date, data.documents)


@router.get("", response_model=ReadAllCollectionResponse)
async def read_all(
    request: Request, use_case: ReadAllCollection = Depends(ReadAllCollection)
) -> ReadAllCollectionResponse:
    return ReadAllCollectionResponse(collection=[cl async for cl in use_case.execute()])


@router.get(
    "/{collection_id}",
    response_model=ReadCollectionResponse,
)
async def read(
    request: Request,
    collection_id: int = Path(..., description=""),
    use_case: ReadCollection = Depends(ReadCollection),
) -> CollectionSchema:
    return await use_case.execute(collection_id)


@router.put(
    "/{collection_id}",
    response_model=UpdateCollectionResponse,
)
async def update(
    request: Request,
    data: UpdateCollectionRequest,
    collection_id: int = Path(..., description=""),
    use_case: UpdateCollection = Depends(UpdateCollection),
) -> CollectionSchema:
    return await use_case.execute(
        collection_id, date=data.date, documents=data.documents
    )


@router.delete("/{collection_id}", status_code=204)
async def delete(
    request: Request,
    collection_id: int = Path(..., description=""),
    use_case: DeleteCollection = Depends(DeleteCollection),
) -> None:
    await use_case.execute(collection_id)
