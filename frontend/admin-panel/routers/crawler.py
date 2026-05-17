"""/crawler — spider health, throughput, blocklist management."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def crawler_page(request: Request):
    raise NotImplementedError


@router.get("/blocklist", response_class=HTMLResponse)
async def blocklist_page(request: Request):
    raise NotImplementedError
