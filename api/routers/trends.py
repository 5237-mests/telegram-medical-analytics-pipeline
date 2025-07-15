
# api/routers/trends.py
from fastapi import APIRouter
from api.db import get_connection

router = APIRouter()

@router.get("/trends/daily")
def get_daily_object_trends():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT
                DATE(msg.message_date) AS date,
                det.class_name,
                COUNT(*) AS count
            FROM raw.image_detections det
            JOIN raw.telegram_messages msg
              ON det.image_file = SPLIT_PART(msg.image_path, '/', -1)
            GROUP BY date, det.class_name
            ORDER BY date, count DESC;
        """)
        rows = cur.fetchall()
        return [
            {
                "date": str(row[0]),
                "class_name": row[1],
                "count": row[2]
            } for row in rows
        ]