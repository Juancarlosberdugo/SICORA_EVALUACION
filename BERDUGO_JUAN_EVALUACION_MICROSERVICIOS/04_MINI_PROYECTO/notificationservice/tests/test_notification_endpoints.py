import pytest
from fastapi.testclient import TestClient
from main import app
from uuid import uuid4

client = TestClient(app)

def test_create_notification():
    user_id = str(uuid4())
    response = client.post("/notifications", json={"user_id": user_id, "message": "Test message"})
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["message"] == "Test message"
    assert data["read_status"] is False

def test_get_notifications_by_user():
    user_id = str(uuid4())
    # Crear notificación
    client.post("/notifications", json={"user_id": user_id, "message": "Another message"})
    response = client.get(f"/notifications/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_mark_as_read():
    user_id = str(uuid4())
    # Crear notificación
    create_resp = client.post("/notifications", json={"user_id": user_id, "message": "Read me"})
    notification_id = create_resp.json()["id"]
    response = client.put(f"/notifications/{notification_id}/read")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
