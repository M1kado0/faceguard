"""/settings — account settings + GDPR controls."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):
    raise NotImplementedError


# GDPR: right to portability
@router.get("/settings/export", response_class=HTMLResponse)
async def export_data(request: Request):
    raise NotImplementedError


# GDPR: right to erasure
@router.get("/settings/delete", response_class=HTMLResponse)
async def delete_account_page(request: Request):
    raise NotImplementedError


@router.post("/settings/delete", response_class=HTMLResponse)
async def delete_account(request: Request):
    raise NotImplementedError
