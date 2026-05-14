"""POST /v1/auth/* — register, login, refresh, logout."""
from fastapi import APIRouter

from backend.api.schemas import LoginRequest, RegisterRequest, TokenPair

router = APIRouter()


@router.post("/register", response_model=TokenPair)
async def register(payload: RegisterRequest) -> TokenPair:
    raise NotImplementedError


@router.post("/login", response_model=TokenPair)
async def login(payload: LoginRequest) -> TokenPair:
    raise NotImplementedError


@router.post("/refresh", response_model=TokenPair)
async def refresh(refresh_token: str) -> TokenPair:
    raise NotImplementedError


@router.post("/logout")
async def logout() -> dict[str, str]:
    raise NotImplementedError
