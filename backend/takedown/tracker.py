"""Track takedown status transitions: pending → sent → resolved | rejected."""
from typing import Literal

Status = Literal["pending", "sent", "resolved", "rejected"]


async def transition(takedown_id: str, to: Status, *, reason: str | None = None) -> None:
    # AUDIT: takedown.status_change
    raise NotImplementedError
