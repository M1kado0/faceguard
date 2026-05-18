"""Crawler test fixtures."""
import pytest


@pytest.fixture
def fake_html() -> str:
    return '<html><body><img src="/face.jpg"></body></html>'
