"""Per-route rate limiting (Redis-backed via slowapi)."""

from slowapi import Limiter
from slowapi.util import get_remote_address

# Backend URI is wired from settings at app startup.
limiter = Limiter(key_func=get_remote_address)

# Defaults documented in backend/CLAUDE.md:
# - Anonymous: 10 req/min per IP
# - Authenticated user: 60 req/min per account
# - Search (free): 20/hour per account; (paid): 200/hour
