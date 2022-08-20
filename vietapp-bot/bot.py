# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from urllib import response
from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import ChannelAccount
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from config import DefaultConfig

class MyBot(ActivityHandler):
    def __init__(self, config: DefaultConfig):
        self.qna_maker = QnAMaker(QnAMakerEndpoint(
            knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
            endpoint_key=config.QNA_ENDPOINT_KEY,
            host=config.QNA_ENDPOINT_HOST
        ))
    
    async def on_message_activity(self, turn_context: TurnContext):
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        if "translate:" in turn_context.activity.text:
            await turn_context.send_activities("Your result: ...")
        else:
            response = await self.qna_maker.get_answers(turn_context)
            if response and len(response)>0:
                await turn_context.send_activity(MessageFactory.text(response[0].answer))
            else:
                await turn_context.send_activities("Sorry i dont have answer, please try other question")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Welcome to Vietbot! Just ask me something for fun")
