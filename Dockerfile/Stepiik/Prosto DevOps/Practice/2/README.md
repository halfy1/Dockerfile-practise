## Запускаем Node.js-приложение в контейнере
В этом задании вы напишете Dockerfile для простого Node.js-приложения, которое будет возвращать Hello from Node Docker! по HTTP-запросу. 
### Техническое задание
1. Базовый образ — node:16.
2. Установить рабочую директорию /app внутри контейнера.
3. Скопировать локальные файлы package.json и package-lock.json в рабочую директорию, установить зависимости.
4. Скопировать весь остальной код — index.js в контейнер.
5. Использовать переменную окружения PORT для указания порта, по умолчанию 3000.
6. EXPOSE порт, который слушает ваше приложение (по умолчанию 3000).
7. CMD — запуск командой npm start 
### Итог 
При запуске контейнера, если пробросить порт (например, -p 3000:3000), открыть http://localhost:3000, вы должны увидеть «Hello from Node Docker!», возвращённое вашим приложением.
### Структура папки
- `Dockerfile` — вы создаёте по требованиям выше.
- `package.json` — с базовым скриптом `"start": "node index.js"`. Пример:
```
{
  "name": "my-node-docker-app",
  "version": "1.0.0",
  "description": "Пример Docker-приложения на Node.js",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```
- `index.js` — тут ваш код приложения, который слушает на порту `process.env.PORT || 3000` и возвращает «Hello from Node Docker!». Пример:
```
const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Hello from Node Docker!");
});

app.listen(PORT, () => {
  console.log("Server is running on port " + PORT);
});
```