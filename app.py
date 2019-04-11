from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lucid-dreaming-techniques")
def techniques():
    return render_template("techniques.html")

@app.route("/lucid-experiences")
def experience():
    return render_template("experience.html")

@app.route("/about-me")
def about():
    return render_template("about.html")
