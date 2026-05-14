"""SCRFD face detector (default). ONNX runtime — fast and accurate."""
from __future__ import annotations

import numpy as np

from ml.detection.base import Detection, FaceDetector


class SCRFDDetector(FaceDetector):
    def __init__(self, model_path: str):
        self.model_path = model_path
        # TODO: load ONNX session

    def detect(self, image: np.ndarray) -> list[Detection]:
        raise NotImplementedError

    def detect_batch(self, images: list[np.ndarray]) -> list[list[Detection]]:
        raise NotImplementedError
