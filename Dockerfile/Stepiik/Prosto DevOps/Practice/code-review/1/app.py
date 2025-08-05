from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Считываем значение переменной окружения, заданной в Dockerfile
    message = os.getenv("HELLO_MSG", "No message found")
    return f"App says: {message}"

if __name__ == "__main__":
    # По умолчанию Flask слушает порт 5000
    # Если хотите слушать 80, измените порт либо используйте gunicorn
    app.run(host="0.0.0.0", port=5000)