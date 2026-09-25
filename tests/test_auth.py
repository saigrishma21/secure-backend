from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Secure Backend API is running"


def test_register():
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser123",
            "email": "testuser123@example.com",
            "password": "testpassword123"
        }
    )

    assert response.status_code in [200, 400]


def test_login():
    response = client.post(
        "/auth/login",
        json={
            "username": "greeshma",
            "password": "mypassword123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_profile_without_token():
    response = client.get("/auth/profile")

    assert response.status_code == 401