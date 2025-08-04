FROM python:3.9

SHELL [ "/bin/bash", "-c" ]


ARG BUILD_MODE=dev
RUN echo "Building with mode: $BUILD_MODE"

LABEL maintainer="you@example.com" \
    version=1.0 \
    description = "Advanced Dockerfile example"

RUN useradd -m -s /bin/bash myapp
USER myapp
WORKDIR /home/myapp

VOLUME /home/myapp/data

ONBUILD COPY .  /home/myapp/extra

STOPSIGNAL SIGQIUT

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f https://localhost:8080 || exit 1

COPY app.py /home/myapp/

RUN pip install flask

EXPOSE 8080

ENTRYPOINT [ "python", "app.py" ]