FROM node:16

ARG APP_VERSION=1.0
RUN echo "Building version $APP_VERSION"

LABEL maintainer="you@example.com" \
    version=$APP_VERSION

RUN useradd -m -s /bin/bash nodeuser
USER nodeuser
WORKDIR /home/nodeuser/app

VOLUME [ "/home/nodeuser/app" ]

COPY package*.json ./
RUN npm install --prefix

COPY index.js /app/index.js

ENTRYPOINT [ "npm", "start" ]
