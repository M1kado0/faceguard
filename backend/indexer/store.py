"""VectorStore protocol — every vector DB backend implements this."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np


@dataclass
class Match:
    image_id: str
    score: float
    metadata: dict


class VectorStore(Protocol):
    async def add(
        self,
        *,
        image_id: str,
        embedding: np.ndarray,
        metadata: dict,
    ) -> None: ...

    async def search(
        self,
        *,
        embedding: np.ndarray,
        top_k: int,
        filter: dict | None = None,
    ) -> list[Match]: ...

    async def delete(self, *, image_id: str) -> None: ...

    # GDPR: right-to-erasure entrypoint. Returns count of deleted vectors.
    async def delete_by_user(self, *, user_id: str) -> int: ...


def get_store() -> VectorStore:
    """Factory selecting the backend by VECTOR_DB_BACKEND env var."""
    raise NotImplementedError
