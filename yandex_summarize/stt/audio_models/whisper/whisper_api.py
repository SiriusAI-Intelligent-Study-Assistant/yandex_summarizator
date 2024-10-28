import whisper

DEVICE = "cpu"

model = whisper.load_model(r"D:\Sirius_AI_code\Task_2\sdfdsf\yandex_summarizator\yandex_summarize\stt\audio_models\whisper\checkpoints\tiny.pt", download_root="checkpoints")
model.to(DEVICE)
result = model.transcribe(r"D:\Sirius_AI_code\Task_2\sdfdsf\yandex_summarizator\test_600.wav")
print(result["text"])