"""ML test fixtures. Only synthetic images in this repo — never real biometric data."""
import pytest


@pytest.fixture
def dummy_face_bytes() -> bytes:
    # TODO: synthesize a small RGB image of approximately face shape.
    return b""
