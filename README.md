# Hindi Text Summarization System 🇮🇳

A backend-focused Hindi text summarization system built using modern NLP models and Django.  
The project provides an API for abstractive summarization of Hindi news and long-form text.

This repository is structured for **production deployment**, with clear separation between:
- Web backend (Django + DRF)
- ML inference services
- Async task handling (Celery)
- Containerization (Docker)

---

## ✨ Features

- Abstractive Hindi text summarization
- Transformer-based NLP model (`google/mt5-base`)
- REST API built with Django REST Framework
- Clean service-oriented architecture
- Celery support for asynchronous summarization
- Docker & Gunicorn ready
- Easily extensible to other Indic models

---

## 🧠 Model Used

- **Model**: `google/mt5-base`
- **Type**: Multilingual Encoder–Decoder Transformer
- **Approach**: Prompt-based abstractive summarization (no fine-tuning)

The system applies preprocessing and optimized decoding strategies to improve summary quality for Hindi news text.

---

## 🏗️ High-Level Architecture

Client
↓
Django REST API
↓
Summarization Service
↓
mT5 Model (Inference)

yaml
Copy code

Optional:
- Celery + Redis for async execution
- Gunicorn for production serving

---

## 📁 Repository Structure

Text Summarization/
├── backend/ # Django backend + ML services
├── frontend/ # Frontend (optional / WIP)
├── docker/ # Docker configuration
├── scripts/ # Model download & warmup scripts
└── README.md # This file

yaml
Copy code

---

## 🚀 Getting Started

For backend setup and API usage, see:

➡️ **[`backend/README.md`](backend/README.md)**

---

## 🧪 Use Cases

- News article summarization (Hindi)
- Political or editorial text compression
- NLP portfolio / research project
- Backend ML system demonstration

---

## 📌 Notes

- This project prioritizes **backend correctness and architecture**
- Frontend is intentionally kept optional
- Model can be swapped later without changing API contracts

---
