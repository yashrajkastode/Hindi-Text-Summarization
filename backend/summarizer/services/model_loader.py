# summarizer/services/model_loader.py

import torch
import threading
from ml.indicbart.inference import IndicBartInference

class ModelLoader:
    """
    Thread-safe singleton model loader.
    Ensures the model is loaded exactly once.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ModelLoader, cls).__new__(cls)
                    cls._instance._load_model()
        return cls._instance

    def _load_model(self):
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        self.model = IndicBartInference(self.device)

    def get_model(self) -> IndicBartInference:
        return self.model
