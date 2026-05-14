"""Append-only audit log writer. EVERY biometric op MUST call `log()`.

Schema (see backend/CLAUDE.md):
  id, timestamp, actor_id, actor_type, action, target_id, metadata, ip_address, user_agent
"""
from __future__ import annotations

from typing import Literal

ActorType = Literal["user", "admin", "system"]


# AUDIT: this is the sole writer; do not mark optional or skip on any biometric op.
async def log(
    *,
    actor_id: str,
    actor_type: ActorType,
    action: str,
    target_id: str | None = None,
    metadata: dict | None = None,
    ip_address: str | None = None,
    user_agent: str | None = None,
) -> None:
    raise NotImplementedError
