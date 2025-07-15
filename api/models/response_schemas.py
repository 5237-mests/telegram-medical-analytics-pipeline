# api/models/response_schemas.py
from pydantic import BaseModel
from typing import List, Optional

class TopProduct(BaseModel):
    class_name: str
    count: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class SearchResult(BaseModel):
    message_id: int
    message_text: str
    message_date: str
    sender_id: Optional[int] = None
