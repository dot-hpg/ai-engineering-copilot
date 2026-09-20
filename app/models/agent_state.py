from typing import TypedDict


class AgentState(TypedDict):
    question: str

    route: str

    classification_reason: str

    classification_confidence: float

    matched_keywords: list[str]

    path: str

    context: list[str]

    answer: str

    execution_time_ms: float