# 6. Использование ENV для конфигурации API
# Сценарий: Ваше приложение нуждается в базе данных или стороннем API, 
# и вы хотите задать URL и режим работы при сборке, но при запуске на 
# проде переопределить эти переменные.

FROM node:16
WORKDIR /app

ENV APP_MODE=production
ENV API_URL=https://api.example.com

COPY package*.json .
RUN npm install

COPY . .
EXPOSE 3000

CMD [ "npm", "start" ]
