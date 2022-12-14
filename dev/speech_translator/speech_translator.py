import azure.cognitiveservices.speech as speechsdk
from config import SpeechConfig

class Speech:
    def __init__(self, config: SpeechConfig) -> None:
        self.key = config.SPEECH_KEY
        self.region = config.SPEECH_REGION

    def recognize_from_microphone(self):
        speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=self.key, region=self.region)
        speech_translation_config.speech_recognition_language="de-DE"

        target_language="en"
        speech_translation_config.add_target_language(target_language)

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

        translation_recognition_result = translation_recognizer.recognize_once()

        if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
            # print("Recognized: {}".format(translation_recognition_result.text))
            # print("""Translated into '{}': {}""".format(
            #     target_language, 
            #     translation_recognition_result.translations[target_language]))
            return f"{translation_recognition_result.translations[target_language]}"
        elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            # print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
            return f"could not be recognized {translation_recognition_result.no_match_details}"
    
    def speech_recognize_once_from_mic(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.key, region=self.region)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        result = speech_recognizer.recognize_once()

        # Check the result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return "{}".format(result.text)
        elif result.reason == speechsdk.ResultReason.NoMatch:
            return "No speech could be recognized"
    