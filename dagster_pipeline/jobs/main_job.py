# dagster_pipeline/jobs/main_job.py
from dagster import job
from dagster_pipeline.ops.scraper import scrape_telegram
from dagster_pipeline.ops.yolo import detect_yolo
from dagster_pipeline.ops.load_to_postgres import load_messages, load_yolo_detections
from dagster_pipeline.ops.dbt import run_dbt

@job
def telegram_pipeline():
    scrape_telegram()
    detect_yolo()
    load_messages()
    load_yolo_detections()
    run_dbt()
