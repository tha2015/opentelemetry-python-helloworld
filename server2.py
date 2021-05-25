from flask import Flask
import requests

PORT = 8000
MESSAGE = "Hello, world!\n"

app = Flask(__name__)


@app.route("/")
def root():
    requests.get('https://api.github.com')
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT, use_reloader=False)
