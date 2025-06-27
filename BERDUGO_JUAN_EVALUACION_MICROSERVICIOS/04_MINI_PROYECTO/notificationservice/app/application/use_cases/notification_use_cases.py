from ...domain.entities.notification import Notification
from ...domain.repositories.notification_repository import NotificationRepository
from ...domain.value_objects.notification_type import NotificationType

class CreateNotificationUseCase:
    def __init__(self, notification_repo: NotificationRepository):
        self.notification_repo = notification_repo

    async def execute(self, user_id: str, title: str, message: str, notification_type: NotificationType) -> Notification:
        notification = Notification(user_id, title, message, notification_type)
        return await self.notification_repo.create(notification)
