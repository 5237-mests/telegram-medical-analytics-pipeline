import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

# conn = psycopg2.connect(
#     dbname=os.environ("POSTGRES_DB"),
#     user=os.environ("POSTGRES_USER"),
#     password=os.environ("POSTGRES_PASSWORD"),
#     host=os.environ("POSTGRES_HOST"),
#     port=os.environ("POSTGRES_PORT")
# )

cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE SCHEMA IF NOT EXISTS raw;
        CREATE TABLE IF NOT EXISTS raw.telegram_messages (
            id BIGINT PRIMARY KEY,
            date TIMESTAMP,
            text TEXT,
            sender_id BIGINT,
            has_media BOOLEAN,
            image_path TEXT
        );
    """)
    conn.commit()

def load_json_to_db(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        messages = json.load(f)
        for msg in messages:
            cur.execute("""
                INSERT INTO raw.telegram_messages (id, date, text, sender_id, has_media, image_path)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                msg['id'], msg['date'], msg.get('text'), msg.get('sender_id'),
                msg.get('has_media'), msg.get('image_path')
            ))
    conn.commit()

def main():
    create_table()
    raw_dir = '../data/raw/telegram_messages/2025-07-11/'
    # Load all JSON files to DB recursively
    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            if file.endswith('.json'):
                full_path = os.path.join(root, file)
                print(f"Loading {full_path} into database...")
                load_json_to_db(full_path)
    print("All JSON files loaded successfully.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
