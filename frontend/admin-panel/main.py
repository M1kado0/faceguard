"""Admin panel (port 8001). Deployed on a separate domain in prod."""
from pathlib import Path

import sys
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

sys.path.insert(0, str(Path(__file__).parent))

from routers import (  # noqa: E402
    analytics,
    audit,
    auth,
    clusters,
    crawler,
    models,
    takedowns,
    users,
)

app = FastAPI(title="FaceGuard — Admin Panel", version="0.1.0")

ROOT = Path(__file__).resolve().parent
SHARED = ROOT.parent / "shared"

app.mount("/static", StaticFiles(directory=SHARED / "static"), name="static")
templates = Jinja2Templates(directory=[ROOT / "templates", SHARED / "templates"])

app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(audit.router, prefix="/audit", tags=["audit"])
app.include_router(crawler.router, prefix="/crawler", tags=["crawler"])
app.include_router(models.router, prefix="/models", tags=["models"])
app.include_router(clusters.router, prefix="/clusters", tags=["clusters"])
app.include_router(takedowns.router, prefix="/takedowns", tags=["takedowns"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
