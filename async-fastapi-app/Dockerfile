FROM python:3.12-slim as builder

COPY /requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .


FROM python:3.12-slim

ENV DB_HOST=localhost \
    DB_PORT=5432 \
    DB_NAME=user \
    DB_PASSWORD=pass \
    DB_NAME=mydb \
    PORT=8000

WORKDIR /app

COPY --from=builder /usr/local/bin/python3.12/site-packages /usr/local/bin/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "univicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]