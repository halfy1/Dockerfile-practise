## Техническое задание
## Цель:
Создать мультистейдж Dockerfile для fullstack-приложения с backend на Node.js (Express) и frontend на React/Vite.

## Структура проекта:
```
fullstack-app/
├── backend/
│   ├── package.json
│   ├── package-lock.json
│   └── index.js
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
└── Dockerfile
```

## Что должно быть в Dockerfile:
- Первый stage: frontend-build
    - Базовый образ: node:18-alpine
    - Установить зависимости из frontend/package.json
    - Выполнить сборку Vite/React (npm run build)
    - Результат: /app/frontend/dist
- Второй stage: backend
    - Базовый образ: node:18-alpine
    - Скопировать бэкенд и фронтенд-сборку
    - Установить зависимости (backend/package.json)
    - Фронтенд-контент должен быть размещён как статические файлы через Express
    - Приложение должно стартовать командой node index.js
- Открыть порт 8080
- Рабочая директория /app