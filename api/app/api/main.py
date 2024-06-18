from fastapi import APIRouter

from .collections.views import router as collections_router
from .documents.views import router as documents_router

router = APIRouter()
router.include_router(documents_router)
router.include_router(collections_router)
