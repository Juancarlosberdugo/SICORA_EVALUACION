from fastapi import FastAPI
from app.presentation.routers.notification_router import router as notification_router

app = FastAPI(title="Notification Service")
app.include_router(notification_router, prefix="/api/v1")
