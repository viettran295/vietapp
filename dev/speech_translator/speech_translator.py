import azure.cognitiveservices.speech as speechsdk
from config import SpeechConfig

class Speech:
    def __init__(self, config: SpeechConfig) -> None:
        self.key = config.SPEECH_KEY
        self.region = config.SPEECH_REGION

    def recognize_from_microphone(self):
        speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=self.key, region=self.region)
        # speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription='790d995fc74e4aceb8fde514d8c82d6f', region='westeurope')

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
        # elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
        #     cancellation_details = translation_recognition_result.cancellation_details
        #     print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        #     if cancellation_details.reason == speechsdk.CancellationReason.Error:
        #         print("Error details: {}".format(cancellation_details.error_details))
    
    def translation_from_file(self, filename: str):
        # set up translation parameters: source language and target languages
        translation_config = speechsdk.translation.SpeechTranslationConfig(
            subscription=self.key, region=self.region,
            speech_recognition_language='de-DE',
            target_languages=('en','vi'))
        audio_config = speechsdk.audio.AudioConfig(filename=filename)

        # Creates a translation recognizer using and audio file as input.
        recognizer = speechsdk.translation.TranslationRecognizer(
            translation_config=translation_config, audio_config=audio_config)

        # Starts translation, and returns after a single utterance is recognized. The end of a
        # single utterance is determined by listening for silence at the end or until a maximum of 15
        # seconds of audio is processed. The task returns the recognition text as result.
        # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
        # shot recognition like command or query.
        # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
        result = recognizer.recognize_once()

        # Check the result
        if result.reason == speechsdk.ResultReason.TranslatedSpeech:
            print("""Recognized: {}
            English: {}
            Vietnamese: {}""".format(
                result.text, result.translations['en'], result.translations['vi']))
        elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))