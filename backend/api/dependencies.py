"""Shared FastAPI dependencies (current user, DB session, etc.)."""
from __future__ import annotations

from typing import Annotated

from fastapi import Depends, Header, HTTPException


async def get_current_user(authorization: Annotated[str | None, Header()] = None):
    """Resolve the current user from the Authorization: Bearer <jwt> header.

    TODO: implement JWT decode + lookup against users table.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="not_authenticated")
    raise NotImplementedError


async def require_admin(user=Depends(get_current_user)):
    """Gate admin-only routes."""
    if getattr(user, "role", None) not in {"admin", "moderator"}:
        raise HTTPException(status_code=403, detail="forbidden")
    return user
