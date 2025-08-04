FROM node:16-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY public/ ./public/
COPY src/ ./src/
COPY .env* ./
COPY tsconfig*.json ./


CMD npm run buil

FROM nginx:1.21-alpine AS production

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]