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