import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

CHANNELS = [
    'https://t.me/CheMed123',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/tikvahpharma'
]

BASE_DIR = 'data/raw/telegram_messages'
