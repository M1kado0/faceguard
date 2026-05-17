"""Admin-only routes (RBAC: role in {admin, moderator})."""

from fastapi import APIRouter, Depends

from backend.api.dependencies import require_admin

router = APIRouter(dependencies=[Depends(require_admin)])

# TODO: mount admin sub-routers (users, audit, crawler, clusters, models).
