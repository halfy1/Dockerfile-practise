FROM node:14-slim
WORKDIR /app

ENV NODE_ENV=production

COPY package*.json ./
RUN npm install --production

COPY . .

EXPOSE 3000
CMD ["npm","start"]