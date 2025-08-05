FROM gcc:11.2 AS builder

WORKDIR /app

RUN apt-get update && \ 
    apt-get install -y cmake \
    make && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN mkdir -p build && cd build && \
    cmake . . && \
    make


FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
    libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/build/cpp_app /usr/local/bin/cpp_app

ENTRYPOINT [ "/usr/local/bin/cpp_app" ]
