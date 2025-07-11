from .telegram_client import client
from .config import CHANNELS
from .scraper_utils import scrape_channel

async def run_scraper():
    for channel in CHANNELS:
        await scrape_channel(channel)

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(run_scraper())
