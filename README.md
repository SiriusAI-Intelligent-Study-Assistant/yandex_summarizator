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

### Основные параметры
```Python
from yandex_summarize import YaSummarizator, MISTRAL_API_KEY

example_url = "https://disk.yandex.ru/i/27Um31l3onCzlg"

model_config = {
    "stt_model": "vosk",        # whisper
    "summarize_model": "llm",   # summarizator
    "API_KEY": MISTRAL_API_KEY, # HG_TOKEN
}
```

### With context manager
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