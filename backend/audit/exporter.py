"""GDPR data export — return every record we hold about a user."""


# GDPR: right to portability — every field a user has must be returned here.
async def export_user_data(user_id: str) -> dict:
    """Return all PII + embeddings + audit entries for the user as a dict."""
    raise NotImplementedError
