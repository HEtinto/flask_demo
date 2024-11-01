from flask import Flask
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootsrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404