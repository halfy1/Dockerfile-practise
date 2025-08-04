FROM golang:1.20

WORKDIR /app

COPY . /app

RUN go build -o app main.app

EXPOSE 8080

CMD [ "/app/app" ]