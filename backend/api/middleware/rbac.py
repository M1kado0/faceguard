"""Role-based access control middleware/dependencies."""
from fastapi import HTTPException


def require_role(*allowed: str):
    def _checker(user):
        if getattr(user, "role", None) not in allowed:
            raise HTTPException(status_code=403, detail="forbidden")
        return user
    return _checker
