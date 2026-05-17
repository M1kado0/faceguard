"""LivenessChecker interface."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np


@dataclass
class LivenessResult:
    passed: bool
    score: float
    label: str
    reason: str | None = None
    challenge_completed: bool | None = None


class LivenessChecker(Protocol):
    def check(self, image: np.ndarray, bbox_xyxy: list[float]) -> LivenessResult: ...
