# summarizer/services/summarization_service.py

from summarizer.services.model_loader import ModelLoader

class SummarizationService:
    """
    High-level summarization service used by views or tasks.
    """

    def __init__(self):
        self.model = ModelLoader().get_model()

    def summarize_text(self, text: str) -> str:
        return self.model.summarize(text)
