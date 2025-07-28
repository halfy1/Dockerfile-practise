## Техническое задание: async-fastapi-app
### Цель:
Собрать production-ready образ FastAPI-приложения с асинхронной логикой и поддержкой PostgreSQL.

### Требования:
1. Базовый язык: Python 3.12
2. Асинхронный веб-фреймворк: FastAPI + Uvicorn
3. Использовать многостадийную сборку:
    - builder — установка зависимостей
    - final — минимальный runtime
4. Использовать ENV для настройки:
    - DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
5. Использовать CMD для запуска Uvicorn
6. Встроить ENTRYPOINT скрипт инициализации
7. Приложение должно читать .env, если он есть
8. Порт по умолчанию: 8000
9. Образ должен быть минимальным и готовым к деплою

### Структура:
```
async-fastapi-app/
├── app/
│   ├── main.py
│   └── db.py
├── requirements.txt
├── entrypoint.sh
└── .env
```