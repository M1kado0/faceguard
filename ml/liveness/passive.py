"""Passive liveness — single image or ~1s clip, no user action required.

Threshold: LIVENESS_THRESHOLD_PASSIVE (default 0.85). Fall back to active below threshold.
"""
from ml.liveness.base import LivenessChecker, LivenessResult


class PassiveLivenessChecker(LivenessChecker):
    def __init__(self, model_path: str, threshold: float = 0.85):
        self.model_path = model_path
        self.threshold = threshold

    def check(self, blob: bytes) -> LivenessResult:
        raise NotImplementedError
