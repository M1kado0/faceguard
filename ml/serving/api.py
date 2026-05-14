"""Thin HTTP wrapper for the non-Triton serving path (port 8003).

Selected by INFERENCE_BACKEND=ray. For triton, requests go straight to Triton.
"""
from fastapi import FastAPI, UploadFile

app = FastAPI(title="FaceGuard ML Service", version="0.1.0")


@app.post("/v1/detect")
async def detect(image: UploadFile) -> dict:
    raise NotImplementedError


@app.post("/v1/embed")
async def embed(image: UploadFile) -> dict:
    raise NotImplementedError


@app.post("/v1/liveness/passive")
async def liveness_passive(blob: UploadFile) -> dict:
    raise NotImplementedError


@app.post("/v1/liveness/active")
async def liveness_active(blob: UploadFile, challenge: str) -> dict:
    raise NotImplementedError


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}
