"""Manual email fallback used until per-platform API integrations exist."""
from backend.takedown.platforms.base import TakedownPlatform


class EmailFallback(TakedownPlatform):
    name = "email_fallback"

    async def submit(self, *, notice: str, source_url: str) -> dict:
        raise NotImplementedError
