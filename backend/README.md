# Backend – Hindi Text Summarization

This directory contains the **Django backend** responsible for serving Hindi text summarization via a REST API.

The backend is designed using **clean architecture principles**, separating:
- API layer
- Business logic
- ML inference
- Utilities and async execution

The system supports **synchronous and asynchronous** summarization using Celery.

---

## 🛠️ Tech Stack

- **Python** 3.10+
- **Django** 4.x
- **Django REST Framework**
- **PyTorch**
- **Hugging Face Transformers**
- **Celery** (async task queue)
- **Redis** (message broker)
- **Gunicorn** (production)
- **Docker** (deployment)

---

## 🧠 NLP Model

- **Model**: `google/mt5-base`
- **Type**: Multilingual encoder–decoder Transformer
- **Framework**: Hugging Face Transformers
- **Execution**: CPU or GPU (auto-detected)

The model is loaded lazily and reused across requests to avoid repeated initialization.

---

## 📁 Backend Structure

backend/
├── config/ # Django project config
│ ├── settings.py
│ ├── urls.py
│ ├── celery.py
│ └── wsgi.py
│
├── summarizer/ # Core application
│ ├── views.py # API views
│ ├── urls.py # API routes
│ ├── tasks.py # Celery tasks
│ │
│ ├── serializers/
│ │ └── summarization_serializer.py
│ │
│ ├── services/
│ │ ├── model_loader.py
│ │ ├── preprocessing.py
│ │ └── summarization_service.py
│ │
│ └── utils/
│ ├── logger.py
│ └── exceptions.py
│
├── docker/
│ ├── Dockerfile
│ └── entrypoint.sh
│
├── scripts/
│ ├── download_model.py
│ └── warmup.py
│
├── manage.py

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Create Python Environment

```bash
conda create -n textsum python=3.10
conda activate textsum
(or use venv if preferred)

2️⃣ Install Dependencies

pip install -r requirements-backend.txt

▶️ Running the Backend (IMPORTANT)
This backend uses multiple processes, so multiple terminals are required during development.

🔴 Terminal 1 — Start Redis (Broker)
Redis must be running before Celery.

redis-server
If Redis is running correctly, you will see:

🟢 Terminal 2 — Apply Migrations and Start Django Server

cd "backend"
python manage.py migrate
python manage.py runserver

Django will be available at:

http://127.0.0.1:8000

🔵 Terminal 3 — Start Celery Worker
Celery handles background summarization tasks.

cd "backend"
celery -A config worker --loglevel=info --pool=solo
You should see:

 -------------- celery@User v5.6.1 (recovery)
--- ***** ----- 
-- ******* ---- Windows-10-10.0.26200-SP0 2026-01-01 15:32:23
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         config:0x1caf67d2590
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:
- *** --- * --- .> concurrency: 16 (solo)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[tasks]
  . summarizer.tasks.summarize_text_task

[2026-01-01 15:32:24,036: INFO/MainProcess] Connected to redis://localhost:6379/0
[2026-01-01 15:32:24,043: INFO/MainProcess] mingle: searching for neighbors
[2026-01-01 15:32:25,075: INFO/MainProcess] mingle: all alone
[2026-01-01 15:32:25,107: INFO/MainProcess] celery@User ready.


Connected to redis://...
ready.
🔁 Summary of Terminals
Terminal	Service	Purpose
1	Redis	Message broker
2	Django	REST API server
3	Celery	Async task execution

All three must be running for async summarization.

🔌 API Endpoint
POST /api/summarize/
Request
json
Copy code
{
  "text": "यह एक लंबा हिंदी पाठ है जिसे संक्षेप में बदलना है..."
}
Response
json
Copy code
{
  "summary": "संक्षिप्त हिंदी सारांश..."
}
If Celery is enabled, the request may return a task ID and process asynchronously.

⏳ Asynchronous Processing (Celery)
Heavy summarization runs in background workers

Prevents blocking Django request threads

Suitable for long inputs and high traffic

Redis is used as the broker

Relevant files:

bash
Copy code
config/celery.py
summarizer/tasks.py
🚀 Production Notes
Use Gunicorn to serve Django

Use multiple Celery workers for scale

Model is loaded once per worker process

Docker setup is included for deployment

🧪 Model Behavior Disclaimer
google/mt5-base is not fine-tuned specifically for summarization.

Output quality is improved through:

Text preprocessing

Prompt engineering

Controlled decoding parameters

The architecture allows easy replacement with a fine-tuned Indic model later.

📌 Design Philosophy
Thin views, fat services

No ML logic inside views

Async-first design

Production-oriented layout

