# ml/indicbart/config.py

MODEL_NAME = "google/mt5-base"
SOURCE_LANG = "hi_IN"
TARGET_LANG = "hi_IN"

MAX_INPUT_TOKENS = 1024
MAX_OUTPUT_TOKENS = 256

NUM_BEAMS = 4
LENGTH_PENALTY = 1.0
EARLY_STOPPING = True

USE_FP16 = True  # Enabled automatically if CUDA is available
