from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello, World!"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/index")
def index():
    return 'This is index'