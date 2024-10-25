# -*- coding: utf-8 -*-
# https://mistral.ai/

from mistralai import Mistral

class MistralAI_API:
    '''
    Class for working with Mistral API
    '''

    def __init__(self, api_key: str) -> None:
        self.model = "mistral-large-latest"
        self.client = Mistral(api_key=api_key)

    def summarize_with_llm(self, content: str, role: str='user') -> str:
        self.chat_response = self.client.chat.complete(
            model = self.model,
            messages = [
                {
                    "role": role,
                    "content": content,
                },
            ]
        )
            
        self.answer = self.chat_response.choices[0].message.content
        return self.answer