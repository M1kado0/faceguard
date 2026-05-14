"""/models — current model versions, trigger re-embedding."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def models_page(request: Request):
    raise NotImplementedError


@router.post("/promote", response_class=HTMLResponse)
async def promote_model(request: Request):
    raise NotImplementedError
