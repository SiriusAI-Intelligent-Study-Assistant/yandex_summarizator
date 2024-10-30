# Задание на второй этап отбора

В репозитории представлен программный код 
для суммаризации видеороликов с **Яндекс.Диска** 
и **API** для работы с ним.

### Что сделано:
1. Реализован скрипт для работы с **API Яндекс.Диска**
2. Реализовано несколько скриптов для распознавания речи (vosk, whisper, GoogleSTT)
3. Реализовано несколько скриптов для суммаризации текста из видеоролоиков (llm, rut5)
4. Реализован собственный API

---
## Документация:

### Для корректной работы программы требуется `ffmpeg`: https://www.ffmpeg.org/

---
### Основные параметры:
```Python
from yandex_summarize import YaSummarizator, MISTRAL_API_KEY

DEVICE = "cpu" #cuda
example_url = "https://disk.yandex.ru/i/27Um31l3onCzlg"

model_config = {
    "stt_model": {"vosk": "vosk-model-small-ru-0.22"},
    "summarize_model": "llm",
    "API_KEY": MISTRAL_API_KEY,
    "DEVICE": DEVICE,
}
```

### With context manager:
```Python
with YaSummarizator( model_config ) as ya_summarizator:
    ya_summarizator.get_video( example_url ) 
    print( ya_summarizator.summarize() )
```

### Without context manager:
```Python
ya_summarizator = YaSummarizator( model_config )
ya_summarizator.get_video( example_url ) 
print( ya_summarizator.summarize() )

ya_summarizator.close()
```

---
## Подробнее про `model_config`:

### `stt_model` - указание модели для распознавания речи из видео. Может принимать значения:
 - `vosk` - легковесная **локальная** модель для распознавания речи. Скачать веса можно с официального сайта https://alphacephei.com/vosk/models. По умолчанию в проекте используются веса `vosk-model-small-ru-0.22`. Они находятся в репозитории по пути: `yandex_summarize\stt\audio_models\vosk\vosk-model-small-ru-0.22`.

- `whisper` - библиотека от OpenAI для распознавания речи. Её весов нет в репозитории, необходимо указать модель для загрузки весов и локального запуска:
    - `tiny`
    - `base`
    - `small`
    - `medium`
    - `large`
    - `turbo`
    
    Пример: `{"whisper": "base"}`<br>
    Веса модели сохраняются по пути: `~/.cache/whisper`<br>
    Подробнее: https://github.com/openai/whisper

- `GoogleSTT` - обёртка вокруг библиотека от **Google** - SpeechRecognition. Распознаёт текст с помощью Google API. Онлайн. Указать язык:
    - `ru_RU`
    - `en_EN`
    - и др.
    
    Пример: `{"GoogleSTT": "ru_RU"}`<br>
    Подробнее: https://pypi.org/project/SpeechRecognition/
---
### `summarize_model` - указание модели для суммаризации текста. Может принимать значения:

- `llm` - для суммаризации используется **LLM** модель: Mistral_Large. Для использования этой модели вам придётся получить **токен** на официальном сайте: https://mistral.ai/<br>
**Инструкция**:
    - Зарегистрируйте на официальном сайте
    - https://console.mistral.ai/api-keys/

    Поместите **токен** в `yandex_summarize\config.py` или в файл `.env`

- `rut5` - модель для суммаризации текстов. Исходный код: https://huggingface.co/cointegrated/rut5-base-absum<br>Модель сохраняет веса локально на диск по пути: `~\.cache\huggingface\hub\models--cointegrated--rut5-base-absum`

---
### `API_KEY`  
- MISTRAL_API_KEY - нужен для работы `mistralai`

---
### `DEVICE` 
- `cpu` - по умолчанию

- `cuda` - для использования **GPU**, необходимо установить **CUDA**: `pip3 install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121 --force-reinstall`. https://pytorch.org/

---
## Параметры `summarize`:
В зависимости от модели суммаризации:
- `llm`:
    - `text_volume = 5` - настраивает объём текста. Примнимает значения `int` от 1 до 10
    - `bullet_points = 0` - настраивает ключевые моменты. Примнимает значения `int` от 0 до любого числа, где 0 - отсутствие ключевых точек

- `rut5`:
    - `n_words = None | int`
    - `compression = None | int`
    - `max_length = 1000`
    - `num_beams = 3`
    - `do_sample = False`
    - `repetition_penalty = 10.0`

\* _Результат может незначительно отличаться от введённых параметров, так как используются нейросетевые модели_