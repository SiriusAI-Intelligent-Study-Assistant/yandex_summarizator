# Задание на второй этап отбора

В репозитории представлен программный код 
для суммаризации видеороликов с **Яндекс.Диска** 
и **API** для работы с ним.

### Что сделано:
1. Реализован скрипт для работы с **API Яндекс.Диска**
2. Реализовано несколько скриптов для распознавания речи (vosk, whisper)
3. Реализовано несколько скриптов для суммаризации текста из видеоролоиков (llm, in_development)
4. Реализован собственный API

---
## Документация:
```Python
# -*- coding: utf-8 -*-
# pipeline

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
video.get_video("https://disk.yandex.ru/i/27Um31l3onCzlg")
video.save_video("video.mp4")

video_name = convert_wav(os.path.abspath("video.mp4"))

audio.file_open(video_name)
text = audio.recognize()
summarize_text = summarize_model.summarize(text)

print(summarize_text)
```