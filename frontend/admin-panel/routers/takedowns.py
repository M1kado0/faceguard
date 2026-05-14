"""/takedowns — review pending takedown requests."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def takedowns_page(request: Request):
    raise NotImplementedError
