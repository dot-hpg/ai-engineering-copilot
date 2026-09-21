from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Engineering question from the user",
    )


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []

    route: str
    path: str

    evidence_sufficient: bool
    evidence_score: float
    evidence_reason: str

    answer_supported: bool
    answer_score: float
    answer_evaluation_reason: str

    execution_time_ms: float