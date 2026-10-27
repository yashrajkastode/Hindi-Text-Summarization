# Hindi Text Summarization System 🇮🇳

A backend-focused Hindi text summarization system built with Python, Django REST Framework, and transformer-based NLP. The project aims to provide a REST API for generating concise summaries of Hindi news articles and long-form text.

The architecture separates API handling, model inference, and asynchronous task processing to support maintainability and future extension.

## ✨ Features

- Abstractive text summarization for Hindi text
- Transformer-based multilingual model: `google/mt5-base`
- REST API using Django REST Framework
- Separate summarization service for model inference
- Celery integration for asynchronous processing
- Docker-based deployment configuration
- Gunicorn support for serving the Django application
- Extensible design for experimenting with other Indic-language models

> **Project status:** Verify the current implementation of each feature before treating it as production-ready. In particular, asynchronous processing, containerized deployment, and model quality should be tested in the target environment.

## 🧠 Model and Approach

| Component | Details |
|---|---|
| Model | `google/mt5-base` |
| Architecture | Multilingual encoder–decoder Transformer |
| Task | Abstractive text summarization |
| Fine-tuning | No fine-tuning claimed in the current implementation |
| Inference | Model-based text generation |

**Important:** mT5 is a general-purpose multilingual text-to-text model. Its summarization performance depends on the input, prompting or task formulation, decoding configuration, and whether the model has been trained for the target task. Hindi summarization quality should be evaluated on representative examples.

## 🏗️ System Architecture

```text
Client
  |
  v
Django REST Framework API
  |
  v
Summarization Service
  |
  v
mT5 Model Inference
  |
  v
Generated Summary
```

Optional asynchronous processing flow, when configured:

```text
Client
  |
  v
Django REST API
  |
  v
Celery Task Queue <----> Redis
  |
  v
Summarization Worker
  |
  v
Model Inference
```

Gunicorn can serve the Django application in a production-style deployment. The API, task queue, and model worker should be configured and tested according to the deployment environment.

## 📁 Repository Structure

```text
Hindi-Text-Summarization/
├── backend/       # Django backend and ML services
├── frontend/      # Optional frontend, if implemented
├── docker/        # Container configuration
├── scripts/       # Model download or warmup scripts
└── README.md
```

The directory descriptions above are intended to reflect the project layout. Update them if the actual repository structure differs.

## 🚀 Getting Started

### Prerequisites

- Python version supported by the project dependencies
- pip and a virtual environment
- Git
- Additional services such as Redis and Docker, if required by the selected configuration

### Setup

Clone the repository:

```bash
git clone https://github.com/yashrajkastode/Hindi-Text-Summarization.git
cd Hindi-Text-Summarization
```

Continue with the backend-specific installation and configuration instructions:

**[Backend README](backend/README.md)**

Follow the documented instructions to configure environment variables, install dependencies, load the model, start the API, and run any required background services.

## 🧪 Potential Use Cases

- Summarizing Hindi news articles
- Condensing long-form Hindi text
- Experimenting with multilingual transformer models
- Demonstrating the integration of NLP inference with a Django REST API
- Exploring asynchronous processing for ML workloads

## 🔬 Evaluation and Future Improvements

Potential improvements include:

- Evaluate summary quality on a representative Hindi dataset
- Compare generated summaries against reference summaries using suitable metrics, such as ROUGE
- Inspect factual consistency, important information retention, and grammatical quality
- Benchmark inference latency and memory consumption
- Add API validation, error handling, and automated tests
- Measure the performance difference between synchronous and asynchronous inference
- Compare mT5 with Hindi-capable Indic-language models

Only publish evaluation scores and performance claims after running the corresponding experiments.

## 🛠️ Technology Stack

- **Language:** Python
- **Backend:** Django, Django REST Framework
- **NLP:** Hugging Face Transformers, mT5
- **Task Processing:** Celery, Redis (if configured)
- **Deployment:** Docker, Gunicorn (if configured)

## 📌 Project Focus

This project explores the engineering involved in integrating transformer-based NLP inference with a Python web backend. Its design emphasizes separation of concerns, API integration, and extensibility for further experiments in Hindi and Indic-language summarization.

---

**Author:** [Yashraj Kastode](https://github.com/yashrajkastode)
