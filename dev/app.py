from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/employments")
def employments():
    return render_template("employments.html")

@app.route("/certificate")
def certificate():
    return render_template("certificate.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")