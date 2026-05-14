"""LivenessChecker interface."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class LivenessResult:
    passed: bool
    score: float
    reason: str | None = None
    challenge_completed: bool | None = None


class LivenessChecker(Protocol):
    def check(self, blob: bytes) -> LivenessResult: ...
