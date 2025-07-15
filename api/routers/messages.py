# api/routers/messages.py
from fastapi import APIRouter
from api.db import get_connection

router = APIRouter()

@router.get("/messages/summary")
def get_message_summary():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT
                COUNT(*) AS total_messages,
                COUNT(image_path) AS total_with_images,
                COUNT(*) FILTER (WHERE has_media) AS total_with_media
            FROM raw.telegram_messages;
        """)
        result = cur.fetchone()
        return {
            "total_messages": result[0],
            "total_with_images": result[1],
            "total_with_media": result[2]
        }
