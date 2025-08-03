FROM python:3.9

WORKDIR /app

COPY calc.py /app/calc.py

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python", "calc.py" ]

CMD [ "--help" ]