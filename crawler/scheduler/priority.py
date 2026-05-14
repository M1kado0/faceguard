"""Priority queue for crawl scheduling.

Bands: high (1-7d), medium (7-30d), low (30-90d).
"""
from typing import Literal

Band = Literal["high", "medium", "low"]


def assign_priority(url: str, *, has_matches: bool, churn_score: float) -> Band:
    raise NotImplementedError
