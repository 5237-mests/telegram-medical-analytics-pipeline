import os
import json
import psycopg2
from dotenv import load_dotenv

OUTPUT_JSON = "data/raw/yolo_detections.json"

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS raw.image_detections (
    id SERIAL PRIMARY KEY,
    image_file TEXT,
    class_id INT,
    class_name TEXT,
    confidence FLOAT,
    bbox FLOAT[]
);
""")
conn.commit()

def load_detections():
    with open(OUTPUT_JSON, 'r') as f:
        detections = json.load(f)

    for det in detections:
        cur.execute("""
            INSERT INTO raw.image_detections (image_file, class_id, class_name, confidence, bbox)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            det['image_file'], det['class_id'], det['class_name'], det['confidence'], det['bbox']
        ))
    conn.commit()
