"""Send email / webhook alerts when new matches are found."""


async def notify_email(user_id: str, matches: list[dict]) -> None:
    raise NotImplementedError


async def notify_webhook(user_id: str, matches: list[dict]) -> None:
    raise NotImplementedError
