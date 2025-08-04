FROM python:3.9

RUN apt-get update && \
    apt-get install -y curl

RUN useradd -m -s /bin/bash webuser
USER webuser

WORKDIR /home/webuser

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY  app.py  ./

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f https://localhost:5000/health || exit 1

VOLUME [ "/data/logs" ]

CMD [ "python", "app.py" ]