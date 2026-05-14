"""Compute perceptual hash (DCT-based pHash) for dedup."""


class PhashPipeline:
    def process_item(self, item, spider):
        # Compute pHash from the image bytes, store on item.phash.
        # If pHash already seen, drop the item (still update last_seen elsewhere).
        raise NotImplementedError
