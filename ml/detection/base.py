"""FaceDetector interface — every detection model implements this."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np


@dataclass
class Detection:
    bbox: tuple[float, float, float, float]  # x1, y1, x2, y2
    landmarks: np.ndarray  # 5 x 2 (eyes, nose, mouth corners)
    score: float


class FaceDetector(Protocol):
    def detect(self, image: np.ndarray) -> list[Detection]: ...

    def detect_batch(self, images: list[np.ndarray]) -> list[list[Detection]]: ...
