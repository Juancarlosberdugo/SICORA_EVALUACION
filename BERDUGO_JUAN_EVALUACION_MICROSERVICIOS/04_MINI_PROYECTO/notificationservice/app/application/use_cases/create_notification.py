from uuid import UUID
from app.domain.entities.notification import Notification
from app.domain.repositories.notification_repository import NotificationRepository

class CreateNotificationUseCase:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def execute(self, user_id: UUID, message: str) -> Notification:
        notification = Notification(user_id=user_id, message=message)
        return self.repository.create(notification)
