#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Warming up model..."
python scripts/warmup.py

echo "Starting Gunicorn..."
gunicorn config.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 1 \
  --threads 4 \
  --timeout 120
