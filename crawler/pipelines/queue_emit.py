"""Emit completed ImageItems to the inference queue (Kafka / Celery)."""


class QueueEmitPipeline:
    def process_item(self, item, spider):
        # Push {s3_key, source_url, phash, crawled_at} to the inference queue.
        raise NotImplementedError
