FROM rust:1.68

ARG BUILD_MODE=debug
RUN echo "Building with mode: $BUILD_MODE"

SHELL [ "/bin/bash", "-c"]

STOPSIGNAL SIGINT

LABEL maintainer="you@example.com" \
    version="1.0" \
    description="CLI app"

WORKDIR /app

COPY Cargo.toml Cargo.lock entrypoint.sh ./
COPY main.rs src/

RUN if [ "$BUILD_MODE" = "release" ]; then \
      cargo build --release ; \
    else \
      cargo build --debug ; \
    fi \
    && chmod +x entrypoint.sh


ENTRYPOINT ["/app/entrypoint.sh"]
CMD []