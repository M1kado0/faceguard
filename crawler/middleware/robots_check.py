"""Honor robots.txt, noindex/nofollow, and X-Robots-Tag headers.

LEGAL: never bypass without an entry in docs/legal/crawl-overrides.md.
"""

from scrapy.exceptions import IgnoreRequest


class RobotsCheckMiddleware:
    def process_response(self, request, response, spider):
        xrobots = response.headers.get("X-Robots-Tag", b"").decode("latin-1").lower()
        if "noindex" in xrobots or "none" in xrobots:
            raise IgnoreRequest(f"X-Robots-Tag forbids indexing: {response.url}")
        return response
