"""FaceEmbedder interface — output is 512-dim float32, L2-normalized."""
from __future__ import annotations

from typing import Protocol

import numpy as np


class FaceEmbedder(Protocol):
    version: str  # e.g. "arcface-r100-v2.1" — REQUIRED, embeddings filter by this.

    def embed(self, aligned_face: np.ndarray) -> np.ndarray: ...

    def embed_batch(self, aligned_faces: list[np.ndarray]) -> np.ndarray: ...
