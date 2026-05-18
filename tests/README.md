# Cross-component integration tests

Tests here exercise multiple services together (backend ↔ ml ↔ crawler).
Per-component unit tests live under each service's `tests/` directory.

```bash
uv run pytest tests/
```
