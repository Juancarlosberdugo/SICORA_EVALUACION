from ...domain.repositories.notification_repository import NotificationRepository
from ...domain.entities.notification import Notification

class InMemoryNotificationRepository(NotificationRepository):
    def __init__(self):
        self.notifications = []

    async def create(self, notification: Notification) -> Notification:
        self.notifications.append(notification)
        return notification
