# summarizer/services/preprocessing.py

import re

MAX_CHAR_LENGTH = 6000  # hard safety cap before tokenization

def preprocess_text(text: str) -> str:
    """
    Light preprocessing only.
    Avoid aggressive normalization to preserve semantic context.
    """

    if not text:
        return ""

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Safety cutoff (prevents OOM / abuse)
    if len(text) > MAX_CHAR_LENGTH:
        text = text[:MAX_CHAR_LENGTH]

    return text
