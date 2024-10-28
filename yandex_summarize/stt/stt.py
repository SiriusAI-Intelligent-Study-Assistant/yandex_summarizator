# -*- coding: utf-8 -*-

from .audio_models.vosk.vosk_api import VoskAudioModel


class AudioRecognizer:
    '''
    Audio models inference
    '''

    def __init__(self, model_name: str) -> None:
        match model_name:
            case "vosk": self.model = VoskAudioModel()
            case _: raise NameError(f"Model <{model_name}> not found!")

    def load_model(self) -> None:
        self.model.load()

    def file_open(self, path: str) -> None:
        self.model.file_open(path)

    def recognize(self) -> str:
        return self.model.recognize()
