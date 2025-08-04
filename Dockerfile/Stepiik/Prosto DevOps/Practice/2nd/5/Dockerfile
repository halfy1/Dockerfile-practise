FROM alpine:3.17

ARG TEXT_TOOL=grep

RUN apk add --no-cache-dir $TEXT_TOOL

RUN adduser -D myuser
USER myuser

WORKDIR /home/myuser/app

COPY process.sh .
RUN chmod +x process.sh

VOLUME [ "/data" ]

ENTRYPOINT [ "./process.sh", "/data/input.txt" ]
