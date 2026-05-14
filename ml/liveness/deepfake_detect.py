"""Deepfake detector — binary classifier run on both passive and active inputs."""


class DeepfakeDetector:
    def __init__(self, model_path: str):
        self.model_path = model_path

    def predict(self, image) -> float:
        """Return p(deepfake) in [0, 1]."""
        raise NotImplementedError
