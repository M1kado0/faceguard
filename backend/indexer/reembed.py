"""Re-embedding pipeline used when promoting a new embedding model.

Heavy job — at 1000 img/sec a 100M index takes ~28h of GPU.
Plan dual-write window before flipping the read path to the new model version.
"""


async def reembed_all(*, from_version: str, to_version: str, batch_size: int = 256) -> None:
    raise NotImplementedError
