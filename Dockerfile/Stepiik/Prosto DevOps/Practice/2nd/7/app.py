from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from a health-checked Flask!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Логи можно писать в /data/logs, если хотите
    port = 5000
    app.run(host="0.0.0.0", port=port)