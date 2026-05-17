"""/users — user management; user detail never exposes embeddings."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def list_users(request: Request):
    raise NotImplementedError


@router.get("/{user_id}", response_class=HTMLResponse)
async def user_detail(request: Request, user_id: str):
    # Never render raw embeddings — they're biometric data.
    raise NotImplementedError
