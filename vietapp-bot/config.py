#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "63358840-6bd8-41f2-9139-ff6f23b0cbe3")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "ba6d0e3c-d6c4-40ee-80bc-6fe55b942393")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://qna-bot-vietapp.azurewebsites.net/qnamaker")
