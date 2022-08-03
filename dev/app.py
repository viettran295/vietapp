from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html", utc_time=datetime.datetime.utcnow())

@app.route("/employments")
def employments():
    return render_template("employments.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/certificate")
def certificate():
    return render_template("certificate.html")