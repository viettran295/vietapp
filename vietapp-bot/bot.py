from posixpath import split
from urllib import response
from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import ChannelAccount
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.ai.luis import LuisApplication, LuisPredictionOptions, LuisRecognizer
from translator.translator_app import Translator_App
from config import DefaultConfig

class MyBot(ActivityHandler):
    def __init__(self, config: DefaultConfig):
        self.qna_maker = QnAMaker(QnAMakerEndpoint(
            knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
            endpoint_key=config.QNA_ENDPOINT_KEY,
            host=config.QNA_ENDPOINT_HOST
        ))
        luis_app = LuisApplication(config.LUIS_APP_ID, config.LUIS_API_KEY, config.LUIS_API_HOST_NAME)
        luis_option = LuisPredictionOptions()
        self.LuisReg = LuisRecognizer(luis_app, luis_option, True)

        self.translate = Translator_App("en")

    async def on_message_activity(self, turn_context: TurnContext):
        luis_result = await self.LuisReg.recognize(turn_context)
        intent = LuisRecognizer.top_intent(luis_result)
        result = luis_result.properties["luisResult"]
        # await turn_context.send_activity(f" Luis Result {result.entities[0]}")
        
        # if: user want to translate something
        if intent == "Translation" and len(result.entities) >= 1:
            split_text = turn_context.activity.text.split(':')
            response = self.translate.translate_text(split_text[-1])
            await turn_context.send_activity(response[0])
        else:
            # else: QnA maker will answer questions
            response = await self.qna_maker.get_answers(turn_context)
            if response and len(response)>0:
                await turn_context.send_activity(MessageFactory.text(response[0].answer))
            else:
                await turn_context.send_activity("Sorry i dont have answer, please try other question")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Welcome to Translate-Bot! I can translate any languages into English, but sometimes i can be wrong :)) ")
                await turn_context.send_activity("Type 'translate: your-sentences' to activate this function (Note: ':' is important). Example: translate: Hallo, ich bin ein Bot")
                await turn_context.send_activity("Or you can ask me some random questions")