"""Generate DMCA / GDPR / platform takedown notices from templates."""

from typing import Literal

NoticeType = Literal["dmca", "gdpr_erasure", "platform_tos"]


def render_notice(*, notice_type: NoticeType, match: dict, user: dict) -> str:
    """Render the body of a takedown notice for the given match + notice type."""
    raise NotImplementedError
