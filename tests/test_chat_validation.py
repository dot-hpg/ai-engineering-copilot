from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_chat_rejects_empty_question():

    response = client.post(
        "/api/v1/chat",
        json={
            "question": ""
        },
    )

    assert response.status_code == 422


def test_chat_rejects_missing_question():

    response = client.post(
        "/api/v1/chat",
        json={},
    )

    assert response.status_code == 422  