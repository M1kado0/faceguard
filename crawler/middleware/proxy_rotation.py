"""Assign a fresh proxy per request from a rotating residential pool.

LEGAL: proxies are for distribution + reliability, never for evading per-site rate limits.
"""


class ProxyRotationMiddleware:
    def process_request(self, request, spider):
        raise NotImplementedError
