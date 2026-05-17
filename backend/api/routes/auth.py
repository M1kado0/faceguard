"""POST /v1/auth/* — register, login, refresh, logout."""

from __future__ import annotations

import os
import uuid
from datetime import UTC, datetime, timedelta
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from passlib.hash import pbkdf2_sha256
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.schemas import LoginRequest, RegisterRequest, TokenPair
from backend.db.models.user import User
from backend.db.session import get_session

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET", "secret")

router = APIRouter()


def _issue_token_pair(user: User) -> TokenPair:
    expires_at = datetime.now(UTC) + timedelta(minutes=15)
    token = jwt.encode(
        {"sub": user.id, "role": user.role, "exp": expires_at},
        JWT_SECRET,
        algorithm="HS256",
    )
    return TokenPair(access_token=token, refresh_token=token)


@router.post("/register", response_model=TokenPair)
async def register(
    payload: RegisterRequest,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> TokenPair:
    result = await session.execute(select(User).where(User.email == payload.email))
    if result.scalar_one_or_none() is not None:
        raise HTTPException(status_code=409, detail="email_already_registered")

    user = User(
        id=str(uuid.uuid4()),
        email=str(payload.email),
        hashed_password=pbkdf2_sha256.hash(payload.password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return _issue_token_pair(user)


@router.post("/login", response_model=TokenPair)
async def login(
    payload: LoginRequest,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> TokenPair:
    result = await session.execute(select(User).where(User.email == payload.email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=401, detail="invalid_credentials")
    if not pbkdf2_sha256.verify(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="invalid_credentials")
    return _issue_token_pair(user)


@router.post("/refresh", response_model=TokenPair)
async def refresh(refresh_token: str) -> TokenPair:
    raise NotImplementedError


@router.post("/logout")
async def logout() -> dict[str, str]:
    raise NotImplementedError
