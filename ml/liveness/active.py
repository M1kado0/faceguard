"""Active liveness — challenge/response (blink, turn, smile)."""

from typing import Literal

from ml.liveness.base import LivenessChecker, LivenessResult

Challenge = Literal["blink", "turn_left", "turn_right", "smile"]


class ActiveLivenessChecker(LivenessChecker):
    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold

    def issue_challenge(self) -> Challenge:
        raise NotImplementedError

    def check(self, blob: bytes) -> LivenessResult:
        # Verify challenge was performed AND the same face is present throughout.
        raise NotImplementedError
