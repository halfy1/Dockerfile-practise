FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip && \
    rm -rf /var/lib/lists/*

RUN pip3 install flask

COPY app.py /opt/app.py

WORKDIR /opt

ENV FLASK_APP=/app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD [ "flask" , 'run']