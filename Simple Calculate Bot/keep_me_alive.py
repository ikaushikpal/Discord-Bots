from flask import Flask
from threading import Thread


app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Starting"


def main():
    app.run(host='0.0.0.0', port=8080)


def alive():
  t = Thread(target=main)
  t.start()