# api/routers/products.py
from fastapi import APIRouter, Query
from api.db import get_connection

router = APIRouter()

@router.get("/reports/top-products")
def get_top_detected_objects(limit: int = Query(10, ge=1, le=100)):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT class_name, COUNT(*) AS count
            FROM raw.image_detections
            GROUP BY class_name
            ORDER BY count DESC
            LIMIT %s;
        """, (limit,))
        rows = cur.fetchall()
        return [{"class_name": row[0], "count": row[1]} for row in rows]
