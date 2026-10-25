from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


@patch("main.connect")
def test_health(mock_connect):
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@patch("main.connect")
def test_index(mock_connect):
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()