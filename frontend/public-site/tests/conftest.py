"""Public site test fixtures."""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    from main import app  # noqa: PLC0415
    return TestClient(app)
