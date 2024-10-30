# -*- coding: utf-8 -*-

# Настройка логгирования и локализации
import logging
import locale

file_log = logging.FileHandler('logs.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

locale.getpreferredencoding = lambda: "UTF-8"

# Игнорирование предупреждений
import warnings
warnings.filterwarnings("ignore")

# API-ключи
from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
