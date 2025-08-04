FROM python:3.9

WORKDIR /app

RUN apt-get update && \
    apt-get install -y tree

ADD data.tar.gz /opt/data

ENV DATA_PATH=/opt/data

COPY process.py /app/process.py

CMD [ "python", "/app/process.pyS" ]