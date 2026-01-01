# scripts/warmup.py

from summarizer.services.summarization_service import SummarizationService

def main():
    service = SummarizationService()
    _ = service.summarize_text(
        "यह एक परीक्षण वाक्य है जिसका उद्देश्य मॉडल को सक्रिय करना है।"
    )
    print("Model warm-up complete.")

if __name__ == "__main__":
    main()
