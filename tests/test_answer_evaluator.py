from app.services.answer_evaluator import AnswerEvaluator


def test_supported_answer():
    evaluator = AnswerEvaluator()

    result = evaluator.evaluate(
        answer="FastAPI is a Python web framework used to build APIs.",
        context=[
            "FastAPI is a Python web framework used to build APIs."
        ],
    )

    assert result["is_supported"] is True
    assert result["score"] == 1.0
    assert result["reason"] == "Answer is supported by context"


def test_unsupported_answer():
    evaluator = AnswerEvaluator()

    result = evaluator.evaluate(
        answer="Kubernetes is a database system.",
        context=[
            "FastAPI is a Python web framework used to build APIs."
        ],
    )

    assert result["is_supported"] is False
    assert result["score"] < 0.50
    assert result["reason"] == (
        "Answer has insufficient support from context"
    )


def test_empty_answer():
    evaluator = AnswerEvaluator()

    result = evaluator.evaluate(
        answer="",
        context=[
            "FastAPI is a Python web framework used to build APIs."
        ],
    )

    assert result["is_supported"] is False
    assert result["score"] == 0.0
    assert result["reason"] == "Answer is empty"


def test_no_context():
    evaluator = AnswerEvaluator()

    result = evaluator.evaluate(
        answer="FastAPI is a Python web framework.",
        context=[],
    )

    assert result["is_supported"] is False
    assert result["score"] == 0.0
    assert result["reason"] == "No supporting context available"