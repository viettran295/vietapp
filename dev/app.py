from flask import Flask, abort, render_template, request, flash, make_response, send_from_directory, current_app
import os
# from speech_translator.speech_translator import Speech
# from config import SpeechConfig

app = Flask(__name__)

# speech_config = SpeechConfig()
# speech = Speech(speech_config)

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
    return render_template("speech_translator.html")

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == "POST":
        if 'audio_file' in request.files:
            file = request.files['audio_file']
            # while True:
            #     dst = os.path.join(current_app.instance_path,
            #                         current_app.config.get('UPLOAD_FOLDER','upload'))
            #     if not os.path.exists(dst):
            #         break
            file.save(file.filename)
        return make_response('', 200)
        
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory('static', path)
# if __name__=="__main__":
#     app.secret_key = 'super secret key'
#     app.config['SESSION_TYPE'] = 'filesystem'
#     app.run(debug=True,host='0.0.0.0')