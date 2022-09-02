from speech_translator import Speech
from config import SpeechConfig

if __name__=="__main__":
    config = SpeechConfig()
    speech = Speech(config)
    file = r"C:\Users\viet tran\Desktop\Python\vietapp\dev\speech_translator\mySound.wav"
    speech.translation_from_file(file)