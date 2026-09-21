from types import SimpleNamespace

from app.services.agent_service import AgentService


def test_agent_success_path(monkeypatch):

    def fake_retrieve(query, limit=3, route="general"):
        return [
            SimpleNamespace(
                payload={
                    "text": "FastAPI is a Python web framework used to build APIs."
                },
                score=0.7884,
            )
        ]

    def fake_generate(self, prompt):
        return "FastAPI is a Python web framework used to build APIs."

    monkeypatch.setattr(
        "app.services.agent_service.retrieval_service.retrieve",
        fake_retrieve,
    )

    monkeypatch.setattr(
        "app.services.agent_service.LLMService.generate",
        fake_generate,
    )

    agent = AgentService()

    result = agent.run(
        "What is FastAPI?"
    )

    assert result["route"] == "technical"
    assert result["path"] == "technical"

    assert result["evidence_sufficient"] is True
    assert result["evidence_score"] == 0.7884

    assert result["answer_supported"] is True
    assert result["answer_score"] == 1.0

    assert result["answer_attempts"] == 1


def test_agent_blocks_insufficient_evidence(monkeypatch):

    def fake_retrieve(query, limit=3, route="general"):
        return [
            SimpleNamespace(
                payload={
                    "text": "FastAPI is a Python web framework used to build APIs."
                },
                score=0.4931,
            )
        ]

    monkeypatch.setattr(
        "app.services.agent_service.retrieval_service.retrieve",
        fake_retrieve,
    )

    agent = AgentService()

    result = agent.run(
        "Explain quantum computing architecture"
    )

    assert result["evidence_sufficient"] is False
    assert result["evidence_score"] == 0.4931

    assert result["answer"] == (
        "Evidence relevance below threshold"
    )

    assert result["answer_attempts"] == 0
    assert result["answer_supported"] is False