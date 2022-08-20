from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

txt = ''''''
@app.route("/")
def about():
    return render_template("about.html")

@app.route("/employments")
def employments():
    return render_template("employments.html")

@app.route("/certificate", methods=['POST','GET'])
def certificate():
    if request.method == "POST":
        if request.form.get("img_to_text") == 'Scanned PDF to Text':
            noti = txt
    else:
        request.method == "GET"
        return render_template("certificate.html")
    return render_template("certificate.html", notification=noti)

@app.route("/projects")
def projects():
    return render_template("projects.html")