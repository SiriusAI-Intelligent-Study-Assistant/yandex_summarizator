# -*- coding: utf-8 -*-

from yandex_summarize import YaSummarizator, MISTRAL_API_KEY

DEVICE = "cpu" #cuda

example_url = "https://disk.yandex.ru/i/27Um31l3onCzlg"

model_config = {
    "stt_model": {"vosk": "vosk-model-small-ru-0.22"},
    "summarize_model": "llm",
    "API_KEY": MISTRAL_API_KEY,
    "DEVICE": DEVICE,
}

with YaSummarizator(model_config) as ya_summarizator:
    ya_summarizator.get_video(example_url)
    print(ya_summarizator.summarize())