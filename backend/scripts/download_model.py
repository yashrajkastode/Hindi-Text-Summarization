# scripts/download_model.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "ai4bharat/indicbart"

def main():
    AutoTokenizer.from_pretrained(MODEL_NAME)
    AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    print("IndicBART model downloaded successfully.")

if __name__ == "__main__":
    main()
