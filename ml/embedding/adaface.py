"""AdaFace embedder — alternative to ArcFace. Swap via ADR."""

from __future__ import annotations

import numpy as np

from ml.embedding.base import FaceEmbedder


class AdaFaceEmbedder(FaceEmbedder):
    def __init__(self, model_path: str, version: str = "adaface-r100-v1"):
        self.model_path = model_path
        self.version = version

    def embed(self, aligned_face: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def embed_batch(self, aligned_faces: list[np.ndarray]) -> np.ndarray:
        raise NotImplementedError
