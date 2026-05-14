"""Download image bytes and put them in S3/MinIO."""


class ImageDownloadPipeline:
    def process_item(self, item, spider):
        # Fetch bytes, write to s3://S3_BUCKET_IMAGES/<key>, set item.s3_key.
        raise NotImplementedError
