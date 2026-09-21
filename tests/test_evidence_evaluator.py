from app.services.evidence_evaluator import EvidenceEvaluator


def test_sufficient_evidence():
    evaluator = EvidenceEvaluator()

    result = evaluator.evaluate(
        context=[
            "FastAPI is a Python web framework used to build APIs."
        ],
        retrieval_scores=[
            0.7884
        ],
    )

    assert result["is_sufficient"] is True
    assert result["score"] == 0.7884
    assert result["reason"] == "Relevant context found"


def test_insufficient_evidence():
    evaluator = EvidenceEvaluator()

    result = evaluator.evaluate(
        context=[
            "FastAPI is a Python web framework used to build APIs."
        ],
        retrieval_scores=[
            0.4931
        ],
    )

    assert result["is_sufficient"] is False
    assert result["score"] == 0.4931
    assert result["reason"] == "Evidence relevance below threshold"


def test_no_evidence():
    evaluator = EvidenceEvaluator()

    result = evaluator.evaluate(
        context=[],
        retrieval_scores=[],
    )

    assert result["is_sufficient"] is False
    assert result["score"] == 0.0
    assert result["reason"] == "No relevant context found"