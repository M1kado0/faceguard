"""Perceptual hash (DCT-based pHash)."""
from __future__ import annotations


def phash(image_bytes: bytes) -> str:
    """Return a hex string suitable for storage + Hamming-distance comparison."""
    raise NotImplementedError


def hamming(a: str, b: str) -> int:
    """Hamming distance between two pHash hex strings."""
    return bin(int(a, 16) ^ int(b, 16)).count("1")
