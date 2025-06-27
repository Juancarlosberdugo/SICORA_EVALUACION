from datetime import datetime
from ..value_objects.notification_type import NotificationType

class Notification:
    def __init__(self, user_id: str, title: str, message: str, notification_type: NotificationType):
        self.user_id = user_id
        self.title = title
        self.message = message
        self.type = notification_type
        self.read_status = False
        self.created_at = datetime.utcnow()
