# 🇮🇳 Hindi Text Summarization System

A full-stack Hindi text summarization application that explores abstractive text generation using transformer-based NLP models, a Django REST API, and a modern web frontend.

The project combines machine learning inference with backend API development and frontend integration, providing a foundation for experimenting with Hindi summarization and multilingual NLP.

## ✨ Features

- **Hindi text summarization** — designed for summarizing Hindi news articles and long-form text.
- **Transformer-based NLP** — integrates a multilingual text-to-text model for summary generation.
- **REST API** — Django REST Framework-based backend architecture.
- **Modular backend** — separates application configuration, summarization logic, and ML-related components.
- **Web frontend** — Vite-based frontend with a dedicated source directory and public assets.
- **Deployment configuration** — includes Docker-related files and Gunicorn configuration.
- **Extensible architecture** — structured to support future experimentation with other Hindi and Indic-language models.

*Feature availability depends on the current implementation and configuration. See the backend and frontend documentation for component-specific instructions.*

## 🧠 NLP Model

The project documentation identifies `google/mt5-base` as the intended summarization model.

| Component | Description |
|---|---|
| Model family | mT5 multilingual text-to-text Transformer |
| Target language | Hindi |
| Task | Abstractive text summarization |
| Integration | Python-based ML inference within the backend |

mT5 is a general-purpose multilingual model. Its ability to produce coherent and factually consistent Hindi summaries depends on the task formulation, model configuration, and any task-specific training or adaptation.

**Evaluation:** Summarization quality should be assessed using representative Hindi text and suitable evaluation methods before making claims about model accuracy or performance.

## 🏗️ Architecture

```text
                    User
                     |
                     v
              Web Frontend
             (Vite / JavaScript)
                     |
                     v
              Django REST API
                     |
                     v
            Summarization Service
                     |
                     v
              ML Inference
                     |
                     v
             Generated Summary
                     |
                     v
             API Response
                     |
                     v
                Web UI
```

The repository separates the frontend and backend, while the backend contains dedicated directories for ML components, summarization logic, configuration, scripts, and deployment-related files.

## 📁 Repository Structure

```text
Hindi-Text-Summarization/
│
├── backend/
│   ├── config/                 # Backend configuration
│   ├── docker/                 # Docker-related files
│   ├── ml/                     # Machine learning components
│   ├── scripts/                # Utility and setup scripts
│   ├── summarizer/             # Summarization application
│   ├── gunicorn.conf.py        # Gunicorn configuration
│   ├── manage.py               # Django management entry point
│   └── README.md               # Backend-specific documentation
│
├── frontend/
│   ├── public/                 # Static assets
│   ├── src/                    # Frontend source code
│   ├── package.json            # Frontend dependencies and scripts
│   ├── vite.config.js           # Vite configuration
│   └── README.md               # Frontend-specific documentation
│
├── requirements-backend.txt    # Python dependencies
├── requirements-frontend.txt   # Frontend-related requirements, if applicable
└── README.md                   # Project overview
```

## 🚀 Getting Started

### Prerequisites

- Python and pip
- Node.js and npm
- Git
- Additional services required by the backend configuration, if any

### 1. Clone the repository

```bash
git clone https://github.com/yashrajkastode/Hindi-Text-Summarization.git
cd Hindi-Text-Summarization
```

### 2. Set up the backend

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements-backend.txt
```

Follow the instructions in [`backend/README.md`](backend/README.md) for environment configuration, model setup, and running the Django application.

### 3. Set up the frontend

```bash
cd frontend
npm install
npm run dev
```

Use the local URL printed by Vite to open the frontend.

Check the frontend configuration and backend API settings to ensure the frontend sends requests to the correct backend address.

### 4. Deployment

The repository contains backend Docker-related files and a Gunicorn configuration.

Refer to the backend documentation for the supported deployment workflow. Production deployment requires appropriate environment variables, dependency configuration, API security, and testing of the complete application.

## 🛠️ Technology Stack

| Area | Technologies |
|---|---|
| Programming | Python, JavaScript |
| Machine Learning | Hugging Face Transformers, mT5 |
| Backend | Django, Django REST Framework |
| Frontend | Vite, JavaScript |
| Deployment | Docker-related configuration, Gunicorn |

Additional technologies should be listed here when their implementation is confirmed in the repository.

## 🎯 Use Cases

- Summarizing Hindi news articles and long-form text
- Exploring multilingual transformer models for Indic-language NLP
- Integrating ML inference into a REST API
- Building a full-stack application around an NLP model
- Experimenting with modular ML service architecture

## 🔬 Potential Improvements

- Evaluate summary quality on a representative Hindi dataset.
- Compare model outputs using ROUGE and qualitative factual-consistency checks.
- Benchmark inference latency and memory usage.
- Add automated tests for API endpoints and summarization logic.
- Improve error handling and input validation.
- Document API request and response examples.
- Validate the end-to-end frontend, backend, and deployment workflow.
- Compare mT5 with other suitable Hindi and Indic-language summarization models.

## 👨‍💻 Author

**Yashraj Kastode**

[GitHub Profile](https://github.com/yashrajkastode)

---

*An NLP and full-stack engineering project focused on Hindi text summarization and the integration of machine learning with web applications.*
