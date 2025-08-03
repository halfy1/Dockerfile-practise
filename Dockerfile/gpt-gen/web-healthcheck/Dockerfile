FROM python:3.12-slim

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY healthcheck.py .

ENV TARGET_URL=https://example.com
ENV DELAY=5

ENTRYPOINT [ "python", "healthcheck.py" ]
CMD [  ]

