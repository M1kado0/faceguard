"""ImageItem — emitted by spiders, processed by pipelines, queued to inference."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ImageItem:
    url: str
    source_page: str
    spider: str
    crawled_at: datetime
    phash: str | None = None
    s3_key: str | None = None
    content_type: str | None = None
    bytes_size: int | None = None
