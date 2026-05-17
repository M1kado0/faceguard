"""Admin auth — separate session from public site to limit blast radius."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    raise NotImplementedError


@router.post("/login", response_class=HTMLResponse)
async def login(request: Request):
    raise NotImplementedError
