FROM python:3.9

RUN apt-get update && \
    apt-get install -y libpq-dev \
    imagemagick 
 ]
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000