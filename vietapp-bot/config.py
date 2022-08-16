#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "f127e3ea-c802-419d-af33-f88d54bad1d6")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "12029db3-552d-4b3e-ac6a-a22913032845")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://qna-vietapp.azurewebsites.net/qnamaker")
