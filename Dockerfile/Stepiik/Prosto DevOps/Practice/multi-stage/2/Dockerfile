#builder
FROM golang:1.18-alpine AS builder
WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY *.go ./

RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"'  \
    -O api-service .

    
#security-check
FROM builder AS security-check
RUN go install github.com/securego/gosec/v2/cmd/gosec@latest
RUN gosec ./...


#production
FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/api-service /api-service

EXPOSE 8080

ENTRYPOINT [ "/api-service" ]