"""/matches — match dashboard + detail."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/matches", response_class=HTMLResponse)
async def matches_list(request: Request):
    raise NotImplementedError


@router.get("/matches/{match_id}", response_class=HTMLResponse)
async def match_detail(request: Request, match_id: str):
    raise NotImplementedError
