import os
import json
import logging
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

# Create Telegram Client
client = TelegramClient('session_name', API_ID, API_HASH)

# Set up logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Telegram Channels to scrape
CHANNELS = [
    'https://t.me/CheMed123',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/tikvahpharma'
]

# Output folder
BASE_DIR = 'data/raw/telegram_messages'

async def scrape_channel(channel_url, limit=100):
    try:
        await client.start()
        entity = await client.get_entity(channel_url)
        messages = []

        async for message in client.iter_messages(entity, limit=limit):
            msg = {
                'id': message.id,
                'date': str(message.date),
                'text': message.text,
                'sender_id': message.sender_id,
                'has_media': bool(message.media),
            }

            # Save image if available
            if message.photo:
                folder = os.path.join(BASE_DIR, 'images')
                os.makedirs(folder, exist_ok=True)
                img_path = os.path.join(folder, f"{channel_url.split('/')[-1]}_{message.id}.jpg")
                await message.download_media(file=img_path)
                msg['image_path'] = img_path

            messages.append(msg)

        # Save JSON file
        date_folder = datetime.utcnow().strftime('%Y-%m-%d')
        save_folder = os.path.join(BASE_DIR, date_folder)
        os.makedirs(save_folder, exist_ok=True)
        filename = f"{channel_url.split('/')[-1]}.json"
        filepath = os.path.join(save_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)

        logging.info(f"Scraped {len(messages)} messages from {channel_url} into {filepath}")

    except Exception as e:
        logging.error(f"Error scraping {channel_url}: {e}")

async def main():
    for channel in CHANNELS:
        await scrape_channel(channel)

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
