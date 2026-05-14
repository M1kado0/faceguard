"""Qdrant implementation of VectorStore."""
from __future__ import annotations

from backend.indexer.store import Match, VectorStore


class QdrantStore(VectorStore):
    async def add(self, *, image_id, embedding, metadata) -> None:
        raise NotImplementedError

    async def search(self, *, embedding, top_k, filter=None) -> list[Match]:
        raise NotImplementedError

    async def delete(self, *, image_id) -> None:
        raise NotImplementedError

    async def delete_by_user(self, *, user_id) -> int:
        raise NotImplementedError
