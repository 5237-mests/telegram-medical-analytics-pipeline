# dagster_pipeline/ops/scraper.py
from dagster import op
from src.main_scraper import run_scraper
from src.telegram_client import client

@op
def scrape_telegram():
    with client:
        client.loop.run_until_complete(run_scraper())
