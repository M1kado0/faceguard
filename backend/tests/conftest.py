"""Shared pytest fixtures for backend tests."""
import pytest


@pytest.fixture
def fake_user():
    return {"id": "test-user-1", "email": "test@example.com", "role": "user", "plan": "free"}
