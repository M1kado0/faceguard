"""/search — search for matches (liveness REQUIRED)."""
from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request):
    raise NotImplementedError


@router.post("/search", response_class=HTMLResponse)
async def search(request: Request, photo: UploadFile, liveness_blob: UploadFile):
    raise NotImplementedError
