"""Public site auth routes — /login, /register, /verify."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    raise NotImplementedError


@router.post("/login", response_class=HTMLResponse)
async def login(request: Request):
    raise NotImplementedError


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    raise NotImplementedError


@router.post("/register", response_class=HTMLResponse)
async def register(request: Request):
    raise NotImplementedError


@router.get("/verify", response_class=HTMLResponse)
async def verify(request: Request, token: str):
    raise NotImplementedError
