from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Guys!</p>"


@app.route("/about")
def about_page():
    return "<p>Welcome to the about page!</p>"

@app.route("/matrix")
def matrix():
    return "<p>I am a software Engineer!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"