"""Consume re-crawl events from the monitor service and enqueue URLs."""


async def handle_recrawl_event(event: dict) -> None:
    raise NotImplementedError
