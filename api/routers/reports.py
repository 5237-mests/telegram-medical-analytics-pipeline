# api/routers/reports.py
from fastapi import APIRouter, Query
from api.db import get_connection
from api.models.response_schemas import TopProduct

router = APIRouter()

@router.get("/reports/top-products", response_model=list[TopProduct])
def get_top_products(limit: int = Query(10, ge=1, le=100)):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT class_name, COUNT(*) AS count
            FROM raw.fct_image_detections
            GROUP BY class_name
            ORDER BY count DESC
            LIMIT %s;
        """, (limit,))
        rows = cur.fetchall()
        return [TopProduct(class_name=row[0], count=row[1]) for row in rows]
