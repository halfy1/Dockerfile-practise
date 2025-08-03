# 5. Задание ENTRYPOINT и использование аргументов запуска
# Сценарий: У вас есть Python или Go-утилита, которая принимает CLI-аргументы для разных режимов работы. 
# Хотите, чтобы при запуске контейнера просто дописывали нужные опции (например, --debug).

FROM python:3.9

WORKDIR /app

COPY main.py /app/main.py

ENTRYPOINT [ "python", "main.py" ]
CMD [ "--mode", "default" ]

