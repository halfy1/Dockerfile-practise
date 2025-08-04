#!/bin/sh
set -e

# По умолчанию ENTRYPOINT вызывается без аргументов, 
# но мы можем пробросить любые аргументы при желании.
# Например, docker run ... --help

echo "Running entrypoint... APP_MODE=${APP_MODE}, PORT=${PORT}"

if [ "$1" = "--help" ]; then
  echo "Usage: Set APP_MODE=python or node, then run container."
  echo "Example: docker run -e APP_MODE=node -p 8080:8080 "
  exit 0
fi

case "${APP_MODE}" in
  python)
    echo "Starting Python (Flask) app on port ${PORT}..."
    python flask_app.py
    ;;
  node)
    echo "Starting Node (Express.js) app on port ${PORT}..."
    node node_app.js
    ;;
  *)
    echo "Unknown APP_MODE=${APP_MODE}. Available: python, node."
    exit 1
    ;;
esac