"""/analytics — dashboards."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def analytics_page(request: Request):
    raise NotImplementedError
