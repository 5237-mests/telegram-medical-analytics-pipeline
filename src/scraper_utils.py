import os
import json
import logging
from datetime import datetime
from .telegram_client import client
from .config import BASE_DIR

logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

async def scrape_channel(channel_url, limit=100):
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

        if message.photo:
            img_folder = os.path.join(BASE_DIR, 'images')
            os.makedirs(img_folder, exist_ok=True)
            img_path = os.path.join(img_folder, f"{channel_url.split('/')[-1]}_{message.id}.jpg")
            await message.download_media(file=img_path)
            msg['image_path'] = img_path

        messages.append(msg)

    save_data(messages, channel_url)

def save_data(messages, channel_url):
    date_folder = datetime.utcnow().strftime('%Y-%m-%d')
    save_folder = os.path.join(BASE_DIR, date_folder)
    os.makedirs(save_folder, exist_ok=True)
    file_path = os.path.join(save_folder, f"{channel_url.split('/')[-1]}.json")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

    logging.info(f"✅ Saved {len(messages)} messages from {channel_url} to {file_path}")
