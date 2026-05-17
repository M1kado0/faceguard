"""Queue consumer: pulls (image_id, embedding, metadata) and writes to the vector store."""

from __future__ import annotations

from backend.indexer.store import get_store


async def consume_one(message: dict) -> None:
    """Handle a single ingest message from the queue.

    Expected payload: {image_id, embedding, source_url, phash,
                       face_bbox, embedding_model_version}.
    Idempotent — re-processing the same image_id must not duplicate vectors.
    """
    store = get_store()
    await store.add(
        image_id=message["image_id"],
        embedding=message["embedding"],
        metadata={k: v for k, v in message.items() if k not in {"image_id", "embedding"}},
    )
