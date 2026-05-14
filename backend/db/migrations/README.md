# Alembic migrations

```bash
# Generate a new migration after editing models/
uv run alembic revision --autogenerate -m "describe change"

# Apply migrations
uv run alembic upgrade head
```

Initialize alembic here (`alembic init .`) once the DB is wired up.
