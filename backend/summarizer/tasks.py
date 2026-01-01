# summarizer/tasks.py

from celery import shared_task
from summarizer.services.summarization_service import SummarizationService
from summarizer.services.preprocessing import preprocess_text

@shared_task(bind=True)
def summarize_text_task(self, text: str) -> str:
    service = SummarizationService()
    cleaned = preprocess_text(text)
    return service.summarize_text(cleaned)
