# api/routers/search.py
from fastapi import APIRouter, Query
from api.db import get_connection
from api.models.response_schemas import SearchResult

router = APIRouter()

@router.get("/search/messages", response_model=list[SearchResult])
def search_messages(query: str = Query(..., min_length=1)):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, text, date, sender_id
            FROM raw.telegram_messages
            WHERE text ILIKE %s
            ORDER BY date DESC
            LIMIT 50;
        """, (f"%{query}%",))
        rows = cur.fetchall()
        return [SearchResult(
            message_id=row[0],
            message_text=row[1],
            message_date=str(row[2]),
            sender_id=row[3]
        ) for row in rows]
