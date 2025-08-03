#!/bin/sh
echo "Starting ping script..."

# Если переменная не задана, берём дефолт
URL="${PING_URL:-https://example.com}"

while true
do
  echo "Pinging $URL..."
  curl -I $URL
  sleep 5
done