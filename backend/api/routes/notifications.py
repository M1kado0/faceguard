"""Notification settings + user-configured webhooks."""
from fastapi import APIRouter, Depends

from backend.api.dependencies import get_current_user

router = APIRouter()


@router.get("/settings")
async def get_notification_settings(user=Depends(get_current_user)) -> dict:
    raise NotImplementedError


@router.patch("/settings")
async def update_notification_settings(user=Depends(get_current_user)) -> dict:
    raise NotImplementedError


@router.post("/webhooks")
async def register_webhook(user=Depends(get_current_user)) -> dict:
    raise NotImplementedError
