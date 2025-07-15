# dagster_pipeline/ops/dbt.py
from dagster import op
from subprocess import run

@op
def run_dbt():
    run(["dbt", "run", "--project-dir", "dbt/medigram_dbt"], check=True)