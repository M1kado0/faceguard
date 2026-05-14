"""Calibrate liveness thresholds against the eval set.

Targets: FAR < 0.1%, FRR < 5%. Run after any liveness model swap.

uv run python scripts/calibrate_liveness.py
"""


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
