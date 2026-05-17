"""POST /v1/takedown — request takedown for a match."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from backend.api.dependencies import get_current_user
from backend.api.schemas import TakedownOut, TakedownRequest
from backend.db.models.user import User

router = APIRouter()


@router.post("/", response_model=TakedownOut)
async def request_takedown(
    payload: TakedownRequest,
    user: Annotated[User, Depends(get_current_user)],
) -> TakedownOut:
    # AUDIT: takedown.requested
    raise NotImplementedError


@router.get("/{takedown_id}", response_model=TakedownOut)
async def get_takedown(
    takedown_id: str,
    user: Annotated[User, Depends(get_current_user)],
) -> TakedownOut:
    raise NotImplementedError
