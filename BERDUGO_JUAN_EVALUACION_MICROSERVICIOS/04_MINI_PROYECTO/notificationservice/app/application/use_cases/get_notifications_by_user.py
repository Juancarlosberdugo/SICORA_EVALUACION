from uuid import UUID
from typing import List
from app.domain.entities.notification import Notification
from app.domain.repositories.notification_repository import NotificationRepository

class GetNotificationsByUserUseCase:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def execute(self, user_id: UUID) -> List[Notification]:
        return self.repository.get_by_user(user_id)
