"""/clusters — face cluster review (merge / split)."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def clusters_page(request: Request):
    raise NotImplementedError


@router.post("/merge", response_class=HTMLResponse)
async def merge_clusters(request: Request):
    raise NotImplementedError


@router.post("/split", response_class=HTMLResponse)
async def split_cluster(request: Request):
    raise NotImplementedError
