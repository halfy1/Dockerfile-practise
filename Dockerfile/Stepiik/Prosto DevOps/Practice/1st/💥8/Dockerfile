FROM node:16

WORKDIR /app

COPY package*.json /app/
RUN npm install
COPY fetch.js /app/fetch.js

ENV API_URL=https://jsonplaceholder.typicode.com/todos/1
ENV FETCH_INTERVAL=5000

ENTRYPOINT [ "node", "fetch.js" ]

