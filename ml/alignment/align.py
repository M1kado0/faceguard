"""5-point landmark alignment via similarity transform.

Output: 112x112 aligned face crop ready for ArcFace/AdaFace.
"""
from __future__ import annotations

import numpy as np


def align_face(image: np.ndarray, landmarks: np.ndarray, output_size: int = 112) -> np.ndarray:
    """Warp `image` so the 5 landmarks match the standard template."""
    raise NotImplementedError
