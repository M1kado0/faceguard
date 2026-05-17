"""Stripe webhook handler — POST /v1/webhooks/stripe."""

from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/stripe")
async def stripe_webhook(request: Request) -> dict[str, str]:
    # Verify signature with STRIPE_WEBHOOK_SECRET, then dispatch by event type.
    raise NotImplementedError
