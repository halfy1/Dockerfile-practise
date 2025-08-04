FROM python:3.9

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl

RUN pip install flask

COPY script.py /app/script.py
COPY config.ini /app/config.ini

ENV LOG_LEVEL=info
ENV APP_MODE=production

ENTRYPOINT [ "python", "/app/script.py" ]

EXPOSE 9000