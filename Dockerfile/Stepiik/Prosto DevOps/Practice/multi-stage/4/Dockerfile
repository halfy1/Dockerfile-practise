#base
FROM python:3.10-slim AS base
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


#builder
FROM base AS builder

RUN apt-get update && \
    apt-get install -y -no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements*.txt ./
RUN pip wheel --no-cache-dir --wheel-dir /wheels \
    -r -requirements.txt \
    -r requirements-dev.txt


#development
FROM base AS development
COPY --from=builder /wheels /wheels
COPY requirements*.txt ./
RUN pip install --no-cache -no-index --find-links=/wheel \
    -r requirements-dev.txt \
    && rm -rf /wheels

ENV FLASK_ENV=development \
    FLASK_DEBUG=1

VOLUME [ "/app" ]
EXPOSE 5000
CMD [ "python", "app.py" ]


#proudciton
FROM base AS production
COPY --from=builder /wheels /wheels
COPY requirements.txt ./
RUN pip install --no-cache no-index --find-links=/wheels \
    -r  requirements.txt && \
    && pip install --no-cache --no-index --find-links=/wheels gunicorn && \
    rm -rf  /wheels && \
    adduser --disabled-password --gecos "" flask && \
    chown -R flask:flask /app

COPY app.py ./
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

ENV FLASK_ENV=production \
    GUNICORN_WORKERS=4

USER flask
EXPOSE 5000
ENTRYPOINT [ "./entrypoint.sh" ]