# dagster_pipeline/ops/yolo.py
from dagster import op
# import sys
# import os
# #  add project root to the path
# sys.path.append(os.path.abspath('..'))
# sys.path.append("../src") # add src directory to the path
from src.yolo_detector import run_detection

@op
def detect_yolo():
    run_detection()
    print("YOLO detection completed successfully.")
