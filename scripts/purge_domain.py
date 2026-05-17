"""Remove all crawled content for a domain from storage + index.

uv run python scripts/purge_domain.py example.com
"""

import sys


def main(domain: str) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: purge_domain.py <domain>")
    main(sys.argv[1])
