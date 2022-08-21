from enum import Enum
from typing import Dict
from botbuilder.ai.luis import LuisRecognizer
from botbuilder.core import IntentScore, TopIntent, TurnContext

class Intent(Enum):
    TRANSLATION = "Translation"

def top_intent(intents: Dict[Intent, dict]) -> TopIntent:
    max_intent = Intent.NONE_INTENT
    max_value = 0.0

    for intent, value in intents:
        intent_score = IntentScore(value)
        if intent_score.score > max_value:
            max_intent, max_value = intent, intent_score.score
    return TopIntent(max_intent, max_value)

class LuisHelper:
    @staticmethod
    async def execute_luis_query(luis_recognizer: LuisRecognizer, turn_context: TurnContext) ->(Intent, object):
        result = None
        intent = None
        try:
            pass
        except Exception as exception:
            print(exception)
        
        return intent, result

