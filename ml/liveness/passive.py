"""Passive liveness — single image or ~1s clip, no user action required.

Threshold: LIVENESS_THRESHOLD_PASSIVE (default 0.85). Fall back to active below threshold.
"""

import numpy as np

from ml.liveness.base import LivenessChecker, LivenessResult
from ml.liveness.minifasnet import MiniFASNet


class PassiveLivenessChecker(LivenessChecker):
    def __init__(self, model_path: str, threshold: float = 0.85):
        self.model_path = model_path
        self.threshold = threshold
        self.model = MiniFASNet(self.model_path)

    def check(self, image: np.ndarray, bbox_xyxy: list[float]) -> LivenessResult:
        result = self.model.predict(image, bbox_xyxy)
        passed = result["score"] >= self.threshold
        return LivenessResult(
            passed=passed,
            score=result["score"],
            label=result["model_label"],
            reason=None if passed else "liveness_score_below_threshold",
        )
