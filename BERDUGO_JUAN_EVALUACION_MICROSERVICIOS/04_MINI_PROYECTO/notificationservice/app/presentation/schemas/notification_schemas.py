from pydantic import BaseModel
from ...domain.value_objects.notification_type import NotificationType

class CreateNotificationRequest(BaseModel):
    user_id: str
    title: str
    message: str
    notification_type: NotificationType

class NotificationResponse(BaseModel):
    user_id: str
    title: str
    message: str
    notification_type: NotificationType
    read_status: bool
    created_at: str
