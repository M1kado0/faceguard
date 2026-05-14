"""Find new matches for enrolled users since the last monitoring pass."""


async def find_new_matches_for(user_id: str) -> list[dict]:
    """Return matches discovered since the user's last_notified_at watermark."""
    raise NotImplementedError
