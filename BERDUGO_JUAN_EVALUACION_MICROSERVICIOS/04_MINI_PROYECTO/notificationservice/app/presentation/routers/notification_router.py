from fastapi import APIRouter, Depends
from ..schemas.notification_schemas import CreateNotificationRequest, NotificationResponse
from ...application.use_cases.notification_use_cases import CreateNotificationUseCase
from ...infrastructure.repositories.notification_repository_impl import InMemoryNotificationRepository

router = APIRouter()

repo = InMemoryNotificationRepository()
use_case = CreateNotificationUseCase(repo)

@router.post("/notifications", response_model=NotificationResponse)
async def create_notification(request: CreateNotificationRequest):
    notification = await use_case.execute(
        user_id=request.user_id,
        title=request.title,
        message=request.message,
        notification_type=request.notification_type
    )
    return NotificationResponse(
        user_id=notification.user_id,
        title=notification.title,
        message=notification.message,
        notification_type=notification.type,
        read_status=notification.read_status,
        created_at=str(notification.created_at)
    )
