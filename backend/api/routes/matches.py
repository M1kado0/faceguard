"""GET /v1/matches — list and read matches the user accumulated."""
from datetime import datetime

from fastapi import APIRouter, Depends

from backend.api.dependencies import get_current_user
from backend.api.schemas import Match

router = APIRouter()


@router.get("/", response_model=list[Match])
async def list_matches(
    since: datetime | None = None,
    user=Depends(get_current_user),
) -> list[Match]:
    raise NotImplementedError


@router.get("/{match_id}", response_model=Match)
async def get_match(match_id: str, user=Depends(get_current_user)) -> Match:
    raise NotImplementedError
