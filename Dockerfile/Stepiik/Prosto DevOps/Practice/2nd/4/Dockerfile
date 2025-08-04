FROM nginx:alpine

RUN apk add --no-cache-dir bash

SHELL [ "/bin/bash", "-c" ]

STOPSIGNAL SIGQIUT

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f https://localhost/health.html || exit 1

COPY index.html /usr/share/nginx/html

