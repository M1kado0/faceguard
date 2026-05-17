"""/enroll — add a face to be monitored (liveness REQUIRED)."""

from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/enroll", response_class=HTMLResponse)
async def enroll_page(request: Request):
    raise NotImplementedError


@router.post("/enroll", response_class=HTMLResponse)
async def enroll(request: Request, photo: UploadFile, liveness_blob: UploadFile):
    # 1. Liveness check FIRST (return partials/liveness_failed.html on fail).
    # 2. Forward to backend /v1/enroll via shared.api_client.
    # 3. Return partials/enroll_success.html.
    raise NotImplementedError
