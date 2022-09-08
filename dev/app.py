from flask import Flask, render_template, request
from translator_app.translator_app import Translator_App

app = Flask(__name__)

trans = Translator_App('en')

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/employments")
def employments():
    return render_template("employments.html")

@app.route("/certificate", methods=['POST','GET'])
def certificate():
    return render_template("certificate.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/bot_architekture")
def bot_architekture():
    return render_template("bot_architekture.html")

@app.route("/speech_translator", methods=['POST','GET'])
def speech_translator():
    if request.method == "POST":
        pass
    return render_template("speech_translator.html")
        

if __name__=="__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True,host='0.0.0.0')