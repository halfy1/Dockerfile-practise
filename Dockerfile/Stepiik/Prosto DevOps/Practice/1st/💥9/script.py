import os
import configparser
from flask import Flask

app = Flask(__name__)

# Читаем переменные окружения
log_level = os.getenv("LOG_LEVEL", "info")
app_mode = os.getenv("APP_MODE", "production")

# Читаем config.ini
config = configparser.ConfigParser()
config.read("/app/config.ini")
# допустим, там [default] greeting=Hello

@app.route("/")
def hello():
    greeting = config.get("default", "greeting", fallback="Hi")
    return f"{greeting} from {app_mode} mode! (Log level: {log_level})"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)