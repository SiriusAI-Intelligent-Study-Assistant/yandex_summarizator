# -*- coding: utf-8 -*-

from .summarization.summarize import Summarizer
from .video2audio import convert_wav
from .get_video import YaDiskAPI
from .stt.stt import AudioRecognizer
import os


class YaSummarizator:
    '''
    Pipeline for summarizing video from Yandex.Disk link
    '''

    def __init__(self, model_config: dict) -> None:
        self.video = YaDiskAPI()
        self.summarize_model = Summarizer(model_config["summarize_model"], 
                                          model_config['API_KEY'])
        
        self.audio = AudioRecognizer(model_config["stt_model"])
        self.audio.load_model()

    def __enter__(self) -> object:
        return self
    
    def __exit__(self, *args, **kwargs) -> None:
        self._temp_clear()

    def _get_temp_path(self) -> str:
        return os.getcwd() + '\\' + __name__.split('.')[0] + '\\temp\\'
    
    def _temp_clear(self) -> bool:
        os.remove(self._get_temp_path() + self._video_name)
        os.remove(self.audio_name)

        return True if not(os.path.exists(self._get_temp_path() + self._video_name))\
                   and not(os.path.exists(self.audio_name)) else False

    def get_video(self, url: str, _video_name: str = "video.mp4") -> None:
        self._video_name = _video_name
        self.video.get_video(url)
        self.video.save_video(self._get_temp_path() + self._video_name)
        self.audio_name = convert_wav(self._get_temp_path() + self._video_name)
        self.audio.file_open(self.audio_name)
        
    def summarize(self) -> str:
        self.text = self.audio.recognize()
        self.summarize_text = self.summarize_model.summarize(self.text)
        
        return self.summarize_text
    
    def close(self) -> bool:
        return self._temp_clear()