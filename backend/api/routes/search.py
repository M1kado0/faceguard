"""POST /v1/search — search by face (liveness REQUIRED)."""
from fastapi import APIRouter, Depends, UploadFile

from backend.api.dependencies import get_current_user
from backend.api.schemas import SearchResponse

router = APIRouter()


@router.post("/search", response_model=SearchResponse)
async def search(
    photo: UploadFile,
    liveness_blob: UploadFile,
    user=Depends(get_current_user),
) -> SearchResponse:
    # AUDIT: search.attempt
    # 1. Liveness check FIRST.
    # 2. Embed query face.
    # 3. ANN query via backend.indexer.
    # AUDIT: search.success | search.liveness_failed
    raise NotImplementedError
