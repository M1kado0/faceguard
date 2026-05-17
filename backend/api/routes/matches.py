"""GET /v1/matches — list and read matches the user accumulated."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends

from backend.api.dependencies import get_current_user
from backend.api.schemas import Match
from backend.db.models.user import User

router = APIRouter()


@router.get("/", response_model=list[Match])
async def list_matches(
    user: Annotated[User, Depends(get_current_user)],
    since: datetime | None = None,
) -> list[Match]:
    raise NotImplementedError


@router.get("/{match_id}", response_model=Match)
async def get_match(
    match_id: str,
    user: Annotated[User, Depends(get_current_user)],
) -> Match:
    raise NotImplementedError
