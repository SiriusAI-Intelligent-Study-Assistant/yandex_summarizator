# -*- coding: utf-8 -*-

import logging
import locale

file_log = logging.FileHandler('logs.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

locale.getpreferredencoding = lambda: "UTF-8"

from .summarization.summarize import Summarizer
from .video2audio import convert_wav
from .get_video import YaDiskAPI
from .stt.stt import AudioRecognizer
from .config import *

__version__ = "0.1.0"