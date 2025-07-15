# api/main.py
from fastapi import FastAPI
from .routers import health, messages,  channels, trends, search, reports

app = FastAPI(title="Medigram Analytics API")

app.include_router(health.router, prefix="/api")
app.include_router(messages.router, prefix="/api")
app.include_router(channels.router, prefix="/api")
app.include_router(trends.router, prefix="/api")
app.include_router(search.router, prefix="/api")
app.include_router(reports.router, prefix="/api")
