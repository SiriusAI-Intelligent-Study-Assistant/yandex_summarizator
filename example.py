# -*- coding: utf-8 -*-

from yandex_summarize import YaSummarizator, MISTRAL_API_KEY

example_url = "https://disk.yandex.ru/i/27Um31l3onCzlg"

model_config = {
    "stt_model": "vosk",
    "summarize_model": "llm",
    "API_KEY": MISTRAL_API_KEY,
}

with YaSummarizator(model_config) as ya_summarizator:
    ya_summarizator.get_video(example_url)
    print(ya_summarizator.summarize())