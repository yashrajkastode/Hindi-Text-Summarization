import re
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from .config import (
    MODEL_NAME,
    MAX_INPUT_TOKENS,
    MAX_OUTPUT_TOKENS,
    NUM_BEAMS,
    LENGTH_PENALTY,
    EARLY_STOPPING,
    USE_FP16,
)

torch.backends.cudnn.benchmark = True


def clean_hindi_output(text: str) -> str:
    """
    Remove leading non-Devanagari characters that may leak
    from SentencePiece decoding (e.g., Kanji like '達').
    """
    match = re.search(r"[ऀ-ॿ]", text)
    return text[match.start():] if match else text


class IndicBartInference:
    """
    Production-grade IndicBART inference wrapper.
    Loaded once per worker (singleton via ModelLoader).
    """

    def __init__(self, device: torch.device):
        self.device = device

        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            use_fast=False
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            MODEL_NAME
        ).to(self.device)

        if USE_FP16 and self.device.type == "cuda":
            self.model = self.model.half()

        self.model.eval()

    @torch.inference_mode()
    def summarize(self, text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Input text is empty")

        prompt = f"summarize: {text}"

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=MAX_INPUT_TOKENS,
        )

        if "token_type_ids" in inputs:
            inputs.pop("token_type_ids")

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        generated_ids = self.model.generate(
            **inputs,
            max_length=MAX_OUTPUT_TOKENS,
            min_length=80,              # 🔴 force compression
            num_beams=6,
            length_penalty=1.8,         # 🔴 discourage copying
            repetition_penalty=1.2,     # 🔴 discourage verbatim output
            no_repeat_ngram_size=4,
            early_stopping=True,
        )

        decoded = self.tokenizer.decode(
            generated_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True,
        ).strip()

        decoded = re.sub(r"<extra_id_\d+>", "", decoded).strip()

        return decoded
