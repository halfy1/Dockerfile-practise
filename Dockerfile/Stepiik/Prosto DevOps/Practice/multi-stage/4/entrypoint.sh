#!/bin/bash
set -e

WORKERS=${GUNICORN_WORKERS:-4}
PORT=${PORT:-5000}

# Запуск gunicorn с правильным числом воркеров
exec gunicorn --bind 0.0.0.0:$PORT --workers $WORKERS app:app