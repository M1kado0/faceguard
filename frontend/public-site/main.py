"""Public site (port 8000) — end-user-facing FastAPI + Jinja2 + HTMX app."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Imported via direct path because the dir uses hyphens (not a Python package).
import sys
sys.path.insert(0, str(Path(__file__).parent))

from routers import auth, billing, enroll, matches, search, settings, takedowns  # noqa: E402

app = FastAPI(title="FaceGuard — Public Site", version="0.1.0")

ROOT = Path(__file__).resolve().parent
SHARED = ROOT.parent / "shared"

app.mount("/static", StaticFiles(directory=SHARED / "static"), name="static")

templates = Jinja2Templates(
    directory=[ROOT / "templates", SHARED / "templates"],
)

app.include_router(auth.router, tags=["auth"])
app.include_router(enroll.router, tags=["enroll"])
app.include_router(search.router, tags=["search"])
app.include_router(matches.router, tags=["matches"])
app.include_router(takedowns.router, tags=["takedowns"])
app.include_router(settings.router, tags=["settings"])
app.include_router(billing.router, tags=["billing"])
