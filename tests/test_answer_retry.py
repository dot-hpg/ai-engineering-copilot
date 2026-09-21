from app.services.agent_service import AgentService


def test_answer_retry(monkeypatch):

    responses = [
        "Kubernetes is a database system.",
        "FastAPI is a Python web framework used to build APIs.",
    ]

    def fake_generate(self, prompt):
        return responses.pop(0)

    monkeypatch.setattr(
        "app.services.agent_service.LLMService.generate",
        fake_generate,
    )

    agent = AgentService()

    result = agent.run(
        "What is FastAPI?"
    )

    assert result["answer_supported"] is True
    assert result["answer_attempts"] == 2
    assert result["answer_score"] >= 0.50