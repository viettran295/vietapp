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

    LUIS_APP_ID = os.environ.get("LuisAppId", "99869189-930d-4807-b8f6-dd2979cfe130")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "7209b1bba256424482b3d9104b39c93c")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://bot-vietapp.cognitiveservices.azure.com/")

    TRANSLATE_KEY = "d07c486a86e04ccf90651d02c1b49ac1"
    TRANSLATE_LOCATION = "westeurope"
