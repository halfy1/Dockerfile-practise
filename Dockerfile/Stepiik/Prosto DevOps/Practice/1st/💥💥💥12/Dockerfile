FROM python:3.9

RUN apt-get update && \
    apt-get install -y nodejs \
    npm

ENV APP_MODE=python
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD assets.tar.gz /app/assets

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY package*.json /app/
RUN npm install

COPY flask_app.py /app/flask_app.py
COPY node_app.js /app/node_app.js
COPY entrypoint.sh /app/entrypoint.sh

EXPOSE 8080

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD [ "--help" ]
