"""MiniFASNet v2 wrapper — backs the passive liveness check."""


class MiniFASNet:
    def __init__(self, model_path: str):
        self.model_path = model_path

    def predict(self, image) -> float:
        """Return spoof score in [0, 1]; higher = more likely real."""
        raise NotImplementedError
