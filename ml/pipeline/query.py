"""End-to-end query path: image bytes → top-k matches.

Steps: liveness → detect → align → embed → ANN query.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class QueryResult:
    matches: list[dict]
    liveness_passed: bool
    liveness_score: float


async def query_image(image_bytes: bytes, *, liveness_blob: bytes, top_k: int = 50) -> QueryResult:
    raise NotImplementedError
