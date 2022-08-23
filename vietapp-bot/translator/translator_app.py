from urllib import request, response
import requests, uuid, json
from typing import List

class Translator_App:
    def __init__(self, to_language: str) -> None:        
        self.key = "d07c486a86e04ccf90651d02c1b49ac1"
        # Endpoint for text
        self.endpoint = "https://api.cognitive.microsofttranslator.com"
        self.location = "westeurope"
        self.path = "/translate"
        self.contructed_url = self.endpoint + self.path

        self.params = {
            'api-version': '3.0',
            # 'from': [from_language],
            'to': [to_language]
        }
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def translate_text(self, text: str) -> List[str]:
        body = [{'text': text}]
        request = requests.post(self.contructed_url, headers=self.headers, 
                                params=self.params, json=body)
        response = request.json()
        to_json = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',',':'))
        response_list = []
        for i in range(len(response[0]['translations'])):
            response_list.append(response[0]['translations'][i]['text'])
        return response_list

# test = Translator_App('en')
# response = test.translate_text("meine Familie wohnt in deutschland")

# print(response)