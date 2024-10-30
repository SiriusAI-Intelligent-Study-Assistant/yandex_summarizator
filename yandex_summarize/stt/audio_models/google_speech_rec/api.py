# -*- coding: utf-8 -*-

import speech_recognition as sr
import os
import logging


class GoogleSTT:
    '''
    Converting voice messages to text with Google Speech Recognition (API)
    '''

    def __init__(self, language: str = "ru_RU") -> None:
        logging.info(f"Model initialized: GoogleSTT, API")
        self.language = language

    def load(self) -> None:
        self.recogniser = sr.Recognizer()
        logging.info(f'The model "Google_Speech_Recognition" has been successfully loaded')

    def file_open(self, path: str) -> None: 
        self.audiopath = os.path.abspath(path)

        with sr.AudioFile(self.audiopath) as source:
            self.audio_text = self.recogniser.listen(source)
        
        logging.info(f'Audio file opened: "{self.audiopath}"')

    def recognize(self) -> str:
        try:
            logging.info("Transcribing audio file...")
            self.text = self.recogniser.recognize_google(self.audio_text, language=self.language)
            logging.info(f'Audio file recognized: "{self.text}"')

            return self.text
        
        except Exception as e:
            logging.error(f"GoogleSTT.recognize: {repr(e)}")
            raise