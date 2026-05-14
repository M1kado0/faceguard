"""POST /v1/takedown — request takedown for a match."""
from fastapi import APIRouter, Depends

from backend.api.dependencies import get_current_user
from backend.api.schemas import TakedownOut, TakedownRequest

router = APIRouter()


@router.post("/", response_model=TakedownOut)
async def request_takedown(
    payload: TakedownRequest,
    user=Depends(get_current_user),
) -> TakedownOut:
    # AUDIT: takedown.requested
    raise NotImplementedError


@router.get("/{takedown_id}", response_model=TakedownOut)
async def get_takedown(takedown_id: str, user=Depends(get_current_user)) -> TakedownOut:
    raise NotImplementedError
