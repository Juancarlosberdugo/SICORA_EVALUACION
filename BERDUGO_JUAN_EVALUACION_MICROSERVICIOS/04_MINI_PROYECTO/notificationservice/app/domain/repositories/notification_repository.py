from abc import ABC, abstractmethod
from ..entities.notification import Notification

class NotificationRepository(ABC):
    @abstractmethod
    async def create(self, notification: Notification) -> Notification:
        pass
