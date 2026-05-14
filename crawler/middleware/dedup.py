"""URL dedup against Redis (cheap layer; pHash dedup happens in the pipeline)."""


class DedupMiddleware:
    def process_request(self, request, spider):
        # Skip if URL was crawled within RECRAWL_INTERVAL_DAYS.
        raise NotImplementedError
