# Test endpointu HTTP /ping
from src.app import app


def test_ping_endpoint():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200
    body = response.get_json()
    assert body["message"] == "pong"
