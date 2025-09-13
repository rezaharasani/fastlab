from fastapi import status
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """Test root function"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    message = {"message": "Welcome to Github deployment with CI/CD pipeline"}
    assert response.json() == message


def test_health():
    """Test healthcheck function. It is so important for
       being successful running.
    """
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "OK"}
