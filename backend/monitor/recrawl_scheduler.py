"""Decide which URLs the crawler should revisit and when.

Priority bands (from crawler/CLAUDE.md):
  high   — pages with matches for monitored users (1-7 days)
  medium — high-churn pages (7-30 days)
  low    — stable archive pages (30-90 days)

Emits re-crawl events to the crawler scheduler.
"""


async def schedule_recrawl_cycle() -> None:
    raise NotImplementedError
