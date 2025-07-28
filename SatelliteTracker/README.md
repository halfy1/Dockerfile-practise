## Техническое задание: Dockerfile для SatelliteTracker
### Цель:
Создать Dockerfile, который:
- Собирает ASP.NET Core WebAPI-проект SatelliteTracker
- Поддерживает симуляцию GPS-данных (файл output.nmea копируется или монтируется)
- Позволяет указать параметры подключения к PostgreSQL через переменные окружения
Автоматически применяет миграции при запуске
- Запускает приложение с использованием ENTRYPOINT

### Требования:
1. Использовать официальный mcr.microsoft.com/dotnet/sdk для сборки
2. Публиковать приложение в Release-режиме
3. Использовать mcr.microsoft.com/dotnet/aspnet как runtime-слой
4. Установить рабочую директорию /app
5. Копировать appsettings.*.json, Nmea_src/output.nmea и всё нужное для симуляции
6. Включить скрипт entrypoint.sh и сделать его исполняемым

