"""ArcFace (ResNet-100) embedder — default."""
from __future__ import annotations

import numpy as np

from ml.embedding.base import FaceEmbedder


class ArcFaceEmbedder(FaceEmbedder):
    def __init__(self, model_path: str, version: str = "arcface-r100-v1"):
        self.model_path = model_path
        self.version = version
        # TODO: load ONNX session

    def embed(self, aligned_face: np.ndarray) -> np.ndarray:
        # Must L2-normalize before returning.
        raise NotImplementedError

    def embed_batch(self, aligned_faces: list[np.ndarray]) -> np.ndarray:
        raise NotImplementedError
