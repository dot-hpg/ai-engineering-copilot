from fastapi.testclient import TestClient

from app.main import app
from app.api.chat import ai_service


client = TestClient(app)


def test_chat_handles_agent_failure(monkeypatch):

    def fake_generate_response(question):
        raise RuntimeError("Simulated AI failure")

    monkeypatch.setattr(
        ai_service,
        "generate_response",
        fake_generate_response,
    )

    response = client.post(
        "/api/v1/chat",
        json={
            "question": "What is FastAPI?"
        },
    )

    assert response.status_code == 500
    assert response.json() == {
        "detail": "AI agent execution failed"
    }