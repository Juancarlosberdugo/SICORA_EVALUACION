from uuid import UUID
from app.domain.repositories.notification_repository import NotificationRepository

class MarkAsReadUseCase:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def execute(self, notification_id: UUID) -> None:
        self.repository.mark_as_read(notification_id)
