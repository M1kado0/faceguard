"""Online face clustering at index time.

Default cosine threshold: 0.65. Below → fragment; above → over-merge.
Calibrate via scripts/cluster_eval.py.
"""
import numpy as np


def assign_or_create(embedding: np.ndarray, *, threshold: float = 0.65) -> str:
    """Compare against existing centroids; return cluster_id."""
    raise NotImplementedError
