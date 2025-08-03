FROM node:18-alpine AS frontend-build

WORKDIR /app/frontend

COPY frontend/package*.json ./ 

RUN npm install

COPY frontend/ .

RUN npm run build


FROM node:18-alpine AS backend

WORKDIR /app

COPY  backend/package*.json ./
RUN npm install --only=production

COPY backend/ .

COPY --from=frontend-build /app/frontend/dist ./public

EXPOSE 8080

CMD [ "node", '"index.js' ]