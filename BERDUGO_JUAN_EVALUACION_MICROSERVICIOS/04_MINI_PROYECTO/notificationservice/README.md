# NotificationService

Microservicio de notificaciones siguiendo Clean Architecture.

## Instalación y ejecución

1. Instala dependencias:
   pip install -r requirements.txt
2. Ejecuta el servicio:
   uvicorn main:app --reload

## Endpoints
- POST /notifications
- GET /notifications/{user_id}
- PUT /notifications/{id}/read
- GET /health
