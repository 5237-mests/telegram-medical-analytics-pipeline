# dagster_pipeline/ops/load_to_postgres.py
from dagster import op
from subprocess import run

@op
def load_messages():
    run(["python", "src/load_to_postgres.py"], check=True)

@op
def load_yolo_detections():
    run(["python", "src/load_yolo_to_postgres.py"], check=True)
