"""Per-domain rate limiting layered on top of Scrapy's AutoThrottle."""


class RateLimitMiddleware:
    def process_request(self, request, spider):
        raise NotImplementedError
