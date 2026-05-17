"""Notification settings + user-configured webhooks."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from backend.api.dependencies import get_current_user
from backend.db.models.user import User

router = APIRouter()


@router.get("/settings")
async def get_notification_settings(
    user: Annotated[User, Depends(get_current_user)],
) -> dict:
    raise NotImplementedError


@router.patch("/settings")
async def update_notification_settings(
    user: Annotated[User, Depends(get_current_user)],
) -> dict:
    raise NotImplementedError


@router.post("/webhooks")
async def register_webhook(
    user: Annotated[User, Depends(get_current_user)],
) -> dict:
    raise NotImplementedError
