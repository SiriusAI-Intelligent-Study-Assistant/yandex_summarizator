# -*- coding: utf-8 -*-

from yandex_summarize import YaDiskAPI, Summarizer, convert_wav, AudioRecognizer
from yandex_summarize.config import MISTRAL_API_KEY
import os

summarize_model_config = {
    "API_KEY": MISTRAL_API_KEY,
    "model_name": "llm",
}

stt_model_config = {
    "API_KEY": None,
    "model_name": "vosk",
}

video = YaDiskAPI()
audio = AudioRecognizer(stt_model_config)
summarize_model = Summarizer(summarize_model_config)

audio.load_model()
video.get_video("https://disk.yandex.ru/i/27Um31l3onCzlg")#"https://disk.yandex.ru/i/IPoz9_tcJ86Luw")
video.save_video("video.mp4")

video_name = convert_wav(os.path.abspath("video.mp4"))

audio.file_open(video_name)
text = audio.recognize()
summarize_text = summarize_model.summarize(text)

print(summarize_text)