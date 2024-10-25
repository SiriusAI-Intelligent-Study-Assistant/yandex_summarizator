from dotenv import load_dotenv
import os

load_dotenv()

YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
HG_TOKEN = os.getenv("HG_TOKEN")