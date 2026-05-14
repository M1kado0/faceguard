"""POST /v1/enroll — enroll a face (liveness REQUIRED before embedding)."""
from fastapi import APIRouter, Depends, UploadFile

from backend.api.dependencies import get_current_user
from backend.api.schemas import EnrollResponse

router = APIRouter()


@router.post("/enroll", response_model=EnrollResponse)
async def enroll(
    photo: UploadFile,
    liveness_blob: UploadFile,
    user=Depends(get_current_user),
) -> EnrollResponse:
    # AUDIT: enroll.attempt
    # 1. Liveness check FIRST — reject before any embedding work.
    # 2. Detect + embed.
    # 3. Write to vector index via backend.indexer.
    # AUDIT: enroll.success | enroll.liveness_failed | enroll.no_face
    raise NotImplementedError


@router.get("/enrollments")
async def list_enrollments(user=Depends(get_current_user)) -> list[dict]:
    raise NotImplementedError


@router.delete("/enrollments/{enrollment_id}")
async def delete_enrollment(
    enrollment_id: str, user=Depends(get_current_user)
) -> dict[str, str]:
    # AUDIT: enroll.delete
    raise NotImplementedError
