"""/billing — Stripe-backed plan management."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/billing", response_class=HTMLResponse)
async def billing_page(request: Request):
    raise NotImplementedError
