"""/takedowns — list + detail."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/takedowns", response_class=HTMLResponse)
async def takedowns_list(request: Request):
    raise NotImplementedError


@router.get("/takedowns/{takedown_id}", response_class=HTMLResponse)
async def takedown_detail(request: Request, takedown_id: str):
    raise NotImplementedError
