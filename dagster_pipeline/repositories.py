# dagster_pipeline/repositories.py
from dagster import Definitions
from dagster_pipeline.jobs.main_job import telegram_pipeline

defs = Definitions(
    jobs=[telegram_pipeline],
)
