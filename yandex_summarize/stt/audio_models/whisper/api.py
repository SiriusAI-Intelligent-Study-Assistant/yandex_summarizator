# -*- coding: utf-8 -*-

import whisper
import os
import logging


class WhisperAudioModel:
    def __init__(self, model_name, _device):
        logging.info(f"Model initialized: <whisper_{model_name}>, to device: <{_device}>")
        self.model_name = model_name
        self.device = _device

    def load(self) -> None:
        self.model = whisper.load_model(self.model_name)
        self.model.to(self.device)
        logging.info(f'The model "whisper_{self.model_name}" has been successfully loaded')

    def file_open(self, path: str) -> None:
        self.audiopath = os.path.abspath(path)
        logging.info(f'Audio file opened: "{self.audiopath}"')

    def recognize(self) -> str:
        logging.info("Transcribing audio file...")
        self.result = self.model.transcribe(self.audiopath)
        logging.info(f'Audio file recognized: "{self.result["text"]}"')
        
        return self.result["text"]