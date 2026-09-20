from typing import TypedDict


class AgentState(TypedDict):
    question: str

    route: str

    classification_reason: str

    classification_confidence: float

    matched_keywords: list[str]

    path: str

    context: list[str]

    retrieval_scores: list[float]

    evidence_sufficient: bool

    evidence_score: float

    evidence_reason: str

    answer: str

    execution_time_ms: float