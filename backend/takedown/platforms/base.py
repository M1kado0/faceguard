"""Per-platform takedown integration interface."""

from typing import Protocol


class TakedownPlatform(Protocol):
    name: str

    async def submit(self, *, notice: str, source_url: str) -> dict:
        """Submit the notice; return the platform's reference id + status."""
        ...
