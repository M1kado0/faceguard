"""/audit — audit log viewer (filterable, exportable)."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def audit_page(request: Request):
    raise NotImplementedError
