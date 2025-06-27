from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: UUID
    message: str

class NotificationRead(BaseModel):
    id: UUID
    user_id: UUID
    message: str
    read_status: bool
    created_at: datetime

class MarkAsReadRequest(BaseModel):
    id: UUID
