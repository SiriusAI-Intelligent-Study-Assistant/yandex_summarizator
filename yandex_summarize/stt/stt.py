# -*- coding: utf-8 -*-

from .audio_models.vosk.api import VoskAudioModel
from .audio_models.whisper.api import WhisperAudioModel
from .audio_models.google_speech_rec.api import GoogleSTT


class AudioRecognizer:
    '''
    A class for managing audio models
    '''

    def __init__(self, model_name: dict, _device: str) -> None:
        match model_name:
            case {"vosk": weight_path}: self.model = VoskAudioModel(weight_path)
            case {"whisper": whisper_name}: self.model = WhisperAudioModel(whisper_name, _device)
            case {"GoogleSTT": language}: self.model = GoogleSTT(language)
            
            case _: raise NameError(f"Model <{model_name}> not found!")

    def load_model(self) -> None:
        self.model.load()

    def file_open(self, path: str) -> None:
        self.model.file_open(path)

    def recognize(self) -> str:
        return self.model.recognize()