# api/routers/channels.py
from fastapi import APIRouter
# from typing import List
from api.db import get_connection
from api.models.response_schemas import ChannelActivity

router = APIRouter()

@router.get("/channels/{channel_name}/activity", response_model=list[ChannelActivity])
def get_channel_activity(channel_name: str):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT
                DATE(date) AS date,
                COUNT(*) AS message_count
            FROM raw.fct_messages
            WHERE channel_id = %s
            GROUP BY date
            ORDER BY date;
        """, (channel_name,))
        rows = cur.fetchall()
        return [ChannelActivity(date=str(row[0]), message_count=row[1]) for row in rows]
