FROM alpine:3.17

WORKDIR /app

RUN apk add --no-cache curl

COPY entrypoint.sh /app/entrypoint.sh

ENV PING_URL=https://example.com

ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]

